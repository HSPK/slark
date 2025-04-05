from typing import Union

from pydantic import BaseModel, ConfigDict
from typing_extensions import Literal


class SegmentStyle(BaseModel):
    bold: bool = False
    italic: bool = False
    strikeThrough: bool = False
    underline: bool = False
    foreColor: str = "#000000"
    fontSize: int = 10


class BaseCell(BaseModel):
    type: str
    text: str
    segment_style: Union[SegmentStyle, None] = None

    model_config = ConfigDict(extra="allow")


class LinkWithText(BaseCell):
    link: str
    type: str = "url"


class Mention(BaseCell):
    """只支持@同租户的用户;单次请求最多支持同时@50人；
    notify:是否发送飞书消息，没有阅读权限的用户不会收到飞书消息；

    grantReadPermission:是否赋予该用户阅读权限（仅在独立表格中支持该字段）；仅当拥有文档分享权限时可用；

    textType:指定text字段的传入的内容，可选email，openId，unionId；

    text:需要@的人的信息，由textType指定"""

    type: str = "mention"
    text_type: str
    notify: bool = True
    grantReadPermission: bool = True


class Formula(BaseCell):
    """text字段为对应的公式，暂不支持跨表引用公式（IMPORTRANGE）"""

    type: str = "formula"


class MentionDocument(BaseCell):
    """textType:固定为fileToken

    text:文档token

    objType:文档类型，可选sheet,doc,slide,bitable,mindnote"""

    type: str = "mention"
    textType: str = "fileToken"
    objType: Literal["sheet", "doc", "slide", "bitable", "mindnote"]


CellTypes = Union[None, str, int, float, bool, LinkWithText, Mention, Formula, MentionDocument]
