from typing import List, Union

from typing_extensions import Literal

from ..base import BaseElement, BaseModel


class ImageCombinationList(BaseModel):
    img_key: str


class ImageCombinationElement(BaseElement):
    tag: str = "img_combination"
    combination_mode: Literal["double", "triple", "bisect", "trisect"] = "double"
    corner_radius: Union[str, None] = None
    img_list: List[ImageCombinationList]