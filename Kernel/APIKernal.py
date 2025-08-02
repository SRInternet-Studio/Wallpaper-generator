"""
PROJECT:    APIKernal - The request, parsing and batch parsing of the API are all completed in one step.
MODULE:     APIKernal.py
FUNCTION:   APIKernal is a module that encapsulates the request, parsing and batch parsing of the API.
AUTHOR:     SRInternet
DATE:       2025-06
VERSION:    1.0.0 (see Releases Notes)

DEPENDENCIES:
  - aiohttp
  - asyncio

NOTES:
  This module is compatible with Python 3.8+
"""

import aiohttp
import asyncio
from typing import Any, Dict, List, Optional, Union, Tuple
import json
import re

try:
    from Kernel.Logger import logger
except ImportError:
    from Logger import logger

def construct_api(api: str, payload: Optional[Dict[str, Any]] = None, split_str: Dict[str, str] = {}):
    """构造请求的URL和参数
    
    :param api: API端点URL
    :param payload: 请求负载(对于POST/PUT等)
    :param split_str: 对于是列表类型的请求负载，如果是 GET 方法，则将列表中的每个值用此字符连接（缺省为 '|'）"""
    
    url = api.rstrip('/').rstrip('?')
    none_params = []
    other_params = {}
    
    # 分离None键和其他参数
    for key, value in payload.items():
        if key is None:
            none_params.append(str(value))
        else:
            s = split_str.get(key, "")
            if not s:
                s = '|'
                
            if isinstance(value, list):
                other_params[key] = s.join(str(v) for v in value)
            else:
                other_params[key] = value
    
    # 构建最终URL
    if none_params:
        url += '/' + '/'.join(none_params)
    if other_params:
        url += '?' + '&'.join(f'{k}={v}' for k, v in other_params.items())
    
    logger.debug(f"构建的请求URL: {url}")
    return url
                
# 请求函数
async def request_api(
    api: str,
    paths: Optional[Union[str, List[str]]] = None,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    payload: Optional[Dict[str, Any]] = None,
    split_str: Dict[str, str] = {},
    timeout: int = 15, 
    raw = False
) -> Any:
    """
    异步执行API请求并解析响应数据
    
    :param api: API端点URL
    :param paths: 要解析的一个或多个路径
    :param method: HTTP方法 (GET, POST, etc.)
    :param headers: 请求头
    :param payload: 请求负载(对于POST/PUT等)
    :param split_str: 对于是列表类型的请求负载，如果是 GET 方法，则将列表中的每个值用此字符连接（缺省为 '|'）
    :param timeout: 超时时间(秒)
    :param raw: True = 返回原始数据，False = 返回按照 paths 解析后的数据
    :return: 解析后的数据
    """
    headers = headers or {}
    payload = payload or {}
    
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
            if method.upper() in ["GET", "HEAD"]:
                url = construct_api(api, payload, split_str)
                async with session.request(method, url, headers=headers) as response:
                    return await handle_response(response, paths, raw)
            else:
                async with session.request(method, api, headers=headers, json=payload) as response:
                    return await handle_response(response, paths, raw)
    except asyncio.TimeoutError:
        raise RuntimeError(f"API请求超时: 超过 {timeout} 秒")
    except aiohttp.ClientError as e:
        error_msg = f"API请求失败: {str(e)}"
        if hasattr(e, 'status') and e.status:
            error_msg += f" (状态码: {e.status})"
        raise RuntimeError(error_msg)

# 响应处理函数
async def handle_response(response: aiohttp.ClientResponse, paths: Optional[Union[str, List[str]]] = None, raw = False) -> Tuple[Any, Any, Any]:
    """处理响应并返回解析后的数据（由 request_api 调用）"""

    try:
        content = await response.text()
    except UnicodeDecodeError:
        content = await response.text('latin1')
    
    if not response.ok:
        error_msg = f"API返回错误: {response.status} {response.reason}"
        if content:
            error_msg += f"\n错误详情: {content[:200]}..."
        raise RuntimeError(error_msg)
    
    if raw:
        return response, content, await response.read()
    
    # 解析JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = content
    
    if not paths:
        return data, None, None
    
    # 解析指定的路径
    return parse_response(data, paths), None, None

def parse_response(data: Any, paths: Union[str, List[str]]) -> Any:
    """
    解析响应数据
    
    :param data: 要解析的数据 (通常是dict或list)
    :param paths: 单个路径字符串或路径字符串列表
    :return: 解析结果，结果类型根据路径和数据类型决定
    """
    # 核心：通过正则表达式，识别索引和切片语法
    index_pattern = re.compile(r'\[(.*?)\]')

    def resolve_path(obj: Any, parts: List[str]) -> Union[Any, List[Any]]:
        """递归解析路径：返回最自然的类型"""
        if not parts or obj is None:
            return obj
            
        current = parts[0]
        remaining = parts[1:]
        
        # 检查当前部分是否包含索引/切片语法
        match = index_pattern.search(current)
        if match:
            # 提取索引/切片表达式
            index_expr = match.group(1)
            # 获取字段名（索引前的部分）
            field = current[:match.start()].strip()
            
            # 如果字段名不为空，先访问该字段
            if field:
                if isinstance(obj, dict) and field in obj:
                    obj = obj[field]
                elif isinstance(obj, (list, tuple)) and field.isdigit():
                    obj = obj[int(field)]
            
                # 处理通配符 (*) 或索引/切片
                if index_expr == '*':
                    # 通配符处理，展开所有元素
                    if not isinstance(obj, (list, tuple)):
                        return None
                    
                    results = []
                    for item in obj:
                        result = resolve_path(item, remaining)
                        # 根据是否使用通配符决定结构
                        if '*' in current:  # 使用通配符时保持每个item的结构
                            results.append(result)
                        else:  # 非通配符情况扁平化
                            if isinstance(result, list):
                                results.extend(result)
                            else:
                                results.append(result)
                    return results
            elif ':' in index_expr:
                # 切片处理
                indices = index_expr.split(':')
                try:
                    start = int(indices[0]) if indices[0] else 0
                    end = int(indices[1]) if len(indices) > 1 and indices[1] else len(obj)
                    step = int(indices[2]) if len(indices) > 2 and indices[2] else 1
                    
                    results = []
                    for item in obj[start:end:step]:
                        result = resolve_path(item, remaining)
                        if isinstance(result, list):
                            results.extend(result)
                        else:
                            results.append(result)
                    return results
                except (ValueError, TypeError):
                    return None
            else:
                # 单个索引处理
                try:
                    idx = int(index_expr)
                    return resolve_path(obj[idx], remaining)
                except (ValueError, TypeError, IndexError):
                    return None
                
        # 处理常规路径
        if isinstance(obj, dict) and current in obj:
            return resolve_path(obj[current], remaining)
            
        # 解析为数组索引
        if isinstance(obj, (list, tuple)) and current.isdigit():
            try:
                idx = int(current)
                return resolve_path(obj[idx], remaining)
            except (ValueError, IndexError):
                return None
            
        # 分割点路径
        if '.' in current:
            sub_paths = current.split('.')
            return resolve_path(obj, sub_paths + remaining)
            
        return None
    
    # 处理单个路径或路径列表
    if isinstance(paths, str):
        # 对于单个路径，返回最自然的类型
        path_parts = [part.strip() for part in paths.split('.') if part.strip()]
        return resolve_path(data, path_parts)
    else:
        # 对于多个路径，返回结果列表
        return [resolve_path(data, [part.strip() for part in p.split('.') if part.strip()]) 
                for p in paths]