from typing import List, Union

from typing_extensions import TYPE_CHECKING

from ..base import BaseElement
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

if TYPE_CHECKING:
    from .column import ColumnSetElement

FormElementType = Union[
    MDElement,
    DivElement,
    ImageElement,
    HlineElement,
    "ColumnSetElement",
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


class FormElement(BaseElement):
    tag: str = "form"
    """表单容器的标签。固定值为 form。"""
    name: str
    """表单容器的唯一标识。用于识别用户提交的数据属于哪个表单容器。在同一张卡片内，该字段的值全局唯一。"""
    elements: List[FormElementType]
    """表单容器的子节点。可内嵌其它容器类组件和展示、交互组件，不支持内嵌表格、图表、和表单容器组件。"""
