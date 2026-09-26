# 壁纸生成器 6 NEXT — APICORE v2\.1 更新计划书

## 关键结论摘要（必读）

1. **解析内核已就绪**：[`APICORE_Python`](https://github.com/SRON-org/APICORE_Python) 2\.1\.0 通过单一 API `load()` / `loads()` / `parse()` / `validate()` 同时支持 **v1 / v2\.0 / v2\.1** 三规范，并自动识别未声明版本（缺省 v2\.0，含 v2\.1 独有字段则推断 v2\.1）。**本项目需内置解析器**。

2. **升级是一次 API 断层式替换，而非配置字段平替**：壁纸生成器 5 NEXT 调用的是旧版 `APICORE(path).init()` 及其 dict 式访问（`config.parameters()` 产出 `dict`，`param.get('type')`；`cfg.response().image()` 产出 `dict`，`.get('content_type')`）。新内核返回 **frozen dataclass**（`V1Document` / `V2Document`），字段为属性访问（`param.type`、`param.value`），无 `.get()` 方法。**所有消费点必须重写**。

3. **响应处理可大幅简化**：新模型 `ResponseConfig.preferred_media` 已内置 `media` 优先、`image` 自动降级为 `media`（`type="image"`）的裁决逻辑，\`UI 侧四分支 URL/BINARY × base64/文本判断可统一收敛为单一取值来源。

4. **i18n 由内核提供确定性解析**：`resolve_i18n(value, locale, fallback_locale=...)` 已实现「精确匹配 → 回退语言 → 首个翻译」规则；纯字符串原样返回。**无需再自行实现 i18n 解析逻辑**。

5. **枚举语义反转需双向处理**：v2\.1 中 `value` 为单个默认选中值，`options`/`friendly_options` 为列表；新版内核对两种写法均放行（有 `options` 时校验 `value` 属标量且存在于 `options`；无 `options` 时要求 `value` 为数组且 `friendly_value` 等长），**但读取侧仍必须区分**，否则选项显示错乱。

---

# 第一部分 · 任务清单

* [x] 1\. 配置模型重定义（Model Layer）

* [x] 1\.1 建立适配层类型别名与文档判别入口

* [x] 1\.2 封装 V1Document / V2Document 统一视图（Udoc）

* [x] 1\.3 封装 Parameter / ResponseConfig / HandlerRule 的只读访问面

* [x] 1\.4 明确响应媒体的唯一取值入口 preferred\_media

    * [x] 1\.5 定义 i18n 解析的系统语言判定策略（zh\-CN 优先 → en\-US 回退）

* [x] 1\.6 建立 custom 参数类型（Parameter\.extra）的字段约定

* [x] 2\. 解析器适配（Parser Layer）

* [x] 2\.1 替换 APICORE\(path\)\.init\(\) 为 apicore\.load\(path\)

* [x] 2\.2 文件发现层扩展三格式后缀（\.api\.json / \.api\.yaml / \.api\.toml）

* [x] 2\.3 依赖补齐与惰性导入策略（orjson / ruamel\.yaml / msgspec）

    * [x] 2\.4 异常映射：ParseError / ValidationError / APICoreError → 现有日志与 InfoBar 体系

* [x] 2\.5 版本协商参数的使用纪律（不传 version 覆写，尊重文档声明）

* [x] 2\.6 市场源下载内容的解析（字符串内容 → loads\(format=\.\.\.\)）

* [x] 3\. 页面控件映射（UI/Controls Layer）

* [x] 3\.1 控件注册表重构：补 number 类型，支持 custom 类型

* [x] 3\.2 enum 控件改造：options \+ friendly\_options \+ value 定位默认索引

* [x] 3\.3 number 控件：浮点支持与步长/精度处理

* [x] 3\.4 show\_if 条件联动：跨参数监听与隐藏仍提交默认值

* [x] 3\.5 enable=false 参数的隐藏与默认值直通

* [x] 3\.6 新字段落地：placeholder / text\_secret / tooltip

* [x] 3\.7 i18n 字段回显（控件标题、tooltip、options 友好名）

* [x] 3\.8 list 控件 split\_str 展示与值拼接兼容

* [x] 4\. 请求 Payload 构建（Payload Layer）

* [x] 4\.1 build\_payload 重写：dataclass 属性访问 \+ 类型化取值

* [x] 4\.2 enable=false 与 show\_if 隐藏参数的提交规则统一

* [x] 4\.3 required=false 且空值的剔除逻辑保持

* [x] 4\.4 GET/HEAD 与 非 GET/HEAD 的 payload 分发规则

* [x] 4\.5 插值执行：\{\{parameters\.name\}\} 作用于 link / headers / timeout\_ms / body\_template

* [x] 4\.6 body\_type 四种序列化实现（json / form\-data / x\-www\-form\-urlencoded / raw）

* [x] 4\.7 自定义请求头与默认 User\-Agent 的合并策略

* [x] 4\.8 split\_str 分隔符映射表构建逻辑修正

* [x] 5\. 响应处理（Response Layer）

* [x] 5\.1 统一经 preferred\_media 取值，废弃直接读 response\(\)\.image\(\)

* [x] 5\.2 media\.type 白名单校验（image 为默认支持，其余按策略处置）

* [x] 5\.3 content\_type=URL / BINARY 双路径保持

* [x] 5\.4 base64 与纯文本自适应分支保持

* [x] 5\.5 others 信息展示链路适配 dataclass

* [x] 5\.6 handlers 状态机执行器：9 种 action 的运行时行为

* [x] 5\.7 extract 求值（含 $body / $status）与 \{\{key\}\} 消息插值

* [x] 5\.8 default 兜底与未定义状态码处理

* [x] 5\.9 双轨重试：configs\.retry（网络层）与 handlers\.retry（HTTP 层）

    * [x] 5\.10 polling 异步轮询的执行器与取消语义

* [x] 5\.11 run 操作的安全授权与记忆

* [x] 6\. v2\.1 官方校验合规（Compliance Layer）

    * [x] 6\.1 以 validate\_v2\_1\.py 规则建立本地校验基线

    * [x] 6\.2 与 apicore\.validate\(\) 的双重校验分工界定

    * [x] 6\.3 内置 EnterPoint 存量文件扫描与整改清单

* [x] 6\.4 \_AutoConfig\.api\.json 生成端的版本升级与字段补全

    * [x] 6\.5 Schema 文件随仓库分发与 IDE 映射配置

    * [x] 6\.6 校验失败的用户可见提示与降级路径

* [x] 7\. 自动更换壁纸消费端（ACW Layer）

* [x] 7\.1 init\_cfg 适配 dataclass 与 intro 身份断言保持

* [x] 7\.2 payload 参数提取逻辑适配

* [x] 7\.3 change\_wallpaper 的响应解析统一改造

* [x] 7\.4 配置描述文本的 i18n 渲染

* [x] 8\. 打包与依赖（Packaging Layer）

* [x] 8\.1 requirements\.txt / requirements\-linux\.txt 依赖补齐

* [x] 8\.2 pyproject\.json（auto\-py\-to\-exe）datas 与 hidden imports 更新

* [x] 8\.3 单例锁、chdir、OsKernal 既有启动约束复核

    * [x] 9\. 回归与验证（Verification Layer）

        * [x] 9\.1 v1 存量配置全量回归

        * [x] 9\.2 v2\.0 / v2\.1 新配置正向验证

        * [x] 9\.3 三格式（JSON/YAML/TOML）加载验证

        * [x] 9\.4 损坏/半损坏配置的容错验证

        * [x] 9\.5 市场源安装链路端到端验证

        * [x] 9\.6 自动更换壁纸全链路验证

        说明：市场安装与 ACW 换壁纸流程已用隔离环境端到端回归；API、下载器、确认对话框及系统桌面设置均使用本地模拟，无真实网络或桌面副作用。


---

# 第二部分 · 更新方案

## 2\.1 目标架构

```Plain Text
flowchart TD
    subgraph Discovery
        A1[SettingsKernal.Construct_control] *--> A2[三格式后缀匹配<br/>.api.json/.api.yaml/.api.toml]*
        A2 *--> A3[apicore.load path]*end
    subgraph Model
        B1[APICORE 适配层 ApicoreDoc] *--> B2[V1Document | V2Document]*
        B2 *--> B3[param 视图]*
        B2 *--> B4[response.preferred_media]*
        B2 *--> B5[handlers 规则表]*
        B2 *--> B6[resolve_i18n]*end
    subgraph UI
        C1[控件注册表<br/>integer/number/boolean/enum/string/list/custom] *--> C2[show_if 联动引擎]*
        C1 *--> C3[enable/placeholder/text_secret/tooltip]*end
    subgraph Runtime
        D1[interpolate 插值器] *--> D2[body_type 序列化]*
        D2 *--> D3[aiohttp 请求 + configs.retry 网络重试]*
        D3 *--> D4[handlers 状态机分发]*
        D4 *--> E1[action=response 主链路]*
        D4 *--> E2[success/warning/error/message]*
        D4 *--> E3[retry HTTP 层]*
        D4 *--> E4[browser/run/return]*end
    A3 *--> B1*
    B1 *--> C1*
    C1 *--> D1*
```

**分层职责**：Discovery 只负责发现与加载；Model 只负责只读视图与 i18n；UI 只负责渲染与取值；Runtime 只负责插值、序列化、请求与状态机。**四层之间禁止直接读取原始 dict**。

## 2\.2 模块变更点

|模块|变更类型|内容|
|---|---|---|
|`Kernel/ApicoreDoc.py`|**新增**|适配层：`load_doc(path) -> ApicoreDoc`，统一 V1/V2 访问面|
|`Kernel/ApicoreRuntime.py`|**新增**|插值器 `interpolate()`、body 序列化 `serialize_body()`、`resolve_timeout()`|
|`Kernel/HaandlerKernal.py`|**新增**|handlers 状态机 `dispatch()`、`evaluate_extract()`、消息插值、重试与轮询|
|`Kernel/APIKernal.py`|改造|`request_api()` 增加 `headers`/`body_type`/`body`/超时参数；HTTP 状态码随响应返回；`construct_api` 保留但不再承担插值|
|`Kernel/SettingsKernal.py`|改造|`Construct_control()` 扩展三格式；读取侧新增 v2\.1 元数据透出|
|`Kernel/MainKernal.py`|改造|图片解析入口改用 `preferred_media`；新增媒体类型白名单校验|
|`MainWindow.py`|改造|`PageTemplate` 控件映射、`build_payload`、`on_api_start`、`on_push_button_clicked`|
|`acw_next/AutoChageWallpaper.py`|改造|`init_cfg`、`change_wallpaper`、描述文本渲染|
|`Kernel/MarketKernal.py`、`Kernel/GithubKernal.py`|改造|文件过滤三后缀；市场内容字符串走 `loads(format=...)`|
|`Exception_Handler.py`、`Kernel/Logger.py`|保持|仅新增 APICORE 异常分类标签，不改结构|
|`UI/Controls/__init__.py`|改造|新增 `number` 导出与 `custom` 占位|

## 2\.3 接口与数据结构调整

### 2\.3\.1 加载接口（替换）

```Python
*# 旧（已废弃）*
from APICORE import APICORE
cfg = APICORE(path).init()          *# dict 风格：cfg.parameters() -> list[dict]*

*# 新*
from apicore import load, loads, parse, validate, resolve_i18n
from apicore.errors import ParseError, ValidationError, APICoreError

doc = load(path)                    *# 返回 V1Document | V2Document*
doc2 = validate(path)               *# 命名别名，校验导向调用点*
inline = loads(text, format="yaml") *# 市场内容等字符串输入*
mapping_doc = parse(mapping)        *# 程序化生成的配置*
```

**纪律**：`load()`/`validate()` 不传 `version=` 覆写参数。传入会与文档声明冲突时抛 `ValidationError`，且会掩盖配置自身版本信息。

### 2\.3\.2 适配层视图 `ApicoreDoc`

|访问器|返回|说明|
|---|---|---|
|`doc.family`|`"v1" | "v2"`|用于 UI 提示与能力降级|
|`doc.spec_version`|`"1.0" | "2.0" | "2.1"`|来自 `apicore_version`|
|`doc.raw`|原始 `Document`|便于特殊字段访问|
|`doc.parameters`|`tuple[Parameter, ...]`|dataclass 元组，非 dict|
|`doc.media`|`ResponseMedia | None`|**唯一媒体取值入口**，等价 `response.preferred_media`|
|`doc.handlers`|`dict[str, HandlerRule]`|空 dict 表示 v1 或未定义|
|`doc.configs`|`Configs | None`|v1 恒为 `None`|
|`doc.tr(field)`|`str`|`resolve_i18n(field, locale, fallback_locale="en-US")`|
|`doc.supports(feature)`|`bool`|`feature ∈ {show_if, polling, body_type, handlers, media}`|

`doc.media` 对 v1 文件自动由 `ResponseConfig.preferred_media` 从 `image` 降级生成（`type="image"`），**因此 UI 与 ACW 侧禁止再读 ****`response.image`**。

### 2\.3\.3 参数视图 `Parameter`（frozen dataclass，字段即真相）

|字段|类型|v1|v2\.0|v2\.1|
|---|---|---|---|---|
|`enable`|`bool`|✓ 默认 `True`|✓|✓|
|`name`|`str | None`|✓|✓|✓（GET/HEAD 可空）|
|`type`|`str`|✓|✓|✓（可自定义）|
|`required`|`bool`|✓ 默认 `True`|✓|✓|
|`value`|`Any`|✓|✓|✓（enum 为\*\*单个标量\*\*）|
|`friendly_name`|`str | dict`|`str`|`str`|`str | dict`|
|`friendly_value`|`tuple | None`|enum 必需|兼容|弃用但仍可用|
|`options`|`tuple | None`|✗ 拒绝|✗ 拒绝|✓|
|`friendly_options`|`tuple | None`|✗ 拒绝|✗ 拒绝|✓（支持 i18n 逐项）|
|`min_value` / `max_value`|`int | float | None`|integer 必需|可选|integer/number 建议|
|`split_str`|`str | None`|list 必需|✓|✓|
|`tooltip` / `placeholder`|`str | dict | None`|`str`|`str`|i18n|
|`text_secret`|`bool`|`str` 类型专用|✓|✓|
|`show_if`|`ShowIf | None`|✗ 拒绝|✗ 拒绝|✓|
|`extra`|`dict`|✓|✓|✓（自定义类型字段）|

`ShowIf`：`parameter: str`，`equals: Any = None`，`in_values: tuple | None`。**`equals`**** 与 ****`in`**** 二者必须且只能有一个**（内核强校验）。

### 2\.3\.4 运行时装载 `Configs` / `RequestConfig`

|字段|默认|v1|v2\.0|v2\.1|
|---|---|---|---|---|
|`request.body_type`|`"json"`|✗|✗|✓|
|`request.body_template`|`None`|✗|✗|✓|
|`request.headers`|`{}`|✗|✓|✓|
|`request.timeout_ms`|`30000`（可传插值字符串）|✗|✓|✓|
|`retry.count` / `retry.delay_ms`|`3` / `10000`|✗|✓|✓|
|`rate_limit.frequency` / `per`|`None` / `"min"`|✗|✓|✓|
|`polling.*`|无默认（全必填）|✗|✗|✓|

### 2\.3\.5 `APIKernal.request_api()` 新签名（重建）

```Python
async def request_api(
    api: str,
    paths=None,
    method: str = "GET",
    *,
    headers: dict | None = None,      # 已插值完成的头
    payload: dict | None = None,
    body_type: str = "json",          # 新增
    raw: bool = False,
    ssl_verify: bool = True,
    timeout: int | float = 15,        # 秒
    split_str: dict | None = None,
    return_status: bool = True,       # 新增：返回 HTTP 状态码供 handlers 分发
) -> tuple[data, text, content, status]
```

`timeout` 保留秒级外部接口，内部换算 `aiohttp.ClientTimeout`；已有连接/读取分拆逻辑（connect≤10s）保持。

## 2\.4 配置项迁移规则

|v1 写法|v2\.1 等价写法|备注|
|---|---|---|
|`"type":"enum", "value":[0,1,2], "friendly_value":["否","是","可能"]`|`"type":"enum", "options":[0,1,2], "friendly_options":["否","是","可能"], "value":2`|**语义反转**，`value` 由「全部选项」变为「默认选中值」|
|`response.image{content_type,path,is_list,is_base64}`|`response.media{type:"image",content_type,path,is_list,is_base64}` 或保留 `image`|内核 `preferred_media` 两种均可；新配置推荐 `media`|
|调用方硬编码 `User-Agent` / `Authorization`|`configs.request.headers`|**必须迁出代码**，否则配置侧无法覆盖|
|调用方 `timeout=settings.timeout_config`|`configs.request.timeout_ms`（毫秒）优先，缺省回退用户设置|单位不同，禁止直接相等|
|调用方 `retries=1`|`configs.retry{count,delay_ms}`|网络层重试|
|调用方裸 `raise RuntimeError`|`handlers.<status>` 规则 \+ `default`|状态机接管|

**`_AutoConfig.api.json`**** 生成规则**：

`APICORE_version` 由 `"1.0"` 升为 `"2.1"`；补 `id`（以源配置名生成稳定 slug）、`version`、`updated_at`（ISO 8601 日期）；`response` 改为 `media` 形式；**保留 ****`intro == "Auto Change Wallpaper Config"`**** 不变**（`AutoChageWallpaper.init_cfg` 的身份断言依赖它）；保留文件名 `_AutoConfig.api.json` 与 `acw_config/` 目录结构（`_` 前缀是其不被主界面枚举的机制，见 4\.2）。但需注意：v2\.1 要求 `friendly_name` 若为 dict 时必须含至少一个 locale，因此该字段继续用**纯字符串**最稳妥。

## 2\.5 向后兼容策略

```Plain Text
flowchart LR
    L[load path] *--> V{内核判别}*
    V *-->|APICORE_version=1.0| V1[V1Document]*
    V *-->|2.0 / 未声明| V20[V2Document 2.0]*
    V *-->|2.1| V21[V2Document 2.1]*
    V1 *--> U[ApicoreDoc 统一视图]*
    V20 *--> U*
    V21 *--> U*
    U *--> UI[同一套控件与运行时代码]*
```

1. **内核级兼容由 ****`APICORE_Python`**** 提供**：v1 文档返回 `V1Document`，其 `parameters` / `response` / `configs=None` / `handlers={}` 字段齐备。**适配层不做 v1→v2 数据改写**，仅在访问侧判空。

2. **UI 级兼容**：enum 读取按 `param.options is not None` 二分支；`show_if`/`preferred_media`/`configs` 一律判空后走降级路径。

3. **v1 存量文件零改动运行**：`EnterPoint/` 中 17 个 v1 文件在 `v6` 中应保持可读可用，仅在 UI 上标注「兼容模式」徽标（可选）。

4. **v1 独有约束由内核强制执行**：v1 的 `integer` 必须带 `min_value`/`max_value`、v1 `enum` 必须 `friendly_value` 等长、v1 拒绝 `configs`/`handlers`/`options`/`show_if`/`media`。这些不再是应用层责任。

---

# 第三部分 · 详细要点解析

## 3\.1 字段映射与类型转换

|层|旧写法（dict）|新写法（dataclass）|转换要点|
|---|---|---|---|
|文档标题|`cfg.friendly_name()`|`doc.tr(doc.raw.friendly_name)`|v1 为 `str` 直接透传；v2\.1 可能 `dict`|
|参数遍历|`for p in cfg.parameters(): p.get('type')`|`for p in doc.parameters: p.type`|dataclass 无 `.get()`；`.value` 保持原类型|
|enum 选项|`param.get('value')`|`param.options`|旧字段在 v2\.1 语义已变，**禁止再当列表用**|
|enum 友好名|`param.get('friendly_value')`|`param.friendly_options`|逐项可能为 i18n dict|
|enum 默认索引|`setCurrentIndex(0)`|`options.index(value)`，用 `_same_value` 语义（\*\*类型与值同时相等\*\*）匹配|内核 `_same_value` 要求 `type(left) is type(right)`，故 `"1"` 与 `1` 不相等|
|响应媒体|`cfg.response().image().get('content_type')`|`doc.media.content_type`|唯一入口|
|响应路径|`cfg.response().image().get('path')`|`doc.media.path`|v2\.1 `media.path` 允许空串仅当 `content_type=BINARY`|
|响应列表|`cfg.response().image().get('is_list', True)`|`doc.media.is_list`（默认 `False`）|**默认值方向变了**：v1 代码默认 `True`，内核默认 `False`，需显式读取|
|others|`other.get('friendly_name')`|`other.friendly_name` / `field.path`|`ResponseGroup.data` 已是 `ResponseDataField` 元组|
|请求超时|`settings["timeout_config"]`（秒）|`configs.request.timeout_ms`（毫秒，允许 `{{parameters.x}}`）|插值后须转 int|
|HTTP 方法|`cfg.func().upper()`|`doc.raw.func`|内核已限定大写白名单（v2\.1: GET/POST/PUT/DELETE/HEAD/PATCH/OPTIONS）|

## 3\.2 默认值与可选字段处理

1. **`enable`**** 默认 ****`True`**：旧代码 `param.get('enable', True)` 一致，但必须显式读 `param.enable`。

2. **`required`**** 默认 ****`True`**：与旧代码 `param.get('required', False)` **不一致**——旧代码缺省视为非必填，新内核缺省视为必填。统一以 `param.required` 为唯一真相，并复核 v1 存量文件中缺 `required` 的参数语义漂移。

3. **`text_secret`**** 默认 ****`False`**，仅 `type=="string"` 有效（内核校验）。

4. **`placeholder`**** 仅 ****`string`**** 有效**（内核校验），非 string 传值直接 `ValidationError`。

5. **`min_value`****/****`max_value`**** 仅 ****`integer`****/****`number`**** 有效**（内核校验）；v1 的 `integer` 二者必填。

6. **`is_list`**** / ****`is_base64`**** 默认 ****`False`**：旧代码默认值不一致（`is_list` 旧默认 `True`），必须改为显式 `doc.media.is_list`。

7. **`retry.count`**** 默认 3 / ****`delay_ms`**** 默认 10000**；`rate_limit.per` 默认 `"min"`；`request.timeout_ms` 默认 30000。

8. **`configs`**** 整体可为 ****`None`**（v1 或 v2 未声明），四个子对象均需判空。

9. **`handlers`**** 为空 dict** 时退化为 v1 行为：`HTTP 2xx` 走主链路，其余抛错。

## 3\.3 版本协商与容错逻辑

1. **不得传 ****`version=`**** 覆写**：`_detect_version` 在 `requested` 与文档声明跨族冲突时抛 `ValidationError`。

2. **未声明 ****`APICORE_version`** → 内核按 v2\.0 语义；若含 v2\.1 独有字段（`$schema/id/version/author/license/repository/updated_at`、i18n 化 `friendly_name`/`intro`/`tooltip`/`placeholder`、`configs.polling`、`configs.request.body_type/body_template`、`parameters[].options/friendly_options/show_if`、`response.media`、i18n 化 `handlers[].message` 或 `others` 友好名）则**推断为 v2\.1**。

3. **v2\.0 文档携带 v2\.1 元数据** → `ValidationError: APICORE v2.1 metadata requires APICORE v2.1: [...]`。应用层需将该信息转为「请将 `APICORE_version` 升级为 `"2.1"`」的用户提示。

4. **v2\.1 的 ****`response`**** 必须至少声明 ****`media`**** 或 ****`image`**** 之一**；v2\.0/v1 允许 `others` 兜底。

5. **handlers 键名校验**：v2\.1 要求三位状态码（100–599）或 `default`；v2\.0 放宽为纯数字或 `default`。**TOML 中键 ****`"200"`**** 必须加引号**，否则 TOML 解析为字符串已满足，但 JSON/YAML 中的 `200` 会被 `_build_handlers` 的 `_is_int` 转为 `"200"`，无需应用层处理。

6. **`run`**** 的 ****`script`**** 必填、****`browser`**** 的 ****`link`**** 必填、****`retry`**** 的 ****`count`****/****`delay_ms`**** 必填**，由内核保证；应用层只实现执行语义。

7. **插值校验在内核**：`{{parameters.x}}` 引用未定义参数名会抛 `ValidationError`；`link` 仅允许 `{{parameters.*}}`，`polling.check_link` 仅允许 `{{response.*}}`，且禁止插值出现在 scheme/netloc/fragment。**应用层不应重复实现该校验**，只需在执行期做值替换。

8. **`show_if`**** 自引用与悬空引用**由内核拒绝（`cannot reference the same parameter` / `references unknown parameter`）。

9. **参数重名**由内核拒绝（`$.parameters contains duplicate parameter names`）——这消除了旧代码 `param_identifier` 冲突的隐患。

10. **URL 模板卫生**：内核在替换插值为字面量后再跑 `_validate_url`，因此 `https://api.example.com/users/{{parameters.uid}}` 合法，`https://{{parameters.host}}/x` 非法。应用层插值时应对参数值做 URL 编码（`quote(str(v), safe='')`），防止注入。

## 3\.4 消费端调用方式变更

### 3\.4\.1 `MainWindow.py` · `PageTemplate`

```Python
*# 旧
class PageTemplate(QWidget, PageTemplate_ui.Ui_Form):
    def __init__(self, parent=None, config: APICORE=None):
        for param in config.parameters():
            name = str(param.get('type')).lower()
            if not bool(param.get('enable', True)): continue
            ...
            opts = param.get('friendly_value')
            if opts is not None:
                if len(opts) == len(param.get('value')): ...

# 新（示意）
def __init__(self, parent=None, doc: ApicoreDoc = None):
    ...
    for param in doc.parameters:
        name = param.type.lower()
        if not param.enable: continue
        ...
        match name:
            case "enum":
                if param.options is not None:
                    self._fill_enum(param, ui)          # options + friendly_options
                else:
**                    self._fill_legacy_enum(param, ui)   # value 数组 + friendly_value*
```

控件注册表需扩展：

```Python
control_classes = {
    "integer": (integer, 1, 3),
    "number":  (number,  1, 3),     *# 新增*
    "boolean": (boolean, 1, 3),
    "enum":    (emum,    1, 3),
    "string":  (string,  1, 3),
    *# list 复用 string；custom 走 extra 驱动的兜底渲染*
}
```

`enable=false` 与 `show_if` 不满足时的统一规则：**隐藏控件，但提交 ****`param.value`**。因此 `build_payload` 不能以「控件是否存在」为唯一判据，需引入 `is_visible(param)` 谓词。

### 3\.4\.2 `build_payload()`

- 取值源：`param.value`（隐藏时）或控件当前值（可见时）。

- `enum` 取值：`param.options[idx]`；兼容分支取 `param.value[idx]`。

- `list` 取值：按 `param.split_str` 切分；**`split_str`**** 缺省时不再默认 ****`"|"`**，内核对 `list` 已强制 `split_str` 非空，直接读 `param.split_str`。

- 剔除规则保持：`value` 为假且 `param.required` 为假时不入 payload。

- **禁止**在 payload 里塞 `friendly_name`（友好参数仅用于展示，旧代码已分离，保持）。

### 3\.4\.3 `on_api_start()`

```Python
media = doc.media                      # 唯一入口
if media.type != "image":
    # 按策略处置：拒绝并提示，或下载为文件（见注意事项）
binary_phrase = media.content_type.upper() == "BINARY"
r, t, c, status = await APIKernal.request_api(
    doc.raw.link,                      # 已插值
    "",
    doc.raw.func,
    headers=interpolate_headers(...),
    payload=payload,
    body_type=body_type,
    split_str=split_str,
    raw=binary_phrase,
    ssl_verify=...,
    timeout=resolve_timeout(doc, settings),
)
```

原四分支 `URL/BINARY × base64/文本` 保持不变，仅把 `cfg.response().image()` 换成 `media`。

### 3\.4\.4 `acw_next/AutoChageWallpaper.py`

- `init_cfg()`：`doc = load(path)`；身份断言 `doc.tr(doc.raw.intro) == "Auto Change Wallpaper Config"` 或直接 `doc.raw.intro == "..."`（生成侧保持纯字符串，故直接比较安全）。

- payload 提取：`for p in doc.parameters: if p.name == "payload": self.payload = p.value`。

- 描述文本：`for p in doc.parameters: if p.friendly_name: self.description_text += f" {doc.tr(p.friendly_name)}：{p.value}\n"`。**注意 v2\.1 ****`friendly_name`**** 可能是 dict，必须经 ****`tr()`**。

- `change_wallpaper()`：与 3\.4\.3 同构改造。

## 3\.5 `validate_v2_1.py` 校验合规要求

本项目须以内核 `apicore.validate()` 为主校验器，官方 `validate_v2_1.py` 为**基线行为对照**。二者差异必须明确：

|校验项|`validate_v2_1.py`|`apicore 2.1.0` 内核|本项目采纳|
|---|---|---|---|
|根必填字段|`friendly_name, link, func, APICORE_version, parameters`|同（但 `APICORE_version` 可缺省并推断）|内核|
|版本白名单|`["2.0","2.1"]`（拒绝 v1）|`1.0/2.0/2.1`|内核（需兼容 v1 存量）|
|HTTP 方法白名单|7 种全大写|v2\.1 同 7 种；v2\.0/v1 用 `http.HTTPMethod` 全集|内核|
|enum 旧写法|⚠️ 警告仍放行|✅ 放行但强制 `friendly_value` 等长|内核|
|参数引用未定义|⚠️ 警告|❌ `ValidationError`|内核|
|`run` 操作|ℹ️ 提示高风险|仅强制 `script` 非空|**应用层补充授权**|
|`media`\+`image` 并存|ℹ️ 提示以 `media` 为准|✅ 放行，`preferred_media` 已实现|内核|
|`action=response` 但 response 空|✅（因要求根字段必有 response）|❌ `ValidationError`|内核|

**合规落点**：内置 `EnterPoint/` 全部文件在提交前须通过 `python APICORE-2/APICORE-2/validate_v2_1.py <file>` 且通过 `apicore.validate()` 双重校验；`_AutoConfig.api.json` 生成后须自校验一次，失败则阻断写入并告警。

---

# 第四部分 · 注意事项

## 4\.1 迁移风险（按严重度排序）

|\#|风险|触发场景|缓解措施|
|---|---|---|---|
|R1|**API 断层导致全面崩溃**|旧 dict 式代码遇到 dataclass，`AttributeError: 'Parameter' object has no attribute 'get'`|以适配层 `ApicoreDoc` 收束全部访问；全局搜索 `.get(` 于 APICORE 相关调用链；禁止在 UI/ACW 直接持有 `Document`|
|R2|**enum 语义反转静默错值**|旧代码把 `param.value` 当选项数组，v2\.1 下变成单值|3\.4\.1 二分支实现；对 `options is None and value not list` 的情况显式告警|
|R3|**`is_list`**** 默认值反转**|旧 `cfg.response().image().get('is_list', True)` vs 内核默认 `False`|一律显式读 `media.is_list`，禁止传默认值|
|R4|**`required`**** 默认语义漂移**|旧默认 False、内核默认 True，导致空值被提交|以 `param.required` 为唯一真相；扫描存量 v1 文件统计缺省数量并评估|
|R5|**`run`**** 任意命令执行**|恶意市场配置|默认拒绝；授权弹窗含完整脚本文本与来源标识；授权结果按「配置 id \+ action」记忆；`front=true` 额外警示|
|R6|**插值注入**|用户输入含 `/ ? # &` 等破坏 URL|执行期对参数值 `quote(str(v), safe='')`，仅对路径段与 query 值，不编码已由配置写死的结构|
|R7|**YAML/TOML 依赖体积**|PyInstaller 打包|惰性导入；YAML 必须 `ruamel.yaml`（内核依赖），\*\*不要\*\*换成 PyYAML；TOML 必须 `msgspec`|
|R8|**market 内容为字符串**|`GithubKernal` 返回 `str`|用 `loads(content, format="json")` 而非 `load(path)`；同时保留原文用于缓存|
|R9|**超时单位混淆**|`timeout_ms`（毫秒）vs `timeout_config`（秒）|集中 `resolve_timeout()`，统一内部用秒；日志记录最终取值与来源|
|R10|**双重重试叠加爆炸**|`configs.retry` 与 `handlers.retry` 同时触发|严格分层：网络层重试只包住连接/超时；HTTP 层重试只在收到响应后按状态码触发；两者不得嵌套循环|

## 4\.2 边界情况

1. **`_`**** 前缀约定**：`Construct_control` 仅以「非 `_` 前缀 \+ 三后缀」筛选，`EnterPoint/acw_config/_AutoConfig.api.json` 依赖此机制隐藏。**改动筛选逻辑时不得破坏该约定**，否则自动换壁纸配置会作为普通图片源出现在主界面（且其 `intro` 断言会误导）。

2. **用户目录与内置目录分离**：`get_config_dir()/EnterPoint/` 与仓库 `EnterPoint/` 是两套；v6 若做「v1 存量归一化」，只动用户目录，且必须备份原文件。

3. **TOML 中 handlers 键**：`[handlers."200"]` 引号不可省；`[handlers.default]` 无需引号。

4. **JSON 中 ****`200`**** 为数字键**：内核 `_is_int(key)` 已转字符串，应用层读取 `doc.handlers["200"]` 时用字符串键。

5. **`polling`**** 的双向插值**：`check_link` 允许 `{{response.xxx}}`，但首次响应尚未产生该值前无法求值 → 必须先完成 `action=response` 提取或按 `extract` 取得 `task_id` 后再插值；`polling` 与 `handlers` 的执行顺序需定义为「先 handlers 定稿首次响应 → 再轮询」。

6. **`body_type="raw"`**** \+ ****`body_template`**** 为字符串**：其余类型 `body_template` 为对象；序列化分支必须按 `body_type` 区分，不允许一律 `json.dumps`。

7. **`form-data`**** 与文件**：v2\.1 未定义文件上传语义，`form-data` 仅承载普通键值；遇到二进制文件需求应在 `Parameter.extra` 自定义并显式提示暂不支持。

8. **`custom`**** 参数类型**：内核**不校验**自定义类型字段有效性，仅要求 Meta 契约必填项齐备。应用层需对未知 `type` 走「隐藏 \+ 提交 `value`」的保守渲染，并 `logger.warning`，禁止崩溃。

9. **空 ****`handlers`**** 的 v2\.1 文档**：`action=response` 不会自动生效，需应用层约定「v2\.1 无 handlers 时 2xx 走主链路，其余报错」，与 v1 行为对齐。

10. **enumerate 索引定位控件**：旧代码用 `config.parameters().index(param)` 生成 `param_N` 标识；新代码改用 `enumerate`，避免同名对象 `index()` 返回首个匹配的 bug。

## 4\.3 验证节点

|节点|通过标准|
|---|---|
|V1 解析|17 个内置 v1 文件全部 `load()` 成功且 `family == "v1"`|
|V2 加载|JSON/YAML/TOML 三格式同构配置产出等价 `V2Document`|
|控件渲染|v1/v2\.1 各类型参数均能渲染；`number`、`show_if`、`text_secret`、`tooltip`、`placeholder` 生效|
|Payload|隐藏参数提交默认值；空值剔除规则不变；enum 取得 `options[idx]`|
|请求|四种 `body_type` 请求体正确；`headers` 插值生效；`timeout` 解析正确|
|响应|URL/BINARY × base64/文本 四分支产出与 v1 一致；`others` 正确展示|
|handlers|9 种 action 逐一验证；`default` 兜底；`retry` 超限降级；`extract` \+ `$body`/`$status` \+ 消息插值|
|ACW|init\_cfg 断言通过；换壁纸全链路；i18n 描述文本|
|合规|`validate_v2_1.py` \+ `apicore.validate()` 双绿|
|容错|损坏文件 / 半损坏字段 / 未知参数类型 / 未知 media 类型均不崩溃且有可读提示|
|打包|PyInstaller 三格式配置在 frozen 模式下可加载（注意 `sys.frozen` 与 `get_internal_dir()`）|

## 4\.4 回滚考虑

1. **代码回滚**：迁移须保持「内核替换」与「消费端改造」两个可独立回滚的提交单元。适配层先行落地时，旧消费端仍可用旧 `APICORE` 包，保证任一环节可单独 revert。

2. **配置回滚**：不得原地覆写用户配置文件。任何归一化/升级操作写入新文件并保留原件（如 `*.api.v1.bak`），失败即恢复。

3. **v1 包共存**：`APICORE_Python` 2\.1\.0 已同时支持 v1，**无需保留旧 ****`APICORE`**** 依赖**。但迁移窗口期内两套并存会造成 `from APICORE import APICORE` 与 `from apicore import load` 混用，须以适配层为唯一出口，逐步清除旧导入残留并在 CI/提交前全局搜索确认归零。

4. **数据兼容面**：`config.json` / `acw_next/config.json` 结构与本次迁移无关，不动。唯一受影响的持久化数据是 `EnterPoint/acw_config/_AutoConfig.api.json`（由程序生成，可随时重建，降级时旧版程序会因 `APICORE_version` 不识别而重建该文件，须保证「重建而非报错」路径可用）。

## 4\.5 与现有 v1 配置共存的交互约束

1. **读取侧只读不改**：v1 文件在 v6 中以 `V1Document` 原样运行，不触发自动迁移。

2. **UI 能力降级提示**：v1 文档不具备 `show_if`/`configs`/`handlers`/`media` 时，相关 UI 区块不渲染而非报错。

3. **市场侧双向兼容**：市场源可能仍分发 v1 文件；安装时按内核判别执行，无需客户端转换。市场元数据（`id`/`version`/`updated_at`）缺失时以文件内容 hash 作为更新判断依据。

4. **写入侧立即升级**：仅 `_AutoConfig.api.json` 由 v6 生成时即采用 v2\.1 规范；该文件不回流市场、不进入内置 `EnterPoint/`，故不污染 v1 生态。

5. **`Kernal`**** 拼写与目录结构保持不变**：`Kernel/`、`MainKernal`、`APIKernal` 等既有命名与 `AGENTS.md` 中记录的导入顺序、`OsKernal` monkey\-patch、`chdir` 约束继续有效，本次迁移**不触碰**这些约束。
