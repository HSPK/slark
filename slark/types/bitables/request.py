from typing import Union

from pydantic import BaseModel


class UpdateBitableMetaBody(BaseModel):
    name: Union[str, None] = None
    is_advanced: Union[bool, None] = None
