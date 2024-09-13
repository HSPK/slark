from typing import List

from slark.types._common import BaseModel
from slark.types.response import BaseResponse

from .common import LarkGetMessage


class SendMessageResponse(BaseResponse):
    data: LarkGetMessage


class ReplyMessageResponse(BaseResponse):
    data: LarkGetMessage


class EditMessageResponse(BaseResponse):
    data: LarkGetMessage


class ForwardMessageResponse(BaseResponse):
    data: LarkGetMessage


class GetMessageData(BaseModel):
    items: List[LarkGetMessage]


class GetMessageResponse(BaseResponse):
    data: GetMessageData
