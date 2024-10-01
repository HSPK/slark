from typing import Union

from typing_extensions import Literal

from ..base import BaseElement, BaseModel
from ..icon import IconElement
from ..text import TextSize


class MDHrefUrlVal(BaseModel):
    url: str
    pc_url: Union[str, None] = None
    android_url: Union[str, None] = None
    ios_url: Union[str, None] = None


class MDHref(BaseModel):
    urlVal: MDHrefUrlVal


class MDElement(BaseElement):
    tag: str = "markdown"
    content: str
    text_align: Literal["left", "center", "right"] = "left"
    """设置文本内容的对齐方式。可取值有：

    left：左对齐
    center：居中对齐
    right：右对齐"""

    text_size: Union[TextSize, str, None] = TextSize.NORMAL.value
    icon: Union[IconElement, None] = None
    href: Union[MDHref, None] = None