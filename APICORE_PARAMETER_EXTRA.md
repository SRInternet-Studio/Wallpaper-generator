# APICORE custom parameter contract

The parser requires every parameter, including a custom type, to provide
`type`, `friendly_name`, and `value`. `name` should identify the submitted
payload key when the HTTP method uses a request payload. Unknown parameter
types are rendered as read-only defaults: the application submits `value`
without inventing a widget or interpreting `extra` fields.

`extra` is reserved for type-specific metadata and must be a JSON object.
Namespaced keys are recommended (for example, `"x-wallpaper-generator": {}`)
to avoid collisions with fields added by APICORE. Until a renderer explicitly
supports a custom type, its `extra` content is preserved by the parser but is
not executed or used to build a control. This keeps third-party configuration
metadata forward-compatible and prevents unknown types from breaking the UI.
