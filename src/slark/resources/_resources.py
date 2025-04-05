import time
from typing import TYPE_CHECKING

import anyio

if TYPE_CHECKING:
    from slark.client.lark import AsyncLark
    from slark.client.sync_lark import Lark


class AsyncAPIResource:
    _client: "AsyncLark"

    def __init__(self, client: "AsyncLark"):
        self._client = client
        self._get = client.get
        self._post = client.post
        self._put = client.put
        self._delete = client.delete
        self._patch = client.patch

    async def _sleep(self, seconds: float):
        await anyio.sleep(seconds)


class APIResource:
    _client: "Lark"

    def __init__(self, client: "Lark"):
        self._client = client
        self._get = client.get
        self._post = client.post
        self._put = client.put
        self._delete = client.delete
        self._patch = client.patch

    def _sleep(self, seconds: float):
        time.sleep(seconds)
