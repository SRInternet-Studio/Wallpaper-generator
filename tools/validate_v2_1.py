# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 使用说明：
# 1. 确保 Python 版本 >= 3.8
# 2. 安装依赖：pip install pyyaml tomli
# 3. 运行脚本：python validate_v2_1.py <配置文件路径>
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import json
import re
from pathlib import Path

# 尝试导入可选解析库
try:
    import yaml
except ImportError:
    yaml = None

try:
    import tomllib  # Python 3.11+ 标准库
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        tomllib = None

def load_config(file_path: str):
    path = Path(file_path)
    content = path.read_text(encoding='utf-8')
    suffix = path.suffix.lower()

    # 结合文件双扩展名判断 (.api.json, .api.yaml, .api.toml)
    full_name = path.name.lower()
    if full_name.endswith('.api.json') or suffix == '.json':
        return json.loads(content), content
    elif full_name.endswith('.api.yaml') or full_name.endswith('.api.yml') or suffix in ['.yaml', '.yml']:
        if not yaml:
            raise ImportError("需安装 PyYAML 以支持 YAML 验证: pip install pyyaml")
        return yaml.safe_load(content), content
    elif full_name.endswith('.api.toml') or suffix == '.toml':
        if not tomllib:
            raise ImportError("需安装 tomli 或升级至 Python 3.11+ 以支持 TOML 验证")
        return tomllib.loads(content), content
    else:
        raise ValueError(f"不支持的文件类型: {file_path}")

def validate_apicore_v2_1(file_path: str) -> bool:
    print(f"正在验证 APICORE 配置文件: {file_path} ...")
    try:
        config, raw_content = load_config(file_path)

        # 1. 基础必需字段检查
        required_fields = ['friendly_name', 'link', 'func', 'APICORE_version', 'parameters']
        for field in required_fields:
            assert field in config, f"缺少必需根字段: '{field}'"

        # 2. 版本检查
        version = str(config.get('APICORE_version'))
        assert version in ['2.0', '2.1'], f"APICORE_version 必须为 '2.0' 或 '2.1'，当前为: {version}"

        # 3. HTTP 方法合法性检查
        valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']
        assert str(config['func']).upper() in valid_methods, f"未知的 HTTP 方法: {config['func']}"

        # 4. 参数定义校验 & 收集参数名
        param_names = set()
        for i, param in enumerate(config.get('parameters', [])):
            # 通用基础 Meta 契约检查 (v2.1)
            assert 'type' in param, f"第 {i+1} 个参数缺少 'type' 字段 (Meta 契约必填)"
            assert 'friendly_name' in param, f"第 {i+1} 个参数缺少 'friendly_name' 字段 (Meta 契约必填)"
            assert 'value' in param, f"第 {i+1} 个参数缺少 'value' 字段 (Meta 契约必填)"

            p_name = param.get('name')
            if p_name:
                param_names.add(p_name)
            elif str(config['func']).upper() not in ['GET', 'HEAD']:
                print(f"⚠️  提醒: 在 {config['func']} 请求中，第 {i+1} 个参数的 'name' 为空")

            # v2.1: enum 类型建议检查 options/value 分离
            if param.get('type') == 'enum':
                if 'options' not in param and isinstance(param.get('value'), list):
                    print(f"⚠️  建议: 第 {i+1} 个 enum 参数仍使用旧版 value 数组写法，请迁移至 'options'(可选列表) + 'value'(默认值) 分离写法")

        # 5. 变量引用安全性检查 {{parameters.var_name}}
        variable_pattern = re.compile(r'\{\{parameters\.(\w+)\}\}')
        found_vars = variable_pattern.findall(raw_content)

        for var in set(found_vars):
            if var not in param_names:
                print(f"⚠️  警告: 发现引用了未定义的参数 '{{{{parameters.{var}}}}}'")

        # 6. Handlers 校验
        handlers = config.get('handlers', {})
        valid_actions = ['response', 'success', 'warning', 'error', 'message', 'retry', 'return', 'browser', 'run']

        for code, rule in handlers.items():
            if code != "default" and not str(code).isdigit():
                print(f"⚠️  警告: Handler 键名 '{code}' 建议统一使用 HTTP 状态码")

            assert 'action' in rule, f"状态码 '{code}' 的 Handler 配置缺少 'action' 字段"
            assert rule['action'] in valid_actions, f"状态码 '{code}' 的 action 类型 '{rule['action']}' 无效"

            if rule['action'] == 'response':
                assert 'response' in config, "存在 action='response' 的 Handler，但未声明根节点 'response' 对象"

            # v2.1: run 操作安全提醒
            if rule['action'] == 'run':
                print(f"ℹ️  提示: 状态码 '{code}' 使用了 'run' 操作，该配置需标记为 High Risk，客户端执行前必须获得用户明确授权")

        # 7. v2.1: 响应结构检查 (image / media 兼容性)
        response_cfg = config.get('response', {})
        if 'media' in response_cfg and 'image' in response_cfg:
            print("ℹ️  提示: 'response' 中同时声明了 'media' 与 'image'，将以 'media' 配置为准 (v2.1 优先级)")
        if not response_cfg or ('image' not in response_cfg and 'media' not in response_cfg):
            # response 不是必填，但若 handlers 有 response action 则需检查
            pass

        print("✅ 配置文件格式与语法验证通过！(APICORE v2.0/v2.1 兼容)")
        return True

    except ImportError as e:
        print(f"❌ 依赖缺失: {str(e)}")
        return False
    except ValueError as e:
        print(f"❌ 文件格式错误: {str(e)}")
        return False
    except AssertionError as e:
        print(f"❌ 规范校验失败: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ 校验失败: {str(e)}")
        return False

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else 'example_v2.api.json'
    validate_apicore_v2_1(target)
