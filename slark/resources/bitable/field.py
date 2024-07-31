from typing import Union

import httpx

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.bitables.field.common import (
    FieldDescription,
    FieldPropertyType,
    FieldType,
    UIType,
)
from slark.types.bitables.field.request import (
    CreateFieldBody,
    CreateFieldParams,
    ListFieldParams,
    UpdateFieldBody,
)
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
        view_id: Union[str, None] = None,
        text_field_as_array: Union[bool, None] = None,
        page_token: Union[str, None] = None,
        page_size: Union[int, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> ListFieldResponse:
        """根据 app_token 和 table_id，获取数据表的所有字段

        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/list
        Args:
            app_token (str): 多维表格的 app_token
            table_id (str): 多维表格的 table_id
            view_id (Union[str, None], optional): 视图 ID. 示例值："vewOVMEXPF". Defaults to None.
            text_field_as_array (Union[bool, None], optional): 	控制字段描述（多行文本格式）数据的返回格式, true 表示以数组富文本形式返回。\
                示例值：true. Defaults to None.
            page_token (Union[str, None], optional): 分页标记，第一次请求不填，表示从头开始遍历；\
                分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果。示例值："fldwJ4YrtB". Defaults to None.
            page_size (Union[int, None], optional): 分页大小，最大支持 100。示例值：10. Defaults to 20. 
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            ListFieldResponse: 数据表的所有字段
        """
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
        ui_type: Union[UIType, None] = None,
        disable_sync: Union[bool, None] = None,
        text: Union[FieldDescription, None] = None,
        client_token: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> CreateFieldResponse:
        """该接口用于在数据表中新增一个字段
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/create

        Args:
            app_token (str): 多维表格的 app_token
            table_id (str): 多维表格的 table_id
            field_name (str): 多维表格字段名。请注意：名称中的首尾空格将会被去除。示例值："多行文本"
            type (FieldType): 多维表格字段类型
            property (Union[FieldPropertyType, None], optional): 字段属性. Defaults to None.
            ui_type (Union[UIType, None], optional): 字段在界面上的展示类型，例如进度字段是数字的一种展示形态. Defaults to None.
            disable_sync (Union[bool, None], optional): 是否禁止同步，如果为true，\
                表示禁止同步该描述内容到表单的问题描述（只在新增、修改字段时生效）. Defaults to None.
            text (Union[FieldDescription, None], optional): 字段的描述. Defaults to None.
            client_token (Union[str, None], optional): 格式为标准的 uuidv4，操作的唯一标识，用于幂等的进行更新操作。\
                此值为空表示将发起一次新的请求，此值非空表示幂等的进行更新操作。\
                示例值："fe599b60-450f-46ff-b2ef-9f6675625b97"
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Raises:
            ValueError: disable_sync and text must be set together

        Returns:
            CreateFieldResponse: 新增字段的返回值
        """
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
            options={
                "timeout": timeout,
                "params": CreateFieldParams(client_token=client_token).model_dump(),
            },
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
        ui_type: Union[UIType, None] = None,
        disable_sync: Union[bool, None] = None,
        text: Union[FieldDescription, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> UpdateFieldResponse:
        """该接口用于在数据表中更新一个字段
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/update

        Args:
            app_token (str): 多维表格的 app_token
            table_id (str): 多维表格的 table_id
            field_id (str): 多维表格的 field_id
            field_name (str): 多维表格字段名，名称中的首尾空格将会被去除。示例值："多行文本"。
            type (FieldType): 多维表格字段类型
            property (Union[FieldPropertyType, None], optional): 字段属性. Defaults to None.
            ui_type (Union[UIType, None], optional): 字段在界面上的展示类型，例如进度字段是数字的一种展示形态. Defaults to None.
            disable_sync (Union[bool, None], optional): 是否禁止同步，如果为true，\
                表示禁止同步该描述内容到表单的问题描述（只在新增、修改字段时生效）. Defaults to None.
            text (Union[FieldDescription, None], optional): 字段描述内容. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Raises:
            ValueError: disable_sync and text must be set together

        Returns:
            UpdateFieldResponse: 更新字段的返回值
        """
        if disable_sync is not None and text is not None:
            desp = FieldDescription(disable_sync=disable_sync, text=text)
        elif disable_sync is None and text is not None or disable_sync is not None and text is None:
            raise ValueError("disable_sync and text must be set together")
        else:
            desp = None
        return await self._put(
            API_PATH.bitables.update_field.format(
                app_token=app_token,
                table_id=table_id,
                field_id=field_id,
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
    ) -> DeleteFieldResponse:
        """该接口用于在数据表中删除一个字段
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/delete

        Args:
            app_token (str): 多维表格的 app_token
            table_id (str): 多维表格的 table_id
            field_id (str): 多维表格的 field_id

        Returns:
            DeleteFieldResponse: 删除字段的返回值
        """
        return await self._delete(
            API_PATH.bitables.delete_field.format(
                app_token=app_token, table_id=table_id, field_id=field_id
            ),
            cast_to=DeleteFieldResponse,
        )
