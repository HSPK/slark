import enum
import hashlib
import json
import typing as t

from fastapi import Request
from typing_extensions import Literal

from slark.types._common import BaseModel


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


class LarkUserID(BaseModel):
    union_id: str
    user_id: str
    open_id: str


class LarkEventSender(BaseModel):
    sender_id: LarkUserID
    sender_type: str
    tenant_key: str
    """tenant key，为租户在飞书上的唯一标识，用来换取对应的tenant_access_token，也可以用作租户在应用里面的唯一标识"""


class LarkMessageMention(BaseModel):
    key: str
    id: LarkUserID
    name: str
    tenant_key: str


class TextContent(BaseModel):
    text: str


class FileContent(BaseModel):
    file_key: str
    file_name: str


class AudioContent(BaseModel):
    file_key: str
    duration: int


class MediaContent(BaseModel):
    file_key: str
    image_key: str
    file_name: str
    duration: int


class StickerContent(BaseModel):
    file_key: str


class RichTextItem(BaseModel):
    tag: Literal["text", "a", "at", "img", "file", "media", "emotion", "hr", "code_block"]
    text: str | None = None
    style: list[str] | None = None
    href: str | None = None
    user_id: str | None = None
    user_name: str | None = None
    image_key: str | None = None
    file_key: str | None = None
    language: str | None = None
    un_escape: bool | None = None
    emoji_type: str | None = None
    duration: int | None = None


class RichTextContent(BaseModel):
    title: str
    content: list[list[RichTextItem]]

    def get_raw_text(self):
        raw_text = ""
        for line in self.content:
            for item in line:
                if item.tag == "text":
                    raw_text += item.text
                elif item.tag == "a":
                    raw_text += item.text
                elif item.tag == "at":
                    raw_text += f"@{item.user_name}"
                elif item.tag == "hr":
                    raw_text += "----"
                elif item.tag == "code_block":
                    raw_text += f"```{item.language}\n{item.text}\n```"
            raw_text += "\n"
        return raw_text


LARK_MSG_TYPE = Literal["text", "post", "file", "folder", "audio", "media", "sticker"] | str

LARK_MSG_TYPE_MAP = {
    "text": TextContent,
    "file": FileContent,
    "audio": AudioContent,
    "media": MediaContent,
    "sticker": StickerContent,
    "post": RichTextContent,
}


class LarkGetMessageSender(BaseModel):
    id: str
    id_type: str
    sender_type: str
    tenant_key: str


class LarkGetMessageBody(BaseModel):
    content: (
        str
        | TextContent
        | RichTextContent
        | FileContent
        | AudioContent
        | MediaContent
        | StickerContent
    )


class LarkGetMessageMention(BaseModel):
    key: str
    id: str
    id_type: str
    name: str
    tenant_key: str


class LarkGetMessage(BaseModel):
    message_id: str
    root_id: str | None = None
    parent_id: str | None = None
    thread_id: str | None = None
    msg_type: LARK_MSG_TYPE
    create_time: str
    update_time: str
    deleted: bool
    updated: bool
    chat_id: str | None = None
    sender: LarkGetMessageSender
    body: LarkGetMessageBody
    mentions: list[LarkGetMessageMention] | None = None
    upper_message_id: str | None = None

    def model_post_init(self, __context) -> None:
        if self.msg_type in LARK_MSG_TYPE_MAP:
            self.body.content = LARK_MSG_TYPE_MAP[self.msg_type].model_validate_json(
                self.body.content
            )
        else:
            self.body.content = json.loads(self.body.content)

    def get_plain_text(self):
        if self.msg_type == "text":
            return self.body.content.text
        elif self.msg_type == "post":
            return self.body.content.get_raw_text()
        else:
            return "Unsupported message type"


class LarkEventMessageBody(BaseModel):
    message_id: str
    """message_id 是一条消息的唯一标识。当发送一条消息时，系统会自动生成唯一ID。message_id 的格式是以om_ 开头的字符串，例如：om_934be5776f5a87239a298af9e74c0f72"""
    root_id: str | None = None
    parent_id: str | None = None
    create_time: str
    update_time: str
    chat_id: str | None = None
    """消息所在的群组 ID"""
    thread_id: str | None = None
    """消息所属的话题 ID（不返回说明该消息非话题消息），说明参见：话题介绍"""
    chat_type: Literal["p2p", "group"]
    message_type: LARK_MSG_TYPE
    content: (
        str
        | TextContent
        | RichTextContent
        | FileContent
        | AudioContent
        | MediaContent
        | StickerContent
    )
    mentions: list[LarkMessageMention] | None = None
    user_agent: str | None = None
    """用户代理数据，仅在接收事件的机器人具备获取客户端用户代理信息权限时返回"""

    def model_post_init(self, __context) -> None:
        if self.message_type in LARK_MSG_TYPE_MAP:
            self.content = LARK_MSG_TYPE_MAP[self.message_type].model_validate_json(self.content)
        else:
            self.content = json.loads(self.content)

    def get_plain_text(self):
        if self.message_type == "text":
            return self.content.text
        elif self.message_type == "post":
            return self.content.get_raw_text()
        else:
            return "Unsupported message type"


class LarkEventBody(BaseModel):
    sender: LarkEventSender
    message: LarkEventMessageBody


class UploadMessage(BaseModel):
    file_name: str
    n_updated: int
    message: str


class UploadFile(BaseModel):
    file_name: str
    saved_file_path: str
    file_size: int


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
