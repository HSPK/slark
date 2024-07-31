from typing import List, Union

import httpx
from typing_extensions import Literal

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.bitables.table.common import TableData
from slark.types.bitables.table.request import (
    BatchCreateTableBody,
    BatchCreateTableParams,
    BatchDeleteTableBody,
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
from slark.types.response import BaseResponse


class AsyncTable(AsyncAPIResource):
    async def list(
        self,
        app_token: str,
        *,
        timeout: Union[httpx.Timeout, None] = None,
        page_token: Union[str, None] = None,
        page_size: Union[int, None] = None,
    ) -> ListTableResponse:
        """根据 app_token，获取多维表格下的所有数据表
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table/list

        Args:
            app_token (str): 多维表格的 app_token
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.
            page_token (Union[str, None], optional): 分页标记，第一次请求不填，表示从头开始遍历；\
                分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果。\
                示例值："tblsRc9GRRXKqhvW". Defaults to None.
            
            page_size (Union[int, None], optional): 分页大小，示例值：10，默认值：20，数据校验规则：\
                最大值：100. Defaults to None.

        Returns:
            ListTableResponse: 数据表列表
        """
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
    ) -> CreateTableResponse:
        """新增数据表
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table/create

        Args:
            app_token (str): 多维表格的 app_token
            table (TableData): 表格数据
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            CreateTableResponse: 创建返回值
        """
        return await self._post(
            API_PATH.bitables.create_table.format(app_token=app_token),
            body=CreateTableBody(
                table=table,
            ).model_dump(),
            options={"timeout": timeout},
            cast_to=CreateTableResponse,
        )

    async def batch_create(
        self,
        app_token: str,
        *,
        names: List[str],
        user_id_type: Union[Literal["user_id", "open_id", "union_id"], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> BatchCreateTableResponse:
        """新增多个数据表。
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table/batch_create

        Args:
            app_token (str): 多维表格的唯一标识符
            names (List[str]): 数据表名称，注意名称中的首尾空格将会被去除。长度范围：1 字符 ～ 100 字符。
            user_id_type (Union[Literal[&quot;user_id&quot;, &quot;open_id&quot;, &quot;union_id&quot;], None], optional): 用户 ID 类型. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            BatchCreateTableResponse: 创建返回值
        """
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
    ) -> UpdateTableResponse:
        r"""该接口用于更新数据表的基本信息，包括数据表的名称等。

        Args:
            app_token (str): 多维表格的 app_token
            table_id (str): 多维表格的 table_id
            name (str): 数据表的新名称。请注意：名称中的首尾空格将会被去除。
                如果名称为空或和旧名称相同，接口仍然会返回成功，但是名称不会被更改。\n
                示例值："数据表的新名称"。\
                数据校验规则：长度范围：1 字符 ～ 100 字符。正则校验：^[^\[\]\:\\\/\?\*]+$。
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            UpdateTableResponse: 更新返回值
        """
        return await self._patch(
            API_PATH.bitables.update_table.format(app_token=app_token, table_id=table_id),
            body=UpdateTableBody(name=name).model_dump(),
            cast_to=UpdateTableResponse,
            options={"timeout": timeout},
        )

    async def delete(
        self,
        app_token: str,
        *,
        table_id: str,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> BaseResponse:
        """删除数据表
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table/delete

        Args:
            app_token (str): 多维表格的 app_token
            table_id (str): 多维表格的 table_id
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            BaseResponse: 删除返回值
        """
        return await self._delete(
            API_PATH.bitables.delete_table.format(app_token=app_token, table_id=table_id),
            options={"timeout": timeout},
            cast_to=BaseResponse,
        )

    async def batch_delete(
        self,
        app_token: str,
        *,
        table_ids: List[str],
        timeout: Union[httpx.Timeout, None] = None,
    ) -> BaseResponse:
        """批量删除数据表
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table/batch_delete

        Args:
            app_token (str): 多维表格的 app_token
            table_ids (List[str]): 待删除的数据表的 id
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            BaseResponse: 删除返回值
        """
        return await self._post(
            API_PATH.bitables.batch_delete_table.format(app_token=app_token),
            body=BatchDeleteTableBody(table_ids=table_ids).model_dump(),
            options={"timeout": timeout},
            cast_to=BaseResponse,
        )
