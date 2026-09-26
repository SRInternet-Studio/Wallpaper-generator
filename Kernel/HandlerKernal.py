"""Runtime dispatch for APICORE HTTP status handlers."""

import asyncio
import re
import sys
import subprocess
import time
from dataclasses import dataclass
from typing import Any
from urllib.parse import quote
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import (QCheckBox, QDialog, QDialogButtonBox, QLabel,
                               QPlainTextEdit, QVBoxLayout)


def _get(value, name, default=None):
    if isinstance(value, dict):
        return value.get(name, default)
    return getattr(value, name, default)


def _path_value(data, path):
    current = data
    for part in (segment for segment in path.split(".") if segment):
        if isinstance(current, dict):
            current = current.get(part)
        elif isinstance(current, (list, tuple)) and part.isdigit():
            index = int(part)
            current = current[index] if index < len(current) else None
        else:
            return None
    return current


def evaluate_extract(expression, body, status):
    if isinstance(expression, dict):
        return {key: evaluate_extract(value, body, status) for key, value in expression.items()}
    if isinstance(expression, (list, tuple)):
        return [evaluate_extract(value, body, status) for value in expression]
    if not isinstance(expression, str):
        return expression
    if expression == "$body":
        return body
    if expression == "$status":
        return status
    if expression.startswith("$body."):
        return _path_value(body, expression[6:])
    if expression.startswith("$status."):
        return _path_value({"status": status}, expression[8:])
    return _path_value(body, expression)


def interpolate_message(message, values):
    if not isinstance(message, str):
        return "" if message is None else str(message)
    def replace(match):
        value = _path_value(values, match.group(1))
        return "" if value is None else str(value)
    return re.sub(r"\{\{([\w.-]+)\}\}", replace, message)


@dataclass(frozen=True)
class HandlerDecision:
    action: str
    rule: Any
    message: str = ""
    extracted: Any = None
    link: str | None = None


def handler_for_status(handlers, status):
    return handlers.get(str(status), handlers.get(status, handlers.get("default")))


def dispatch(status, handlers, body, parameters=None, translator=None):
    rule = handler_for_status(handlers, status)
    if rule is None:
        return HandlerDecision("response" if 200 <= int(status) < 300 else "error", None,
                               "" if 200 <= int(status) < 300 else f"HTTP 请求失败，状态码 {status}")
    action = _get(rule, "action", "error")
    action = getattr(action, "value", action)
    action = str(action).lower()
    extract = _get(rule, "extract")
    extracted = evaluate_extract(extract, body, status) if extract is not None else {}
    values = dict(parameters or {})
    values["parameters"] = dict(parameters or {})
    if isinstance(extracted, dict):
        values.update(extracted)
    else:
        values["value"] = extracted
    values.setdefault("body", body)
    values.setdefault("status", status)
    message_source = _get(rule, "message", "")
    if translator:
        message_source = translator(message_source)
    message = interpolate_message(message_source, values)
    link = _get(rule, "link")
    if isinstance(link, str):
        link = interpolate_message(link, values)
    return HandlerDecision(action, rule, message, extracted, link)


async def request_with_handlers(request_api, handlers, *args, request_kwargs=None, translator=None):
    """Run network and HTTP retry layers, then return the selected status action."""
    request_kwargs = dict(request_kwargs or {})
    retry_config = request_kwargs.pop("network_retry", None)
    if retry_config:
        request_kwargs["network_retries"] = int(_get(retry_config, "count", 3))
        request_kwargs["retry_delay_ms"] = int(_get(retry_config, "delay_ms", 10000))
    request_kwargs["return_status"] = True
    attempts = 0
    while True:
        result = await request_api(*args, **request_kwargs)
        body = result[1] if result[1] not in (None, "") else result[2] if result[2] not in (None, b"") else result[0]
        status = result[3]
        parameters = request_kwargs.get("payload") or {}
        decision = dispatch(status, handlers, body, parameters, translator)
        if decision.action != "retry":
            if decision.action == "error":
                raise RuntimeError(decision.message or f"HTTP 请求失败，状态码 {status}")
            return (*result, decision)

        retry = _get(decision.rule, "retry", decision.rule)
        limit = max(0, int(_get(retry, "count", 0)))
        delay_ms = max(0, int(_get(retry, "delay_ms", 0)))
        if attempts >= limit:
            fallback = handlers.get("default")
            if fallback is not None and fallback is not decision.rule:
                decision = dispatch(status, {"default": fallback}, body, parameters, translator)
                if decision.action == "error":
                    raise RuntimeError(decision.message or f"HTTP 重试次数已用尽，状态码 {status}")
                if decision.action != "retry":
                    return (*result, decision)
            raise RuntimeError(decision.message or f"HTTP 重试次数已用尽，状态码 {status}")
        attempts += 1
        await asyncio.sleep(delay_ms / 1000)


