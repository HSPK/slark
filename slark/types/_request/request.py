from typing import Dict, TypedDict, Union

import httpx
from pydantic import BaseModel, ConfigDict
from typing_extensions import Literal

from slark._constants import DEFAULT_MAX_RETRIES


class RequestOptions(TypedDict):
    headers: dict
    timeout: httpx.Timeout
    params: dict
    max_retries: int
    no_auth: bool


class FinalRequestOptions(BaseModel):
    method: Literal["get", "post", "put", "delete", "patch"]
    url: str
    headers: dict = {}
    params: dict = {}
    max_retries: Union[int, None] = DEFAULT_MAX_RETRIES
    timeout: Union[httpx.Timeout, None] = None
    json_data: Union[Dict] = None
    no_auth: bool = False

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def get_max_retries(self, max_retries: int) -> int:
        return self.max_retries if self.max_retries is not None else max_retries
