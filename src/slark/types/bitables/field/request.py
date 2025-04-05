from typing import Union

from slark.types._common import BaseModel

from ..common import FieldType, UIType
from .common import FieldDescription, FieldPropertyType


class ListFieldParams(BaseModel):
    view_id: Union[str, None] = None
    """视图 ID

    示例值："vewOVMEXPF"
    """

    text_field_as_array: Union[bool, None] = None
    """控制字段描述（多行文本格式）数据的返回格式, true 表示以数组富文本形式返回

    示例值：true"""

    page_token: Union[str, None] = None
    """分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果

    示例值："fldwJ4YrtB"
    """

    page_size: Union[int, None] = None
    """	
    分页大小

    示例值：10

    默认值：20

    数据校验规则：

    最大值：100"""


class CreateFieldParams(BaseModel):
    client_token: Union[str, None] = None
    """格式为标准的 uuidv4，操作的唯一标识，用于幂等的进行更新操作。此值为空表示将发起一次新的请求，此值非空表示幂等的进行更新操作。\
        示例值："fe599b60-450f-46ff-b2ef-9f6675625b97"。"""


class CreateFieldBody(BaseModel):
    field_name: str
    """多维表格字段名

    请注意：

    名称中的首尾空格将会被去除。
    示例值："多行文本"
    """
    type: FieldType
    property: Union[FieldPropertyType, None] = None
    """字段属性，因字段类型而异"""
    ui_type: UIType
    description: Union[FieldDescription, None] = None
    """字段描述"""


class UpdateFieldBody(CreateFieldBody):
    pass
