from typing_extensions import Literal

from ..base import BaseElement


class PersonElement(BaseElement):
    tag: str = "person"
    size: Literal["extra_small", "small", "medium", "large"] = "medium"
    show_avatar: bool = False
    show_name: bool = True
    style: Literal["normal", "capsule"] = "normal"
    user_id: str