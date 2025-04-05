from typing import List, Union

from ..base import BaseElement
from ..icon import IconElement
from .image import ImageElement
from .plain_text import PlainTextElement


class NoteElement(BaseElement):
    tag: str = "note"
    elements: List[Union[IconElement, PlainTextElement, ImageElement]]
