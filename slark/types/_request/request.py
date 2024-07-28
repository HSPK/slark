from pydantic import BaseModel, ConfigDict
from typing import Literal
import httpx
from typing import TypedDict
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
    max_retries: int = DEFAULT_MAX_RETRIES
    timeout: httpx.Timeout | None = None
    json_data: object | None = None
    no_auth: bool = False

    model_config = ConfigDict(arbitrary_types_allowed=True)
