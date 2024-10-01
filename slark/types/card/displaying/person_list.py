from typing import List, Union

from typing_extensions import Literal

from ..base import BaseElement, BaseModel
from ..icon import IconElement
from ..ud_icon import UDIconElement


class PersonListPerson(BaseModel):
    user_id: str


class PersonListElement(BaseElement):
    tag: str = "person_list"
    lines: Union[int, None] = None
    show_name: bool = True
    show_avatar: bool = False
    size: Literal["extra_small", "small", "medium", "large"] = "medium"
    persons: List[PersonListPerson]
    icon: Union[IconElement, None] = None
    ud_icon: Union[UDIconElement, None] = None
