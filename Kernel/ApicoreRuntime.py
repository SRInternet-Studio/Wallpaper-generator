"""Small runtime helpers shared by the interactive and ACW consumers."""

import re
from urllib.parse import quote

_TOKEN = re.compile(r"\{\{parameters\.([A-Za-z_][\w.-]*)\}\}")


def interpolate(value, parameters, *, url_encode=False):
    if isinstance(value, dict):
        return {k: interpolate(v, parameters, url_encode=url_encode) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [interpolate(v, parameters, url_encode=url_encode) for v in value]
    if not isinstance(value, str):
        return value

    def replace(match):
        name = match.group(1)
        if name not in parameters:
            raise ValueError(f"插值引用了未知参数: {name}")
        result = str(parameters[name])
        return quote(result, safe="") if url_encode else result

    return _TOKEN.sub(replace, value)


def _config_parts(doc):
    configs = doc.configs
    request = getattr(configs, "request", None) if configs else None
    if request is None:
        return None
    return request


def resolve_timeout(doc, settings_seconds, parameters):
    request = _config_parts(doc)
    timeout_ms = getattr(request, "timeout_ms", None) if request else None
    if timeout_ms is None:
        return float(settings_seconds)
    timeout_ms = interpolate(timeout_ms, parameters)
    try:
        resolved = float(timeout_ms) / 1000.0
    except (TypeError, ValueError) as exc:
        raise ValueError(f"无效的 request.timeout_ms: {timeout_ms}") from exc
    if resolved <= 0:
        raise ValueError("request.timeout_ms 必须大于 0")
    return resolved


def request_options(doc, parameters):
    request = _config_parts(doc)
    if request is None:
        return {"headers": {}, "body_type": "json", "body": parameters,
                "url": interpolate(doc.link, parameters, url_encode=True)}
    headers = interpolate(getattr(request, "headers", {}) or {}, parameters)
    body_type = getattr(request, "body_type", None) or "json"
    template = getattr(request, "body_template", None)
    body = interpolate(template, parameters) if template is not None else parameters
    url = interpolate(doc.link, parameters, url_encode=True)
    return {"headers": headers, "body_type": body_type, "body": body, "url": url}
