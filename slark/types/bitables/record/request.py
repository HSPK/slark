from typing import Dict, List, Union

from typing_extensions import Literal

from slark.types._common import BaseModel

from .common import FieldValueType


class CreateRecordParams(BaseModel):
    user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None
    client_token: Union[str, None] = None
    """格式为标准的 uuidv4，操作的唯一标识，用于幂等的进行更新操作。此值为空表示将发起一次新的请求，此值非空表示幂等的进行更新操作。

    示例值："fe599b60-450f-46ff-b2ef-9f6675625b97"""


class CreateRecordBody(BaseModel):
    """用于创建多维表格记录的请求体
    Example:
    ```
    {
        "fields": {
            "多行文本": "多行文本内容",
            "条码": "+$$3170930509104X512356",
            "数字": 100,
            "货币": 3,
            "评分": 3,
            "进度": 0.25,
            "单选": "选项1",
            "多选": ["选项1", "选项2"],
            "日期": 1674206443000,
            "复选框": true,
            "人员": [
                {"id": "ou_2910013f1e6456f16a0ce75ede950a0a"},
                {"id": "ou_e04138c9633dd0d2ea166d79f548ab5d"},
            ],
            "群组": [{"id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"}],
            "电话号码": "13026162666",
            "超链接": {"text": "飞书多维表格官网", "link": "https://www.feishu.cn/product/base"},
            "附件": [
                {"file_token": "DRiFbwaKsoZaLax4WKZbEGCccoe"},
                {"file_token": "BZk3bL1Enoy4pzxaPL9bNeKqcLe"},
                {"file_token": "EmL4bhjFFovrt9xZgaSbjJk9c1b"},
                {"file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"},
            ],
            "单向关联": ["recHTLvO7x", "recbS8zb2m"],
            "双向关联": ["recHTLvO7x", "recbS8zb2m"],
            "地理位置": "116.397755,39.903179",
        }
    }
    ```
    """

    fields: Dict[str, FieldValueType]


class UpdateRecordParams(BaseModel):
    user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None


class UpdateRecordBody(BaseModel):
    fields: Dict[str, FieldValueType]


class SearchRecordParams(BaseModel):
    user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None
    """用户 ID 类型

    示例值："open_id"

    可选值有：

    open_id：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。了解更多：如何获取 Open ID
    union_id：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。了解更多：如何获取 Union ID？
    user_id：标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。了解更多：如何获取 User ID？
    默认值：open_id

    当值为 user_id，字段权限要求：

    获取用户 user ID
    仅自建应用"""

    page_token: Union[str, None] = None
    """分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果

    示例值："eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0="."""

    page_size: Union[int, None] = None
    """分页大小。最大值为 500

    示例值：10

    默认值：20"""


class SearchRecordSort(BaseModel):
    field_name: str
    """字段名称

    示例值："多行文本"

    数据校验规则：

    长度范围：0 字符 ～ 1000 字符"""

    desc: Union[bool, None] = None
    """是否倒序排序

    示例值：true

    默认值：false"""


class SearchRecordFilterCondition(BaseModel):
    field_name: str
    """筛选条件的左值，值为字段的名称

    示例值："字段1"

    数据校验规则：

    长度范围：0 字符 ～ 1000 字符"""

    operator: Literal[
        "is",
        "isNot",
        "contains",
        "doesNotContain",
        "isEmpty",
        "isNotEmpty",
        "isGreater",
        "isGreaterEqual",
        "isLess",
        "isLessEqual",
        "like",
        "in",
    ]
    """条件运算符

    示例值："is"

    可选值有：

    is：等于
    isNot：不等于
    contains：包含
    doesNotContain：不包含
    isEmpty：为空
    isNotEmpty：不为空
    isGreater：大于
    isGreaterEqual：大于等于
    isLess：小于
    isLessEqual：小于等于
    like：LIKE 运算符。暂未支持
    in：IN 运算符。暂未支持"""

    value: List[str]
    """目标值

    [目标值填写指南](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide)

    示例值：["文本内容"]

    数据校验规则：

    长度范围：0 ～ 10"""


class SearchRecordFilter(BaseModel):
    conjunction: Union[Literal["and", "or"], None] = None
    """条件逻辑连接词

    示例值："and"

    可选值有：

    and：满足全部条件
    or：满足任一条件
    数据校验规则：

    长度范围：0 字符 ～ 10 字符"""
    conditions: List[SearchRecordFilterCondition]


