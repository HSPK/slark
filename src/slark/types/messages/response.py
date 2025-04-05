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
    """消息内容。注意：如果查询的消息类型为合并转发（merge_forward），则返回的 items 中会包含 1 条合并转发消息和 N 条子消息。"""


class GetMessageResponse(BaseResponse):
    data: GetMessageData