async def run_polling(request_api, polling, initial_response, handlers, parameters,
                      *, headers=None, ssl_verify=True, translator=None, network_retry=None):
    """Poll a configured check_link until its status handler resolves or its timeout expires."""
    template = _get(polling, "check_link")
    if not isinstance(template, str) or not template:
        raise ValueError("polling.check_link 不能为空")
    interval_ms = int(_get(polling, "interval_ms", 1000))
    timeout_ms = int(_get(polling, "timeout_ms", 60000))
    status_path = _get(polling, "status_path")
    success_value = _get(polling, "success_value")
    failed_value = _get(polling, "failed_value")
    if not status_path:
        raise ValueError("polling.status_path 不能为空")
    retries = max(0, int(_get(network_retry, "count", 0))) if network_retry else 0
    retry_delay_ms = max(0, int(_get(network_retry, "delay_ms", 10000))) if network_retry else 10000
    if interval_ms < 0 or timeout_ms <= 0:
        raise ValueError("polling.interval_ms / timeout_ms 配置无效")
    started = time.monotonic()
    response_context = initial_response
    while True:
        elapsed_ms = (time.monotonic() - started) * 1000
        remaining_ms = timeout_ms - elapsed_ms
        if remaining_ms <= 0:
            raise TimeoutError(f"异步轮询超时（{timeout_ms} ms）")

        def replace(match):
            value = _path_value(response_context, match.group(1))
            if value is None:
                raise ValueError(f"polling.check_link 引用的 response 字段不存在: {match.group(1)}")
            return quote(str(value), safe="")

        url = re.sub(r"\{\{response\.([\w.-]+)\}\}", replace, template)
        result = await request_api(url, "", "GET", headers=headers,
                                   timeout=max(0.1, remaining_ms / 1000),
                                   ssl_verify=ssl_verify, return_status=True,
                                   network_retries=retries, retry_delay_ms=retry_delay_ms)
        body = result[1] if result[1] not in (None, "") else result[2] if result[2] not in (None, b"") else result[0]
        status = result[3]
        # Poll completion is defined by the APICORE polling status field, not
        # by HTTP status handlers (which describe the endpoint's HTTP result).
        if not 200 <= int(status) < 300:
            decision = dispatch(status, handlers, body, parameters, translator)
            if decision.action == "error":
                raise RuntimeError(decision.message or f"轮询请求失败，HTTP {status}")
            if decision.action != "response":
                return (*result, decision)
        poll_status = _path_value(body, status_path)
        if failed_value is not None and poll_status == failed_value:
            raise RuntimeError(f"异步任务执行失败（{status_path}={poll_status}）")
        if poll_status == success_value:
            return (*result, HandlerDecision("response", None, extracted=body))
        await asyncio.sleep(min(interval_ms / 1000, max(0, remaining_ms) / 1000))


async def authorize_and_run(rule, config_id, parent):
    """Show the full command before running it; authorization is remembered per config and action."""
    script = _get(rule, "script", "")
    if not isinstance(script, str) or not script.strip():
        raise ValueError("APICORE run action 缺少 script")
    identifier = str(config_id or "unknown-config")
    settings = QSettings("SRInternet", "WallpaperGenerator")
    key = f"handler_run_authorized/{identifier}/run"
    approved = bool(settings.value(key, False, type=bool))
    front = bool(_get(rule, "front", False))
    if not approved:
        dialog = QDialog(parent)
        dialog.setWindowTitle("授权配置执行命令")
        dialog.setMinimumSize(620, 420)
        layout = QVBoxLayout(dialog)
        warning = "此命令将在前台窗口运行，请确认命令内容。" if front else "此命令可能修改系统或文件，请确认命令内容。"
        prompt = QLabel(f"配置 ID：{identifier}\n{warning}\n仅在信任此配置来源时继续。", dialog)
        prompt.setWordWrap(True)
        layout.addWidget(prompt)
        preview = QPlainTextEdit(dialog)
        preview.setReadOnly(True)
        preview.setPlainText(script)
        layout.addWidget(preview)
        remember = QCheckBox("记住此配置的 run 授权", dialog)
        layout.addWidget(remember)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.No, dialog)
        buttons.button(QDialogButtonBox.StandardButton.Yes).setText("授权并运行")
        buttons.button(QDialogButtonBox.StandardButton.No).setText("拒绝")
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        approved = dialog.exec() == QDialog.DialogCode.Accepted
        if approved and remember.isChecked():
            settings.setValue(key, True)
    if not approved:
        raise PermissionError("用户拒绝了 APICORE run action")

    kwargs = {"stdout": asyncio.subprocess.PIPE, "stderr": asyncio.subprocess.PIPE}
    if front and sys.platform == "win32":
        kwargs["creationflags"] = subprocess.CREATE_NEW_CONSOLE
    process = await asyncio.create_subprocess_shell(script, **kwargs)
    stdout, stderr = await process.communicate()
    output = (stdout or b"").decode(errors="replace").strip()
    error = (stderr or b"").decode(errors="replace").strip()
    if process.returncode:
        raise RuntimeError(error or f"run action 退出码：{process.returncode}")
    return output or error or "命令已完成。"
