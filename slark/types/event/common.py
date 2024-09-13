import enum
import hashlib

from fastapi import Request
from typing_extensions import Literal

from slark.types._common import BaseModel
from slark.types.messages.common import LarkEventMessageBody, LarkUserID


class EventType(enum.Enum):
    IM_MESSAGE_RECEIVE_V1 = "im.message.receive_v1"
    """机器人接收到用户发送的消息后触发此事件。"""
    IM_MESSAGE_MESSAGE_READ_V1 = "im.message.message_read_v1"
    """用户阅读机器人发送的单聊消息后触发此事件。"""
    IM_MESSAGE_RECALLED_V1 = "im.message.recalled_v1"
    """机器人所在会话内的消息被撤回时触发此事件。"""
    IM_MESSAGE_REACTION_CREATED_V1 = "im.message.reaction.created_v1"
    """应用订阅该事件后，消息被添加表情回复时会触发此事件。事件体包含被添加表情回复的消息 message_id、添加表情回复的操作人 ID、表情类型、添加时间等信息。"""
    IM_MESSAGE_REACTION_DELETED_V1 = "im.message.reaction.deleted_v1"
    """应用订阅该事件后，消息被删除表情回复时会触发此事件。事件体包含被删除表情回复的消息 message_id、删除表情回复的操作人 ID、表情类型、添加时间等信息。"""
    IM_CHAT_DISBANDED_V1 = "im.chat.disbanded_v1"
    """群组被解散后触发此事件。"""
    IM_CHAT_UPDATED_V1 = "im.chat.updated_v1"
    """群组配置被修改后触发此事件，包含：群主转移
    群基本信息修改(群头像/群名称/群描述/群国际化名称)
    群权限修改(加人入群权限/群编辑权限/at所有人权限/群分享权限等)
    用户进群"""

    IM_CHAT_MEMBER_USER_ADDED_V1 = "im.chat.member.user.added_v1"
    """新用户进群（包含话题群）触发此事件。"""
    IM_CHAT_MEMBER_USER_DELETED_V1 = "im.chat.member.user.deleted_v1"
    """用户主动退群或被移出群聊时推送事件。"""
    IM_CHAT_MEMBER_USER_WITHDRAWN_V1 = "im.chat.member.user.withdrawn_v1"
    """撤销拉用户进群后触发此事件。"""
    IM_CHAT_MEMBER_BOT_ADDED_V1 = "im.chat.member.bot.added_v1"
    """机器人被用户添加至群聊时触发此事件。"""
    IM_CHAT_MEMBER_BOT_DELETED_V1 = "im.chat.member.bot.deleted_v1"
    """机器人被移出群聊后触发此事件。"""
    P2P_CHAT_CREATE = "p2p_chat_create"
    """首次会话是用户了解应用的重要机会，你可以发送操作说明、配置地址来指导用户开始使用你的应用。"""
    IM_CHAT_ACCESS_EVENT_BOT_P2P_CHAT_ENTERED_V1 = "im.chat.access_event.bot_p2p_chat_entered_v1"
    """用户进入与机器人的会话时触发此事件"""


class LarkEventHeader(BaseModel):
    event_id: str
    event_type: EventType
    create_time: str
    token: str
    app_id: str
    tenant_key: str


class LarkEventSender(BaseModel):
    sender_id: LarkUserID
    sender_type: str
    tenant_key: str
    """tenant key，为租户在飞书上的唯一标识，用来换取对应的tenant_access_token，也可以用作租户在应用里面的唯一标识"""


class LarkEventBody(BaseModel):
    sender: LarkEventSender
    message: LarkEventMessageBody


class InvalidEventException(Exception):
    def __init__(self, error_info):
        self.error_info = error_info

    def __str__(self) -> str:
        return "Invalid event: {}".format(self.error_info)

    __repr__ = __str__


class LarkEvent(BaseModel):
    schema: Literal["2.0"]
    header: LarkEventHeader
    event: LarkEventBody

    def _validate(self, request: Request, token: str, encrypt_key: str):
        if self.header.token != token:
            raise InvalidEventException("Invalid token")
        timestamp = request.headers.get("X-Lark-Request-Timestamp")
        nonce = request.headers.get("X-Lark-Request-Nonce")
        signature = request.headers.get("X-Lark-Signature")
        body = request._body
        bytes_b1 = (timestamp + nonce + encrypt_key).encode("utf-8")
        bytes_b = bytes_b1 + body
        h = hashlib.sha256(bytes_b)
        if signature != h.hexdigest():
            raise InvalidEventException("invalid signature in event")
