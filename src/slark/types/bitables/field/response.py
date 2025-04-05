from typing import List, Union

from slark.types._common import BaseModel
from slark.types.response import BaseResponse

from .common import Field


class ListFieldResponseData(BaseModel):
    has_more: bool
    """是否还有更多项"""
    page_token: Union[str, None] = None
    """分页标记，当 has_more 为 true 时，会同时返回新的 page_token，否则不返回 page_token"""
    total: int
    """总数"""
    items: List[Field]
    """字段信息"""


class ListFieldResponse(BaseResponse):
    data: ListFieldResponseData


class CreateFieldResponseData(BaseModel):
    field: Field


class CreateFieldResponse(BaseResponse):
    data: CreateFieldResponseData


class UpdateFieldResponse(BaseResponse):
    data: CreateFieldResponseData


class DeleteFieldResponseData(BaseModel):
    field_id: str
    """field id"""
    deleted: bool
    """删除标记"""


class DeleteFieldResponse(BaseResponse):
    data: DeleteFieldResponseData
