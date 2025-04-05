from typing import List, Union

from ..base import BaseElement
from ..color import Color


class CollapsibleElement(BaseElement):
    tag: str = "collapsible_panel"
    expanded: Union[bool, None] = None
    background_color: Union[Color, None] = None
    elements: List[BaseElement]