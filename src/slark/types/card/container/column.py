from typing import List, Union

from typing_extensions import Literal

from ..base import BaseElement, BaseModel
from ..displaying.chart import ChartElement
from ..displaying.divider import HlineElement
from ..displaying.image import ImageElement
from ..displaying.image_combination import ImageCombinationElement
from ..displaying.markdown import MDElement
from ..displaying.note import NoteElement
from ..displaying.person import PersonElement
from ..displaying.person_list import PersonListElement
from ..displaying.plain_text import DivElement
from ..interactive.button import ButtonElement
from ..interactive.checker import CheckerElement
from ..interactive.date_picker import DatePickerElement
from ..interactive.input_box import InputBoxElement
from ..interactive.multi_select_person import MultiSelectPersonElement
from ..interactive.multi_select_static import MultiSelectStaticElement
from ..interactive.picker_datetime import PickerDatetimeElement
from ..interactive.picker_time import PickerTimeElement
from ..interactive.select_img import SelectImgElement
from ..interactive.select_person import SelectPersonElement
from ..interactive.select_static import SelectStaticElement

"""https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-components/containers/column-set"""


class ColumnSetActionMultiUrl(BaseModel):
    url: Union[str, None] = None
    android_url: Union[str, None] = None
    ios_url: Union[str, None] = None
    pc_url: Union[str, None] = None


class ColumnSetAction(BaseModel):
    multi_url: Union[ColumnSetActionMultiUrl, None] = None


ColumnSupportElementType = Union[
    MDElement,
    DivElement,
    ImageElement,
    HlineElement,
    "ColumnSetElement",
    ChartElement,
    ImageCombinationElement,
    PersonElement,
    PersonListElement,
    NoteElement,
    ButtonElement,
    InputBoxElement,
    MultiSelectPersonElement,
    MultiSelectStaticElement,
    SelectPersonElement,
    SelectStaticElement,
    SelectImgElement,
    PickerDatetimeElement,
    PickerTimeElement,
    DatePickerElement,
    CheckerElement,
]


class ColumnElement(BaseElement):
    tag: str = "column"
    background_style: str = "default"
    """列的背景色样式。可取值：

    default：默认的白底样式，客户端深色主题下为黑底样式
    卡片支持的颜色枚举值和 RGBA 语法自定义颜色。参考颜色枚举值。"""

    elements: List[ColumnSupportElementType] = []
    """列容器内嵌的组件，不支持内嵌表格组件、多图混排组件和表单容器。"""

    width: Union[Literal["auto", "weighted"], str] = "auto"
    """列宽度。仅 flex_mode 为 none 时，生效此属性。取值：

    auto：列宽度与列内元素宽度一致
    weighted：列宽度按 weight 参数定义的权重分布
    具体数值，如 100px。取值范围为 [16,600]px。V7.4 及以上版本支持该枚举"""

    weight: int = 1
    """当 width 字段取值为 weighted 时生效，表示当前列的宽度占比。取值范围为 1 ~ 5 之间的整数。"""

    vertical_align: Literal["top", "center", "bottom"] = "top"
    """列垂直居中的方式。可取值：

    top：上对齐
    center：居中对齐
    bottom：下对齐"""

    vertical_spacing: Union[Literal["default", "medium", "large"], str] = "default"
    """列内组件的纵向间距。取值：

    default：默认间距，8px
    medium：中等间距
    large：大间距
    具体数值，如 8px。取值范围为 [0,28]px"""

    padding: Union[str, None] = None
    """列的内边距。值的取值范围为 [0,28]px。可选值：

    单值，如 "10px"，表示列的四个外边距都为 10 px。
    多值，如 "4px 12px 4px 12px"，表示列的上、右、下、左的外边距分别为 4px，12px，4px，12px。四个值必填，使用空格间隔。"""

    action: Union[ColumnSetAction, None] = None


class ColumnSetElement(BaseElement):
    tag: str = "column_set"
    """组件的标签。分栏组件的固定值为 column_set。"""
    flex_mode: Literal["none", "stretch", "flow", "bisect", "trisect"] = "none"
    """移动端和 PC 端的窄屏幕下，各列的自适应方式。取值：
    none：不做布局上的自适应，在窄屏幕下按比例压缩列宽度
    stretch：列布局变为行布局，且每列（行）宽度强制拉伸为 100%，所有列自适应为上下堆叠排布
    flow：列流式排布（自动换行），当一行展示不下一列时，自动换至下一行展示
    bisect：两列等分布局
    trisect：三列等分布局"""

    horizontal_spacing: Union[Literal["default", "small", "large"], str] = "default"
    """各列之间的水平分栏间距。取值：
    default：默认间距，8px
    small：窄间距，4px
    large：大间距，12px
    [0, 28px]：自定义间距"""

    horizontal_align: Literal["left", "center", "right"] = "left"
    """列容器水平对齐的方式。可取值：
    left：左对齐
    center：居中对齐
    right：右对齐"""

    margin: Union[str, None] = None
    """列的外边距。值的取值范围为 [0,28]px。可选值：
    单值，如 "10px"，表示列的四个外边距都为 10 px。
    多值，如 "4px 12px 4px 12px"，表示列的上、右、下、左的外边距分别为 4px，12px，4px，12px。四个值必填，使用空格间隔。
    注意：首行列的上外边距强制为 0，末行列的下外边距强制为 0。"""

    background_style: str = "default"
    """分栏的背景色样式。可取值：
    default：默认的白底样式，客户端深色主题下为黑底样式
    卡片支持的颜色枚举值和 RGBA 语法自定义颜色。参考颜色枚举值。
    注意：当存在分栏的嵌套时，上层分栏的颜色覆盖下层分栏的颜色。"""

    columns: List[ColumnElement] = []
    """分栏中列的配置。"""

    action: Union[ColumnSetAction, None] = None
