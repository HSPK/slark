from typing import Union

from typing_extensions import Literal

from ..base import BaseElement
from ..color import Color
from ..icon import IconElement
from ..text import TextSize


class PlainTextElement(BaseElement):
    tag: Literal["plain_text", "lark_md"] = "plain_text"
    """文本类型的标签。可取值：

    plain_text：普通文本内容
    lark_md：支持部分 Markdown 语法的文本内容。详情参考下文 lark_md 支持的 Markdown 语法
    注意：飞书卡片搭建工具中仅支持使用 plain_text 类型的普通文本组件。你可使用富文本组件添加 Markdown 格式的文本。"""

    content: str
    """文本内容。当 tag 为 lark_md 时，支持部分 Markdown 语法的文本内容。详情参考下文 lark_md 支持的 Markdown 语法。
    https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-components/content-components/plain-text#39ee4e65"""

    text_size: Union[TextSize, str, None] = TextSize.NORMAL.value
    """文本大小。可取值如下所示。如果你填写了其它值，卡片将展示为 normal 字段对应的字号。你也可分别为移动端和桌面端定义不同的字号，详细步骤参考下文 为移动端和桌面端定义不同的字号。"""
    text_align: Literal["left", "center", "right"] = "left"
    """文本对齐方式。可取值：

    left：左对齐
    center：居中对齐
    right：右对齐"""

    text_color: Union[str, Color] = "default"
    """文本的颜色。仅在 tag 为 plain_text 时生效。可取值：

    default：客户端浅色主题模式下为黑色；客户端深色主题模式下为白色"""

    lines: Union[int, None] = None
    """内容最大显示行数，超出设置行的内容用 ... 省略。"""

class DivElement(BaseElement):
    tag: str = "div"
    text: PlainTextElement
    icon: Union[IconElement, None] = None