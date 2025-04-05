from typing import List, Union

from ..base import BaseElement
from .button import ButtonElement
from .checker import CheckerElement
from .date_picker import DatePickerElement
from .input_box import InputBoxElement
from .multi_select_person import MultiSelectPersonElement
from .multi_select_static import MultiSelectStaticElement
from .overflow import OverflowElement
from .picker_datetime import PickerDatetimeElement
from .picker_time import PickerTimeElement
from .select_img import SelectImgElement
from .select_person import SelectPersonElement
from .select_static import SelectStaticElement

ActionElementType = Union[
    ButtonElement,
    CheckerElement,
    DatePickerElement,
    InputBoxElement,
    MultiSelectPersonElement,
    MultiSelectStaticElement,
    OverflowElement,
    PickerDatetimeElement,
    PickerTimeElement,
    SelectImgElement,
    SelectPersonElement,
    SelectStaticElement,
]


class ActionElements(BaseElement):
    tag: str = "action"
    layout: Union[str, None] = None
    actions: List[ActionElementType]
