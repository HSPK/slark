from typing import List, Union

from slark.types._common import BaseModel
from slark.types.response import BaseResponse


class CreateTableResponseData(BaseModel):
    table_id: str
    """多维表格数据表的唯一标识符"""
    default_view_id: Union[str, None] = None
    """默认表格视图的id，该字段仅在请求参数中填写了default_view_name或fields才会返回"""
    field_id_list: Union[List[str], None] = None
    """数据表初始字段的id列表，该字段仅在请求参数中填写了fields才会返回"""


class ListTableItem(BaseModel):
    table_id: str
    """多维表格数据表的唯一标识符"""
    revision: int
    """数据表的版本号"""
    name: str
    """数据表的名称"""


class ListTableResponseData(BaseModel):
    has_more: bool
    """是否还有更多项"""
    page_token: Union[str, None] = None
    """分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token"""
    total: int
    """总数"""
    items: List[ListTableItem]
    """数据表信息"""


class ListTableResponse(BaseResponse):
    data: ListTableResponseData


class CreateTableResponse(BaseResponse):
    data: CreateTableResponseData


class BatchCreateTableResponseData(BaseModel):
    table_ids: List[str]


class BatchCreateTableResponse(BaseResponse):
    data: BatchCreateTableResponseData


class UpdateTableResponseData(BaseModel):
    name: str
    """数据表的名称"""


class UpdateTableResponse(BaseResponse):
    data: UpdateTableResponseData
