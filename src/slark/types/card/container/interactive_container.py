from typing import List, Literal, Union

from typing_extensions import TYPE_CHECKING

from ..base import BaseElement
from ..behavior import BehaviorType
from ..color import Color
from ..confirm import ConfirmDialogue
from ..displaying.image import ImageElement
from ..displaying.markdown import MDElement
from ..displaying.note import NoteElement
from ..displaying.plain_text import DivElement
from ..interactive.checker import CheckerElement
from ..text import PlainText

if TYPE_CHECKING:
    from .column import ColumnSetElement


InteractiveContainerElementType = Union[
    DivElement,
    MDElement,
    ImageElement,
    NoteElement,
    "ColumnSetElement",
    CheckerElement,
    "InteractiveContainerElement",
]


class InteractiveContainerElement(BaseElement):
    tag: str = "interactive_container"
    width: Union[str, Literal["full", "auto"], None] = None
    """交互容器的宽度。可取值：

    fill：卡片最大支持宽度
    auto：自适应宽度
    [16,999]px：自定义宽度，如 "20px"。最小宽度为 16px"""

    height: Union[str, Literal["auto"], None] = None
    """交互容器的高度。可取值：

    auto：自适应高度
    [10,999]px：自定义高度，如 "20px"""

    background_style: Union[Literal["default", "laser"], Color, None] = None
    """交互容器的背景色样式。可取值：

    default：默认的白底样式，客户端深色主题下为黑底
    laser：镭射渐变彩色样式
    卡片支持的颜色枚举值和 RGBA 语法自定义颜色。参考颜色枚举值"""

    has_border: Union[bool, None] = None
    """是否展示边框，粗细固定为 1px。"""

    border_color: Union[Color, None] = None
    """边框的颜色，仅 has_border 为 true 时，此字段生效。枚举值为卡片支持的颜色枚举值和 RGBA 语法自定义颜色，参考颜色枚举值。"""

    corner_radius: Union[str, None] = None
    """交互容器的圆角半径，单位是像素（px）或百分比（%）。取值遵循以下格式：

    [0,∞]px，如 "10px"
    [0,100]%，如 "30%" """

    padding: Union[str, None] = None
    """交互容器的内边距。值的取值范围为 [0,28]px。支持填写单值或多值：

    单值：如 "10px"，表示容器内四个内边距都为 10px
    多值：如 "4px 12px 4px 12px"，表示容器内上、右、下、左的内边距分别为 4px，12px，4px，12px。四个值必填，使用空格间隔"""

    behaviors: BehaviorType
    """https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/configuring-card-interactions#355ec8c0"""

    hover_tips: Union[PlainText, None] = None
    """用户在 PC 端将光标悬浮在交互容器上方时的文案提醒。默认为空。"""

    disabled: Union[bool, None] = None
    """是否禁用交互容器。可选值：

    true：禁用整个容器
    false：容器组件保持可用状态"""

    disabled_tips: Union[PlainText, None] = None
    """禁用交互容器后，用户触发交互时的弹窗文案提醒。默认为空，即不弹窗。"""

    confirm: Union[ConfirmDialogue, None] = None
    """二次确认弹窗配置。指在用户提交时弹出二次确认弹窗提示；只有用户点击确认后，才提交输入的内容。该字段默认提供了确认和取消按钮，你只需要配置弹窗的标题与内容即可。"""

    elements: List[InteractiveContainerElementType]