class SearchRecordBody(BaseModel):
    """用于搜索多维表格记录的请求体
        Example:
        ```
        {
        "view_id":"vewqhz51lk",
        "field_names":[
            "字段1",
            "字段2"
        ],
        "sort":[
            {
                "field_name":"多行文本",
                "desc":true
            }
        ],
        "filter":{
            "conjunction":"and",
            "conditions":[
                {
                    "field_name":"字段1",
                    "operator":"is",
                    "value":[
                        "文本内容"
                    ]
                }
            ]
        },
        "automatic_fields":false
    }```"""

    view_id: Union[str, None] = None
    """视图的唯一标识符，获取指定视图下的记录view_id 参数说明

    注意：当 filter 参数 或 sort 参数不为空时，请求视为对数据表中的全部数据做条件过滤，指定的view_id 会被忽略。

    示例值："vewqhz51lk"

    数据校验规则：

    长度范围：0 字符 ～ 50 字符"""

    field_names: Union[List[str], None] = None
    """字段名称，用于指定本次查询返回记录中包含的字段

    示例值：["字段1","字段2"]

    数据校验规则：

    长度范围：0 ～ 200"""

    sort: Union[List[SearchRecordSort], None] = None
    """排序条件

    数据校验规则：

    长度范围：0 ～ 100"""

    filter: Union[SearchRecordFilter, None] = None
    """筛选条件"""

    automatic_fields: Union[bool, None] = None
    """控制是否返回自动计算的字段, true 表示返回

    示例值：false"""


class BatchCreateRecordBody(BaseModel):
    records: List[CreateRecordBody]


class BatchUpdateRecord(BaseModel):
    record_id: str
    """一条记录的唯一标识 ID。参考record_id 参数说明 获取 record_id。该参数必填，请忽略左侧必填列的否

    示例值："recqwIwhc6"."""

    fields: Dict[str, FieldValueType]
    """数据表的字段，即数据表的列

    当前接口支持的字段类型请参考接入指南

    不同类型字段的数据结构请参考数据结构概述

    示例值：{"多行文本":"HelloWorld"}"""


class BatchUpdateRecordBody(BaseModel):
    """用于批量更新多维表格记录的请求体
        Example:
        ```{
        "records": [
            {
                "record_id": "reclAqylTN",
                "fields": {
                    "索引": "索引列多行文本类型",
                    "多行文本": "多行文本内容",
                    "数字": 100,
                    "单选": "选项3",
                    "多选": [
                        "选项1",
                        "选项2"
                    ],
                    "日期": 1674206443000,
                    "条码": "qawqe",
                    "复选框": true,
                    "人员": [
                        {
                            "id": "ou_2910013f1e6456f16a0ce75ede950a0a"
                        },
                        {
                            "id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
                        }
                    ],
                    "群组": [
                        {
                            "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
                        }
                    ],
                    "电话号码": "13026162666",
                    "超链接": {
                        "text": "飞书多维表格官网",
                        "link": "https://www.feishu.cn/product/base"
                    },
                    "附件": [
                        {
                            "file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
                        }
                    ],
                    "单向关联": [
                        "recHTLvO7x",
                        "recbS8zb2m"
                    ],
                    "双向关联": [
                        "recHTLvO7x",
                        "recbS8zb2m"
                    ],
                    "地理位置": "116.397755,39.903179",
                    "评分": 3,
                    "货币": 3,
                    "进度": 0.25
                }
            }
        ]
    }```"""

    records: List[BatchUpdateRecord]


class BatchGetRecordBody(BaseModel):
    """用于批量获取多维表格记录的请求体
    Example:
    ```
    {
        "record_ids": ["recyOaMB2F", "rec111111", "recyOaMB2F"],
        "user_id_type": "open_id",
        "with_shared_url": true,
        "automatic_fields": true,
    }```
    """

    record_ids: List[str]
    """记录 ID 列表。调用列出记录获取。

    示例值：["recyO3299N"]

    数据校验规则：

    长度范围：1 ～ 100"""

    user_id_type: Union[str, None] = None
    """此次调用中使用的用户 id 的类型

    示例值："open_id"

    可选值有：

    user_id：以user_id来识别用户
    union_id：以union_id来识别用户
    open_id：以open_id来识别用户"""

    with_shared_url: Union[bool, None] = None
    """是否返回记录的分享链接。可选值：

    true：返回分享链接
    false：不返回分享链接
    默认值：false

    示例值：true"""

    automatic_fields: Union[bool, None] = None
    """是否返回自动计算的字段。可选值：

    true：返回自动计算的字段
    false：不返回自动计算的字段
    默认值：false

    示例值：true"""


class BatchDeleteRecordBody(BaseModel):
    records: List[str]
    """待删除的记录的id

    示例值：["recyO3299N"]"""
