from typing import List, Union

from pydantic import field_validator

from slark.types._common import BaseModel
from slark.types.bitables.common import FieldPropertyType, FieldType, UIType


class TableFieldDescription(BaseModel):
    disable_sync: Union[bool, None] = None
    """是否禁止同步，如果为true，表示禁止同步该描述内容到表单的问题描述

    示例值：true

    默认值：true"""

    text: Union[str, None] = None
    """字段描述内容，支持换行\n

    示例值："请按 name_id 格式填写\n例如：“Alice_20202020”"""


class TableField(BaseModel):
    field_name: str
    """字段名,示例值："文本"""
    type: FieldType
    ui_type: Union[UIType, None] = None
    property: Union[FieldPropertyType, None] = None
    description: Union[TableFieldDescription, None] = None


class TableData(BaseModel):
    name: Union[str, None] = None
    """数据表名称

    请注意：

    名称中的首尾空格将会被去除。
    示例值："table1"

    数据校验规则：

    长度范围：1 字符 ～ 100 字符"""
    default_view_name: Union[str, None] = None
    """默认表格视图的名称，不填则默认为 表格。

    请注意：

    名称中的首尾空格将会被去除。
    名称中不允许包含 [ ] 两个字符"""

    fields: Union[List[TableField]] = None
    """数据表的初始字段。

    请注意：

    如果 default_view_name 字段和 fields 字段都不填写，将会创建一个仅包含索引列的空数据表。

    如果指定了 fields 字段，将会创建一个包含初始字段的数据表且默认第一个字段为索引列。

    数据校验规则：

    长度范围：1 ～ 300"""

    @field_validator("name")
    def validate_name(cls, v: str):
        v = v.strip()
        if not v or len(v) > 100:
            raise ValueError("name length should be 1-100")
        return v

    @field_validator("default_view_name")
    def validate_default_view_name(cls, v: str):
        v = v.strip()
        if "[" in v or "]" in v:
            raise ValueError("default_view_name should not contain [ or ]")
        return v

    @field_validator("fields")
    def validate_fields(cls, v: List[TableField]):
        if v is not None and len(v) > 300:
            raise ValueError("fields length should be 1-300")
        return v
