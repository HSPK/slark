from typing import List, Union

from pydantic import BaseModel

from slark.types.response import BaseResponse

from .common import BlockInfo


class GetAllBlocksResponseData(BaseModel):
    items: List[BlockInfo]
    page_token: Union[str, None] = None
    has_more: bool


class GetAllBlocksResponse(BaseResponse):
    data: GetAllBlocksResponseData
