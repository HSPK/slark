from typing import Union

from slark.types._common import BaseModel
from slark.types.bitables.common import FieldPropertyType, FieldType, UIType


class FieldDescription(BaseModel):
    disable_sync: bool
    """是否禁止同步，如果为true，表示禁止同步该描述内容到表单的问题描述注意：该字段在列出字段时不生效。只在新增、修改字段时生效。"""
    text: str
    """字段描述内容"""


class Field(BaseModel):
    field_id: str
    """字段id"""

    field_name: str
    """字段名"""

    type: FieldType

    property: Union[FieldPropertyType, None] = None
    """字段属性，因字段类型而异"""

    ui_type: Union[UIType, None] = None

    description: Union[FieldDescription, None] = None
    """字段描述"""

    is_primary: Union[bool, None] = None
    """是否是索引列"""

    is_hidden: Union[bool, None] = None
    """是否是隐藏字段"""
