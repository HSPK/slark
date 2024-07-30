from typing import Dict, List, Union

import httpx
from typing_extensions import Literal

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.bitables.record.common import FieldValueType
from slark.types.bitables.record.request import (
    BatchCreateRecordBody,
    BatchDeleteRecordBody,
    BatchGetRecordBody,
    BatchUpdateRecord,
    BatchUpdateRecordBody,
    CreateRecordBody,
    CreateRecordParams,
    SearchRecordBody,
    SearchRecordFilter,
    SearchRecordParams,
    SearchRecordSort,
    UpdateRecordBody,
    UpdateRecordParams,
)
from slark.types.bitables.record.response import (
    BatchCreateRecordResponse,
    BatchDeleteRecordResponse,
    BatchGetRecordResponse,
    CreateRecordResponse,
    DeleteRecordResponse,
    SearchRecordResponse,
    UpdateRecordResponse,
)


class AsyncRecord(AsyncAPIResource):
    async def create(
        self,
        app_token: str,
        *,
        table_id: str,
        fields: Dict[str, FieldValueType],
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        client_token: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._post(
            API_PATH.bitables.create_record.format(app_token=app_token, table_id=table_id),
            body=CreateRecordBody(
                fields=fields,
            ).model_dump(),
            options={
                "timeout": timeout,
                "params": CreateRecordParams(
                    user_id_type=user_id_type, client_token=client_token
                ).model_dump(),
            },
            cast_to=CreateRecordResponse,
        )

    async def update(
        self,
        app_token: str,
        *,
        table_id: str,
        record_id: str,
        fields: Dict[str, FieldValueType],
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._patch(
            API_PATH.bitables.update_record.format(
                app_token=app_token, table_id=table_id, record_id=record_id
            ),
            body=UpdateRecordBody(
                fields=fields,
            ).model_dump(),
            options={
                "timeout": timeout,
                "params": UpdateRecordParams(user_id_type=user_id_type).model_dump(),
            },
            cast_to=UpdateRecordResponse,
        )

    async def delete(
        self,
        app_token: str,
        *,
        table_id: str,
        record_id: str,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._delete(
            API_PATH.bitables.delete_record.format(
                app_token=app_token, table_id=table_id, record_id=record_id
            ),
            options={"timeout": timeout},
            cast_to=DeleteRecordResponse,
        )

    async def search(
        self,
        app_token: str,
        *,
        table_id: str,
        view_id: Union[str, None] = None,
        field_names: Union[str, None] = None,
        sort: Union[List[SearchRecordSort], None] = None,
        filter: Union[SearchRecordFilter, None] = None,
        automatic_fields: Union[bool, None] = None,
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        page_token: Union[str, None] = None,
        page_size: Union[int, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._post(
            API_PATH.bitables.search_record.format(app_token=app_token, table_id=table_id),
            body=SearchRecordBody(
                view_id=view_id,
                field_names=field_names,
                sort=sort,
                filter=filter,
                automatic_fields=automatic_fields,
            ).model_dump(),
            options={
                "timeout": timeout,
                "params": SearchRecordParams(
                    user_id_type=user_id_type,
                    page_token=page_token,
                    page_size=page_size,
                ).model_dump(),
            },
            cast_to=SearchRecordResponse,
        )

    async def batch_get(
        self,
        app_token: str,
        *,
        table_id: str,
        record_ids: List[str],
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        with_shared_url: Union[bool, None] = None,
        automatic_fields: Union[bool, None] = None,
        page_token: Union[str, None] = None,
        page_size: Union[int, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return await self._post(
            API_PATH.bitables.batch_get_record.format(app_token=app_token, table_id=table_id),
            body=BatchGetRecordBody(
                record_ids=record_ids,
                user_id_type=user_id_type,
                with_shared_url=with_shared_url,
                automatic_fields=automatic_fields,
            ).model_dump(),
            options={
                "timeout": timeout,
                "params": SearchRecordParams(
                    user_id_type=user_id_type,
                    page_token=page_token,
                    page_size=page_size,
                ).model_dump(),
            },
            cast_to=BatchGetRecordResponse,
        )

    def batch_create(
        self,
        app_token: str,
        *,
        table_id: str,
        records: List[Dict[str, FieldValueType]],
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        client_token: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return self._post(
            API_PATH.bitables.batch_create_record.format(app_token=app_token, table_id=table_id),
            body=BatchCreateRecordBody(
                records=records,
            ).model_dump(),
            options={
                "timeout": timeout,
                "params": CreateRecordParams(
                    user_id_type=user_id_type, client_token=client_token
                ).model_dump(),
            },
            cast_to=BatchCreateRecordResponse,
        )

    def batch_update(
        self,
        app_token: str,
        *,
        table_id: str,
        records: List[BatchUpdateRecord],
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return self._patch(
            API_PATH.bitables.batch_update_record.format(app_token=app_token, table_id=table_id),
            body=BatchUpdateRecordBody(
                records=records,
            ).model_dump(),
            options={
                "timeout": timeout,
                "params": UpdateRecordParams(user_id_type=user_id_type).model_dump(),
            },
            cast_to=UpdateRecordResponse,
        )

    def batch_delete(
        self,
        app_token: str,
        *,
        table_id: str,
        record_ids: List[str],
        timeout: Union[httpx.Timeout, None] = None,
    ):
        return self._delete(
            API_PATH.bitables.batch_delete_record.format(app_token=app_token, table_id=table_id),
            body=BatchDeleteRecordBody(
                record_ids=record_ids,
            ).model_dump(),
            options={"timeout": timeout},
            cast_to=BatchDeleteRecordResponse,
        )
