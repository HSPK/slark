import typing as t

from typing_extensions import Literal

from slark.types._common import BaseModel

MESSAGE_TYPE = Literal[
    "text",
    "post",
    "image",
    "file",
    "audio",
    "media",
    "sticker",
    "interactive",
    "share_card",
    "share_user",
]
"""text：文本
    post：富文本
    image：图片
    file：文件
    audio：语音
    media：视频
    sticker：表情包
    interactive：卡片
    share_card：分享群名片
    share_user：分享个人名片"""


class SendMessageParams(BaseModel):
    receive_id_type: Literal["open_id", "user_id", "email", "chat_id"]
    """用户 ID 类型

    示例值："open_id"

    可选值有：

    open_id：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。了解更多：如何获取 Open ID
    union_id：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。了解更多：如何获取 Union ID？
    user_id：标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。了解更多：如何获取 User ID？
    email：以用户的真实邮箱来标识用户。
    chat_id：以群 ID 来标识群聊。了解更多：如何获取群 ID"""


class GetMessageParams(BaseModel):
    user_id_type: Literal["open_id", "union_id", "user_id"] = "open_id"


class SendMessageBody(BaseModel):
    receive_id: str
    """消息接收者的 ID，ID 类型与查询参数 receive_id_type 的取值一致。

    注意事项：

    给用户发送消息时，用户需要在机器人的可用范围内。例如，你需要给企业全员发送消息，则需要将应用的可用范围设置为全体员工。
    给群组发送消息时，机器人需要在该群组中，且在群组内拥有发言权限。
    如果消息接收者为用户，推荐使用用户的 open_id。"""

    msg_type: MESSAGE_TYPE
    content: str
    """消息内容，JSON 结构序列化后的字符串。该参数的取值与 msg_type 对应，例如 msg_type 取值为 text，则该参数需要传入文本类型的内容。

    注意：
    JSON 字符串需进行转义。例如，换行符 \n 转义后为 \\n。
    文本消息请求体最大不能超过 150 KB。
    卡片消息、富文本消息请求体最大不能超过 30 KB。
    如果使用卡片模板（template_id）发送消息，实际大小也包含模板对应的卡片数据大小。
    如果消息中包含样式标签，会使实际消息体长度大于您输入的请求体长度。
    图片需要先上传图片，然后使用图片的 Key 发消息。
    音频、视频、文件需要先上传文件，然后使用文件的 Key 发消息。注意不能使用云文档上传素材接口返回的 file_token。
    了解不同类型的消息内容格式、使用限制，可参见发送消息内容。"""

    uuid: t.Union[str, None] = None
    """自定义设置的唯一字符串序列，用于在回复消息时请求去重。不填则表示不去重。持有相同 uuid 的请求，在 1 小时内至多成功回复一条消息。\
        注意：你可以参考示例值自定义参数值。当回复的内容不同时，如果传入了该参数，则需要在每次请求时都更换该参数的取值。\
        示例值："选填，每次调用前请更换，如a0d69e20-1dd1-458b-k525-dfeca4015204" """


class ReplyMessageBody(BaseModel):
    content: str
    msg_type: MESSAGE_TYPE
    reply_in_thread: bool = False
    """是否以话题形式回复。取值为 true 时将以话题形式回复。\
        注意：如果要回复的消息已经是话题形式的消息，则默认以话题形式进行回复。"""

    uuid: t.Union[str, None] = None
    """自定义设置的唯一字符串序列，用于在回复消息时请求去重。不填则表示不去重。持有相同 uuid 的请求，在 1 小时内至多成功回复一条消息。\
        注意：你可以参考示例值自定义参数值。当回复的内容不同时，如果传入了该参数，则需要在每次请求时都更换该参数的取值。\
        示例值："选填，每次调用前请更换，如a0d69e20-1dd1-458b-k525-dfeca4015204" """


class EditMessageBody(BaseModel):
    msg_type: Literal["text", "post"]
    content: str
