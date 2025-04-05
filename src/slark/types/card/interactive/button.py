from typing import List, Union

from typing_extensions import Literal

from ..base import BaseElement
from ..behavior import BehaviorType
from ..confirm import ConfirmDialogue
from ..icon import IconElement
from ..text import PlainText

"""https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-components/interactive-components/button"""

"""在卡片 JSON 1.0 结构中，若按钮组件直接位于卡片根节点，而非嵌套在其它组件中，你需将其 JSON 数据配置在交互模块（"tag": "action"）的 actions 字段中使用。

卡片 JSON 2.0 结构已不支持交互模块（"tag": "action"）相关属性。你可直接将按钮放置于 elements 中，并配置合适的组件间距 (vertical_spacing 和 horizontal_spacing) 使用。

嵌套规则

按钮组件支持嵌套在分栏、表单容器、折叠面板、循环容器中使用。
"""


class ButtonElement(BaseElement):
    tag: str = "button"
    type: Literal[
        "default",
        "primary",
        "danger",
        "text",
        "primary_text",
        "danger_text",
        "primary_filled",
        "danger_filled",
        "laser",
    ] = "default"
    """按钮的类型。可选值：

    default：黑色字体按钮，有边框
    primary：蓝色字体按钮，有边框
    danger：红色字体按钮，有边框
    text：黑色字体按钮，无边框
    primary_text：蓝色字体按钮，无边框
    danger_text：红色字体按钮，无边框
    primary_filled：蓝底白字按钮
    danger_filled：红底白字按钮
    laser：镭射按钮"""

    name: str
    """按钮的名称，用于标识按钮。"""
    form_action_type: Literal["submit", "reset", "none"] = "none"
    """按钮的行为。可选值"submit"、"reset"、"none"。"""
    size: Literal["tiny", "small", "medium", "large"] = "medium"
    """按钮的尺寸。可选值：

    tiny：超小尺寸，PC 端为 24 px；移动端为 28 px
    small：小尺寸，PC 端为 28 px；移动端为 28 px
    medium：中尺寸，PC 端为 32 px；移动端为 36 px
    large：大尺寸，PC 端为 40 px；移动端为 48 px"""

    width: Union[Literal["default", "fill"], str] = "default"
    """按钮的宽度。支持以下枚举值：

    default：默认宽度
    fill：卡片最大支持宽度
    [100,∞)px：自定义宽度，如 120px。超出卡片宽度时将按最大支持宽度展示"""

    text: Union[PlainText, None] = None
    """按钮上的文本。"""

    icon: Union[IconElement, None] = None
    """添加图标作为文本前缀图标。支持自定义或使用图标库中的图标。"""

    hover_tips: Union[PlainText, None] = None
    """用户在 PC 端将光标悬浮在交互容器上方时的文案提醒。默认为空。"""

    disabled: Union[bool, None] = None
    disabled_tips: Union[PlainText, None] = None
    """禁用按钮后，用户触发交互时的弹窗文案提醒。默认为空，即不弹窗。"""

    confirm: Union[ConfirmDialogue, None] = None
    """二次确认弹窗配置。指在用户提交时弹出二次确认弹窗提示；只有用户点击确认后，才提交输入的内容。该字段默认提供了确认和取消按钮，你只需要配置弹窗的标题与内容即可。"""

    behaviors: Union[List[BehaviorType], None] = None
