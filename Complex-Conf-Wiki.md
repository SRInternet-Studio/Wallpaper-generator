# 复杂配置

## 复杂路径规范（Beta）

> [!Note]
> 此页规范搭配包含模块 [APIKernal](https://github.com/SRInternet/APIKernal) ，并且兼容 APICORE 配置文件规范的项目使用，现已兼容 [壁纸生成器 NEXT](https://github.com/SRInternet-Studio/Wallpaper-generator/tree/NEXT-PREVIEW) 。

### 1. 核心语法元素

| 元素类型   | 语法               | 描述                     | 示例               |
|------------|--------------------|--------------------------|--------------------|
| 键名访问   | `.key`             | 访问字典键               | ```users.name```       |
| 通配符     | `[*]`             | 遍历数组所有元素         | ```items[*].id```      |
| 索引       | `[n]`             | 访问数组特定索引的元素   | ```posts[0].title```   |
| 切片       | `[start:end:step]`| 访问数组切片             | ```products[0:3]```    |

---

### 2. 基础场景案例

#### 2.1 单值访问
```python
路径: "user.address.city"
数据: {
    "user": {
        "address": {
            "city": "Beijing"
        }
    }
}
结果: "Beijing"
类型: str
```

#### 2.2 数组通配符
```python
路径: "students[*].grade"
数据: {
    "students": [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92}
    ]
}
结果: [85, 92]
类型: list
```

#### 2.3 数组索引访问
```python
路径: "products[1].price"
数据: {
    "products": [
        {"name": "Pencil", "price": 1.99},
        {"name": "Notebook", "price": 5.99},
        {"name": "Eraser", "price": 0.99}
    ]
}
结果: 5.99
类型: float
```

#### 2.4 数组切片访问
```python
路径: "items[0:2].status"
数据: {
    "items": [
        {"id": 101, "status": "active"},
        {"id": 102, "status": "completed"},
        {"id": 103, "status": "pending"}
    ]
}
结果: ["active", "completed"]
类型: list
```

---

### 3. 复合路径案例

#### 3.1 嵌套对象访问
```python
路径: "company.departments.hr.manager.email"
数据: {
    "company": {
        "departments": {
            "hr": {
                "manager": {
                    "name": "Sarah",
                    "email": "sarah@company.com"
                }
            }
        }
    }
}
结果: "sarah@company.com"
类型: str
```

#### 3.2 对象中的数组通配符
```python
路径: "orders[*].order_id"
数据: {
    "orders": [
        {"order_id": "A1001", "total": 49.99},
        {"order_id": "A1002", "total": 29.99},
        {"order_id": "A1003", "total": 99.99}
    ]
}
结果: ["A1001", "A1002", "A1003"]
类型: list
```

#### 3.3 数组中的对象访问
```python
路径: "employees[0].contact.phone"
数据: {
    "employees": [
        {
            "name": "John",
            "contact": {
                "email": "john@company.com",
                "phone": "123-4567"
            }
        },
        {
            "name": "Emma",
            "contact": {
                "phone": "987-6543"
            }
        }
    ]
}
结果: "123-4567"
类型: str
```

#### 3.4 多级通配符组合
```python
路径: "school.classes[*].students[*].final_score"
数据: {
    "school": {
        "classes": [
            {
                "class_name": "Math",
                "students": [
                    {"name": "Tom", "final_score": 92},
                    {"name": "Lily", "final_score": 85}
                ]
            },
            {
                "class_name": "Science",
                "students": [
                    {"name": "Sam", "final_score": 78}
                ]
            }
        ]
    }
}
结果: [92, 85, 78]
类型: list
```

---

### 4. 特殊场景处理

#### 4.1 空数组处理
```python
路径: "empty_list[*].name"
数据: {"empty_list": []}
结果: []
类型: list
```

#### 4.2 路径不存在
```python
路径: "user.address.zip_code"
数据: {"user": {"name": "Alice"}}
结果: None
类型: NoneType
```

#### 4.3 类型不匹配
```python
路径: "products.name[0]"
数据: {
    "products": {
        "name": "Laptop"
    }
}
结果: None
类型: NoneType
```

#### 4.4 索引越界
```python
路径: "orders[5].total"
数据: {
    "orders": [
        {"order_id": "A1001", "total": 49.99}
    ]
}
结果: None
类型: NoneType
```

#### 4.5 切片边界处理
```python
路径: "items[5:10].id"
数据: {
    "items": [
        {"id": 1}, {"id": 2}, {"id": 3},
        {"id": 4}, {"id": 5}, {"id": 6}
    ]
}
结果: [6]
类型: list
```

---

### 5. 返回值规则总结

| 场景描述 | 返回类型 | 示例 |
|----------|----------|------|
| 单个键名访问成功 | 具体值类型 | ```user.age → 25``` |
| 单个索引访问成功 | 具体值类型 | ```posts[0] → {id: 101}``` |
| 通配符访问数组 | list | ```items[*].id → [101,102]``` |
| 切片访问数组 | list | ```posts[0:2] → [{id:101}, {id:102}]``` |
| 组合路径无通配符 | 具体值类型 | ```data.products[0].price → 19.99``` |
| 组合路径有通配符 | list | ```data[*].products[0].price → [19.99, 24.99]``` |
| 路径不可访问 | None | ```non.existent.path → None``` |

---

### 6. 实用技巧

#### 6.1 深度嵌套访问
```python
路径: "response.data.images[0].sizes.original.url"
数据: {
    "response": {
        "data": {
            "images": [
                {
                    "id": "IMG001",
                    "sizes": {
                        "thumbnail": "url_thumb.jpg",
                        "original": {
                            "url": "url_full.jpg",
                            "width": 1920
                        }
                    }
                }
            ]
        }
    }
}
结果: "url_full.jpg"
```

#### 6.2 多层通配符过滤
```python
路径: "users[*].posts[0:3].comments[:2].author"
数据: {
    "users": [
        {
            "name": "Alice",
            "posts": [
                {
                    "title": "Post1",
                    "comments": [
                        {"text": "Great!", "author": "UserA"},
                        {"text": "Nice", "author": "UserB"}
                    ]
                },
                {
                    "title": "Post2",
                    "comments": [
                        {"text": "Awesome", "author": "UserC"}
                    ]
                }
            ]
        }
    ]
}
结果: [["UserA", "UserB"], ["UserC"]]
```

#### 6.3 使用步长提取数据
```python
路径: "sensors.hourly[::2].temperature"
数据: {
    "sensors": {
        "hourly": [
            {"time": "00:00", "temperature": 22.1},
            {"time": "01:00", "temperature": 21.8},
            {"time": "02:00", "temperature": 20.5},
            {"time": "03:00", "temperature": 19.2}
        ]
    }
}
结果: [22.1, 20.5]
```

#### 6.4 边界切片处理
```python
路径: "transactions[-3:].amount"
数据: {
    "transactions": [
        {"id": "T001", "amount": 50.0},
        {"id": "T002", "amount": 30.0},
        {"id": "T003", "amount": 20.0},
        {"id": "T004", "amount": 60.0}
    ]
}
结果: [30.0, 20.0, 60.0]
```

---

### 7. 常见问题排查

#### 7.1 为什么返回结果是None？
- 路径中的键名拼写错误
- 路径访问了不存在的索引
- 类型不匹配（如在字典上使用索引）

#### 7.2 为什么返回空列表？
- 使用通配符访问空数组
- 切片范围超出实际数据边界

#### 7.3 如何避免错误？
- 先访问API获取原始数据验证结构
- 从简单路径开始逐步构建复杂路径
- 使用简单的示例数据进行测试