from typing import TYPE_CHECKING

import anyio

if TYPE_CHECKING:
    from slark.client.lark import AsyncLark


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
