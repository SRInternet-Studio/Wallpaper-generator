"""Application-facing read-only adapter for APICORE documents."""

from dataclasses import dataclass
from typing import Any, TypeAlias

from apicore import V1Document, V2Document, load, loads, parse, resolve_i18n, validate
from apicore.errors import APICoreError, ParseError, ValidationError

APICoreDocument: TypeAlias = V1Document | V2Document


def system_locale() -> str:
    """Use the system language when supported; otherwise prefer English."""
    try:
        from PySide6.QtCore import QLocale
        locale = QLocale.system().name().replace("_", "-")
    except Exception:
        import locale as system_locale_module
        locale = (system_locale_module.getlocale()[0] or "en-US").replace("_", "-")
    return "zh-CN" if locale.lower().startswith("zh") else "en-US"


def describe_apicore_error(error: Exception) -> str:
    """Translate parser failures into concise, actionable UI copy."""
    if isinstance(error, ValidationError):
        return f"APICORE 配置字段校验失败：{error}"
    if isinstance(error, ParseError):
        return f"APICORE 配置格式无法解析：{error}"
    if isinstance(error, APICoreError):
        return f"APICORE 配置加载失败：{error}"
    return str(error)


@dataclass(frozen=True)
class ApicoreDoc:
    raw: Any
    locale: str = ""

    def __post_init__(self):
        if not self.locale:
            object.__setattr__(self, "locale", system_locale())

    @property
    def family(self) -> str:
        return "v1" if str(getattr(self.raw, "apicore_version", "2.0")) == "1.0" else "v2"

    @property
    def spec_version(self) -> str:
        return str(getattr(self.raw, "apicore_version", "2.0"))

    @property
    def parameters(self) -> tuple:
        return tuple(getattr(self.raw, "parameters", ()) or ())

    @property
    def response(self):
        return getattr(self.raw, "response", None)

    @property
    def media(self):
        response = self.response
        return getattr(response, "preferred_media", None) if response is not None else None

    @property
    def others(self) -> tuple:
        response = self.response
        return tuple(getattr(response, "others", ()) or ()) if response is not None else ()

    @property
    def handlers(self) -> dict:
        return dict(getattr(self.raw, "handlers", {}) or {})

    @property
    def configs(self):
        return getattr(self.raw, "configs", None)

    @property
    def polling(self):
        return getattr(self.configs, "polling", None) if self.configs is not None else None

    def tr(self, value) -> str:
        if value is None:
            return ""
        return resolve_i18n(value, self.locale, fallback_locale="en-US")

    def supports(self, feature: str) -> bool:
        if feature == "media":
            return self.media is not None
        if feature == "handlers":
            return bool(self.handlers)
        if feature == "configs":
            return self.configs is not None
        if feature == "show_if":
            return any(getattr(p, "show_if", None) is not None for p in self.parameters)
        if feature == "polling":
            return self.configs is not None and getattr(self.configs, "polling", None) is not None
        if feature == "body_type":
            request = getattr(self.configs, "request", None) if self.configs else None
            return request is not None and getattr(request, "body_type", None) is not None
        return False

    @property
    def friendly_name(self) -> str:
        return self.tr(getattr(self.raw, "friendly_name", ""))

    @property
    def intro(self) -> str:
        return self.tr(getattr(self.raw, "intro", ""))

    @property
    def link(self) -> str:
        return getattr(self.raw, "link", "")

    @property
    def func(self) -> str:
        return getattr(self.raw, "func", "GET")

    @property
    def icon(self) -> str:
        return getattr(self.raw, "icon", "")


def _wrap(document: APICoreDocument) -> ApicoreDoc:
    return ApicoreDoc(document)


def load_doc(path: str) -> ApicoreDoc:
    return _wrap(load(path))


def validate_doc(path: str) -> ApicoreDoc:
    return _wrap(validate(path))


def loads_doc(content: str, format: str = "json") -> ApicoreDoc:
    return _wrap(loads(content, format=format))


def parse_doc(mapping) -> ApicoreDoc:
    return _wrap(parse(mapping))


__all__ = ["APICoreDocument", "ApicoreDoc", "load_doc", "loads_doc", "parse_doc", "validate_doc",
           "system_locale", "describe_apicore_error"]
