import json
from typing import List, Union

from typing_extensions import Literal

from slark.types._common import BaseModel


class LarkUserID(BaseModel):
    union_id: str
    user_id: str
    open_id: str


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
    text: Union[str, None] = None
    style: Union[List[str], None] = None
    href: Union[str, None] = None
    user_id: Union[str, None] = None
    user_name: Union[str, None] = None
    image_key: Union[str, None] = None
    file_key: Union[str, None] = None
    language: Union[str, None] = None
    un_escape: Union[bool, None] = None
    emoji_type: Union[str, None] = None
    duration: Union[int, None] = None


class RichTextContent(BaseModel):
    title: str
    content: List[List[RichTextItem]]

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


class ImageContent(BaseModel):
    image_key: str


LARK_MSG_TYPE = Union[
    Literal["text", "post", "file", "folder", "image", "audio", "media", "sticker"], str
]

LARK_MSG_TYPE_MAP = {
    "text": TextContent,
    "file": FileContent,
    "audio": AudioContent,
    "media": MediaContent,
    "sticker": StickerContent,
    "post": RichTextContent,
    "image": ImageContent,
}


class LarkGetMessageSender(BaseModel):
    id: str
    id_type: str
    sender_type: str
    tenant_key: str


class LarkGetMessageBody(BaseModel):
    content: Union[
        str,
        TextContent,
        RichTextContent,
        FileContent,
        AudioContent,
        MediaContent,
        StickerContent,
        ImageContent,
    ]


class LarkGetMessageMention(BaseModel):
    key: str
    id: str
    id_type: str
    name: str
    tenant_key: str


class LarkGetMessage(BaseModel):
    message_id: str
    root_id: Union[str, None] = None
    parent_id: Union[str, None] = None
    thread_id: Union[str, None] = None
    msg_type: LARK_MSG_TYPE
    create_time: str
    update_time: str
    deleted: bool
    updated: bool
    chat_id: Union[str, None] = None
    sender: LarkGetMessageSender
    body: LarkGetMessageBody
    mentions: Union[List[LarkGetMessageMention], None] = None
    upper_message_id: Union[str, None] = None

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
    root_id: Union[str, None] = None
    parent_id: Union[str, None] = None
    create_time: str
    update_time: str
    chat_id: Union[str, None] = None
    """消息所在的群组 ID"""
    thread_id: Union[str, None] = None
    """消息所属的话题 ID（不返回说明该消息非话题消息），说明参见：话题介绍"""
    chat_type: Literal["p2p", "group"]
    message_type: LARK_MSG_TYPE
    content: Union[
        str,
        TextContent,
        RichTextContent,
        FileContent,
        AudioContent,
        MediaContent,
        StickerContent,
        ImageContent,
    ]
    mentions: Union[List[LarkMessageMention], None] = None
    user_agent: Union[str, None] = None
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
