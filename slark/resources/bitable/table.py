from typing import List, Union

import httpx
from typing_extensions import Literal

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.bitables.table.common import TableData
from slark.types.bitables.table.request import (
    BatchCreateTableBody,
    BatchCreateTableParams,
    CreateTableBody,
    ListTableParams,
    UpdateTableBody,
)
from slark.types.bitables.table.response import (
    BatchCreateTableResponse,
    CreateTableResponse,
    ListTableResponse,
    UpdateTableResponse,
)


class AsyncTable(AsyncAPIResource):
    async def list(
        self,
        app_token: str,
        *,
        timeout: Union[httpx.Timeout, None] = None,
        page_token: Union[str, None] = None,
        page_size: Union[int, None] = None,
    ):
        return await self._get(
            API_PATH.bitables.list_tables.format(app_token=app_token),
            options={
                "timeout": timeout,
                "params": ListTableParams(
                    page_token=page_token,
                    page_size=page_size,
                ).model_dump(),
            },
            cast_to=ListTableResponse,
        )

    async def create(
        self,
        app_token: str,
        *,
        table: TableData,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._post(
            API_PATH.bitables.create_table.format(app_token=app_token),
            options={
                "timeout": timeout,
                "json_data": CreateTableBody(
                    table=table,
                ).model_dump(),
            },
            cast_to=CreateTableResponse,
        )

    async def batch_create(
        self,
        app_token: str,
        *,
        names: List[str],
        user_id_type: Union[Literal["user_id", "open_id", "union_id"], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._post(
            API_PATH.bitables.batch_create_table.format(app_token=app_token),
            body=BatchCreateTableBody(tables=[{"name": name} for name in names]).model_dump(),
            cast_to=BatchCreateTableResponse,
            options={
                "timeout": timeout,
                "params": BatchCreateTableParams(user_id_type=user_id_type).model_dump(),
            },
        )

    async def update(
        self,
        app_token: str,
        *,
        table_id: str,
        name: str,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._patch(
            API_PATH.bitables.update_table.format(app_token=app_token, table_id=table_id),
            body=UpdateTableBody(name=name).model_dump(),
            cast_to=UpdateTableResponse,
            options={"timeout": timeout},
        )
