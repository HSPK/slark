from typing import Dict, TypedDict, Union

import httpx
from typing_extensions import Literal

from slark._constants import DEFAULT_MAX_RETRIES
from slark.types._common import BaseModel


class RequestOptions(TypedDict):
    headers: dict
    timeout: httpx.Timeout
    params: dict
    max_retries: int
    no_auth: bool
    raw_response: bool
    files: Dict
    data: Dict


class FinalRequestOptions(BaseModel):
    method: Literal["get", "post", "put", "delete", "patch"]
    url: str
    headers: dict = {}
    params: dict = {}
    max_retries: Union[int, None] = DEFAULT_MAX_RETRIES
    timeout: Union[httpx.Timeout, None] = None
    files: Union[Dict, None] = None
    data: Union[Dict, None] = None
    no_auth: bool = False
    raw_response: bool = False

    def get_max_retries(self, max_retries: int) -> int:
        return self.max_retries if self.max_retries is not None else max_retries
