from typing import Union

import httpx

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.bitables.field.common import (
    FieldDescription,
    FieldPropertyType,
    FieldType,
    FieldUIType,
)
from slark.types.bitables.field.request import CreateFieldBody, ListFieldParams, UpdateFieldBody
from slark.types.bitables.field.response import (
    CreateFieldResponse,
    DeleteFieldResponse,
    ListFieldResponse,
    UpdateFieldResponse,
)


class AsyncField(AsyncAPIResource):
    async def list(
        self,
        app_token: str,
        *,
        table_id: str,
        timeout: Union[httpx.Timeout, None] = None,
        view_id: Union[str, None] = None,
        text_field_as_array: Union[bool, None] = None,
        page_token: Union[str, None] = None,
        page_size: Union[int, None] = None,
    ):
        return await self._get(
            API_PATH.bitables.list_field.format(app_token=app_token, table_id=table_id),
            options={
                "timeout": timeout,
                "params": ListFieldParams(
                    view_id=view_id,
                    text_field_as_array=text_field_as_array,
                    page_token=page_token,
                    page_size=page_size,
                ).model_dump(),
            },
            cast_to=ListFieldResponse,
        )

    async def create(
        self,
        app_token: str,
        *,
        table_id: str,
        field_name: str,
        type: FieldType,
        property: Union[FieldPropertyType, None] = None,
        ui_type: Union[FieldUIType, None] = None,
        disable_sync: Union[bool, None] = None,
        text: Union[FieldDescription, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        if disable_sync is not None and text is not None:
            desp = FieldDescription(disable_sync=disable_sync, text=text)
        elif disable_sync is None and text is not None or disable_sync is not None and text is None:
            raise ValueError("disable_sync and text must be set together")
        else:
            desp = None
        return await self._post(
            API_PATH.bitables.create_field.format(app_token=app_token, table_id=table_id),
            body=CreateFieldBody(
                field_name=field_name,
                type=type,
                property=property,
                ui_type=ui_type,
                description=desp,
            ).model_dump(),
            options={"timeout": timeout},
            cast_to=CreateFieldResponse,
        )

    async def update(
        self,
        app_token: str,
        *,
        table_id: str,
        field_id: str,
        field_name: str,
        type: FieldType,
        property: Union[FieldPropertyType, None] = None,
        ui_type: Union[FieldUIType, None] = None,
        disable_sync: Union[bool, None] = None,
        text: Union[FieldDescription, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        if disable_sync is not None and text is not None:
            desp = FieldDescription(disable_sync=disable_sync, text=text)
        elif disable_sync is None and text is not None or disable_sync is not None and text is None:
            raise ValueError("disable_sync and text must be set together")
        else:
            desp = None
        return await self._put(
            API_PATH.bitables.update_field.format(
                app_token=app_token, table_id=table_id, field_id=field_id
            ),
            body=UpdateFieldBody(
                field_name=field_name,
                type=type,
                property=property,
                ui_type=ui_type,
                description=desp,
            ).model_dump(),
            options={"timeout": timeout},
            cast_to=UpdateFieldResponse,
        )

    async def delete(
        self,
        app_token: str,
        *,
        table_id: str,
        field_id: str,
    ):
        return await self._delete(
            API_PATH.bitables.delete_field.format(
                app_token=app_token, table_id=table_id, field_id=field_id
            ),
            cast_to=DeleteFieldResponse,
        )
