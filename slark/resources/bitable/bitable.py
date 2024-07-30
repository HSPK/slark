from typing import Union

import httpx

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types._utils import cached_property
from slark.types.bitables.request import UpdateBitableMetaBody
from slark.types.bitables.response import GetBitableMetaResponse, UpdateBitableMetaResponse

from .field import AsyncField
from .record import AsyncRecord
from .table import AsyncTable
from .view import AsyncView


class AsyncBiTable(AsyncAPIResource):
    @cached_property
    def field(self) -> AsyncField:
        return AsyncField(self._client)

    @cached_property
    def record(self) -> AsyncRecord:
        return AsyncRecord(self._client)

    @cached_property
    def view(self) -> AsyncView:
        return AsyncView(self._client)

    @cached_property
    def table(self) -> AsyncTable:
        return AsyncTable(self._client)

    async def get_bitable_meta(
        self,
        app_token: str,
        *,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._get(
            API_PATH.bitables.get_bitable_meta.format(app_token=app_token),
            cast_to=GetBitableMetaResponse,
            options={"timeout": timeout},
        )

    async def update_bitable_meta(
        self,
        app_token: str,
        *,
        name: Union[str, None] = None,
        is_advanced: Union[bool, None] = None,
    ):
        return await self._put(
            API_PATH.bitables.update_bitable_meta.format(app_token=app_token),
            body=UpdateBitableMetaBody(
                name=name,
                is_advanced=is_advanced,
            ).model_dump(),
            cast_to=UpdateBitableMetaResponse,
        )
