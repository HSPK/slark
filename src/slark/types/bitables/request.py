from typing import Union

from slark.types._common import BaseModel


class UpdateBitableMetaBody(BaseModel):
    name: Union[str, None] = None
    is_advanced: Union[bool, None] = None
