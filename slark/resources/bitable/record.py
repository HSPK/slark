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
    BatchUpdateRecordResponse,
    CreateRecordResponse,
    DeleteRecordResponse,
    SearchRecordResponse,
    UpdateRecordResponse,
)


class AsyncRecord(AsyncAPIResource):
    MAX_RECORDS_PER_REQUEST = 500

    async def create(
        self,
        app_token: str,
        *,
        table_id: str,
        fields: Dict[str, FieldValueType],
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        client_token: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> CreateRecordResponse:
        """该接口用于在数据表中新增一条记录
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/create

        Args:
            app_token (str): 多维表格的唯一标识符
            table_id (str): 多维表格数据表的唯一标识符
            fields (Dict[str, FieldValueType]): 数据表的字段，即数据表的列。\
                [数据结构](https://open.feishu.cn/document/server-docs/docs/bitable-v1/bitable-structure)
            user_id_type (Union[Literal[&quot;open_id&quot;, &quot;union_id&quot;, &quot;user_id&quot;], None], optional): \
                用户 ID 类型. Defaults to None.
            client_token (Union[str, None], optional): 格式为标准的 uuidv4，操作的唯一标识，用于幂等的进行更新操作。\
                此值为空表示将发起一次新的请求，此值非空表示幂等的进行更新操作。. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            CreateRecordResponse: 新增记录的返回结果
        """
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
    ) -> UpdateRecordResponse:
        """该接口用于在数据表中更新一条记录
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/update

        Args:
            app_token (str): 多维表格的唯一标识符
            table_id (str): 多维表格数据表的唯一标识符
            record_id (str): 一条记录的唯一标识 id 
            fields (Dict[str, FieldValueType]): 数据表的字段，即数据表的列。
            user_id_type (Union[Literal[&quot;open_id&quot;, &quot;union_id&quot;, &quot;user_id&quot;], None], optional): \
                用户 ID 类型. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            UpdateRecordResponse: 更新记录的返回结果
        """
        return await self._put(
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
    ) -> DeleteRecordResponse:
        """该接口用于在数据表中删除一条记录
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/delete

        Args:
            app_token (str): 多维表格的唯一标识符
            table_id (str): 多维表格数据表的唯一标识符
            record_id (str): 一条记录的唯一标识 id
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            DeleteRecordResponse: 删除记录的返回结果
        """
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
    ) -> SearchRecordResponse:
        """该接口用于查询数据表中的现有记录，单次最多查询 500 行记录，支持分页获取。
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search

        Args:
            app_token (str): 多维表格的唯一标识符
            table_id (str): 多维表格数据表的唯一标识符
            view_id (Union[str, None], optional): 视图的唯一标识符，获取指定视图下的记录. Defaults to None.
            field_names (Union[str, None], optional): 字段名称，用于指定本次查询返回记录中包含的字段. Defaults to None.
            sort (Union[List[SearchRecordSort], None], optional): 排序条件. Defaults to None.
            filter (Union[SearchRecordFilter, None], optional): 筛选条件. Defaults to None.
            automatic_fields (Union[bool, None], optional): 控制是否返回自动计算的字段, true 表示返回. Defaults to None.
            user_id_type (Union[Literal[&quot;open_id&quot;, &quot;union_id&quot;, &quot;user_id&quot;], None], optional): 用户 ID 类型. Defaults to None.
            page_token (Union[str, None], optional): 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果. Defaults to None.
            page_size (Union[int, None], optional): 分页大小。最大值为 500. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            SearchRecordResponse: 查询记录的返回结果
        """
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
        timeout: Union[httpx.Timeout, None] = None,
    ) -> BatchGetRecordResponse:
        """该接口用于批量获取数据表中的记录
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/batch_get

        Args:
            app_token (str): 多维表格的唯一标识符
            table_id (str): 多维表格数据表的唯一标识符
            record_ids (List[str]): 记录的唯一标识 id 列表
            user_id_type (Union[Literal[&quot;open_id&quot;, &quot;union_id&quot;, &quot;user_id&quot;], None], optional): 此次调用中使用的用户 id 的类型. Defaults to None.
            with_shared_url (Union[bool, None], optional): 是否返回记录的分享链接。. Defaults to None.
            automatic_fields (Union[bool, None], optional): 是否返回自动计算的字段。. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): _description_. Defaults to None.

        Returns:
            BatchGetRecordResponse: 批量获取记录的返回结果
        """
        return await self._post(
            API_PATH.bitables.batch_get_record.format(app_token=app_token, table_id=table_id),
            body=BatchGetRecordBody(
                record_ids=record_ids,
                user_id_type=user_id_type,
                with_shared_url=with_shared_url,
                automatic_fields=automatic_fields,
            ).model_dump(),
            options={"timeout": timeout},
            cast_to=BatchGetRecordResponse,
        )

    async def batch_create(
        self,
        app_token: str,
        *,
        table_id: str,
        records: List[Dict[str, FieldValueType]],
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        client_token: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> BatchCreateRecordResponse:
        """该接口用于在数据表中新增多条记录，单次调用最多新增 500 条记录。
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/batch_create

        Args:
            app_token (str): 多维表格的唯一标识符
            table_id (str): 多维表格数据表的唯一标识符
            records (List[Dict[str, FieldValueType]]): 记录的字段，即数据表的列
            user_id_type (Union[Literal[&quot;open_id&quot;, &quot;union_id&quot;, &quot;user_id&quot;], None], optional): 用户 ID 类型. Defaults to None.
            client_token (Union[str, None], optional): 格式为标准的 uuidv4，操作的唯一标识，用于幂等的进行更新操作。此值为空表示将发起一次新的请求，此值非空表示幂等的进行更新操作。. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            BatchCreateRecordResponse: 批量新增记录的返回结果
        """
        return await self._post(
            API_PATH.bitables.batch_create_record.format(app_token=app_token, table_id=table_id),
            body=BatchCreateRecordBody(
                records=[{"fields": record} for record in records],
            ).model_dump(),
            options={
                "timeout": timeout,
                "params": CreateRecordParams(
                    user_id_type=user_id_type, client_token=client_token
                ).model_dump(),
            },
            cast_to=BatchCreateRecordResponse,
        )

    async def batch_update(
        self,
        app_token: str,
        *,
        table_id: str,
        records: List[BatchUpdateRecord],
        user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> BatchUpdateRecordResponse:
        """该接口用于更新数据表中的多条记录，单次调用最多更新 500 条记录。
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/batch_update

        Args:
            app_token (str): 多维表格的唯一标识符
            table_id (str): 多维表格数据表的唯一标识符
            records (List[BatchUpdateRecord]): 记录的字段，即数据表的列
            user_id_type (Union[Literal[&quot;open_id&quot;, &quot;union_id&quot;, &quot;user_id&quot;], None], optional): 用户ID类型. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            BatchUpdateRecordResponse: 更新记录的返回结果
        """
        return await self._post(
            API_PATH.bitables.batch_update_record.format(app_token=app_token, table_id=table_id),
            body=BatchUpdateRecordBody(records=records).model_dump(),
            options={
                "timeout": timeout,
                "params": UpdateRecordParams(user_id_type=user_id_type).model_dump(),
            },
            cast_to=BatchUpdateRecordResponse,
        )

    async def batch_delete(
        self,
        app_token: str,
        *,
        table_id: str,
        record_ids: List[str],
        timeout: Union[httpx.Timeout, None] = None,
    ) -> BatchDeleteRecordResponse:
        """该接口用于删除数据表中现有的多条记录，单次调用中最多删除 500 条记录。
        https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/batch_delete

        Args:
            app_token (str): 多维表格的唯一标识符
            table_id (str): 多维表格数据表的唯一标识符
            record_ids (List[str]): 记录的唯一标识 id 列表
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            BatchDeleteRecordResponse: 删除记录的返回结果
        """
        return await self._post(
            API_PATH.bitables.batch_delete_record.format(app_token=app_token, table_id=table_id),
            body=BatchDeleteRecordBody(
                records=record_ids,
            ).model_dump(),
            options={"timeout": timeout},
            cast_to=BatchDeleteRecordResponse,
        )
