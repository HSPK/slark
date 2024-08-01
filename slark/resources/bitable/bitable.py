import re
from typing import List, Union

import httpx
import pandas as pd
from pydantic import BaseModel

from slark.resources._resources import AsyncAPIResource
from slark.types._utils import cached_property
from slark.types.bitables.record.response import RecordResponseData

from .field import AsyncField
from .meta import AsyncMeta
from .record import AsyncRecord
from .table import AsyncTable
from .utils import dataframe_to_records, fields_records_to_dataframe
from .view import AsyncView


class BitableInfo(BaseModel):
    app_token: str
    table_id: str
    view_id: Union[str, None] = None


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

    @cached_property
    def meta(self) -> AsyncMeta:
        return AsyncMeta(self._client)

    async def get_bitable_info(self, url: str) -> BitableInfo:
        """从多维表格分享链接中提取 app_token, table_id, view_id

        Args:
            url (str): URL of the bitable

        Returns:
            BitableInfo: app_token, table_id, view_id
        """
        if "/base/" in url:
            app_token, table_id, view_id = re.findall(
                r"\/base\/([^\/\?]+)(?:\?table=([^\/\&\?]+))?(?:\&view=([^\/]+))?", url
            )[0]
        elif "/wiki/" in url:
            wiki_token, table_id, view_id = re.findall(
                r"\/wiki\/([^\/\?]+)(?:\?table=([^\/\&\?]+))?(?:\&view=([^\/]+))?", url
            )[0]
            node_info = (
                await self._client.knowledge_space.nodes.get_node_info(wiki_token)
            ).data.node
            if node_info.obj_type != "bitable":
                raise ValueError("The node is not a bitable")
            app_token = node_info.obj_token
        else:
            raise ValueError("The url is not a bitable url")
        assert app_token, "BiTable token is not found"
        if not table_id:
            table_id = (await self.table.list(app_token)).data.items[0].table_id
        return BitableInfo(app_token=app_token, table_id=table_id, view_id=view_id)

    async def read(
        self,
        url: str,
        *,
        rows: Union[int, None] = None,
        field_names: Union[List[str], None] = None,
        return_raw: bool = False,
        timezone: Union[str, None] = "Asia/Shanghai",
        timeout: Union[httpx.Timeout, None] = None,
    ) -> Union[dict, pd.DataFrame]:
        """从多维表格中读取数据

        Args:
            url (str): 多维表格分享链接
            rows (Union[int, None], optional): 读取的行数. Defaults to None.
            field_names (Union[List[str], None], optional): 读取的列名. Defaults to None.
            raw (bool, optional): 是否返回原始数据. Defaults to False.
            timezone (Union[str, None], optional): 时区，仅在raw=False时有效. Defaults to "Asia/Shanghai".

        Returns:
            Union[dict, pd.DataFrame]: 当raw=True时返回原始数据，否则返回DataFrame\
                返回的 dataframe 的 index 为对应记录的 record id
        """
        info = await self.get_bitable_info(url)

        items: List[RecordResponseData] = []
        has_more: bool = True
        page_token: str = None
        if rows is None or rows > self.record.MAX_RECORDS_PER_REQUEST:
            page_size = self.record.MAX_RECORDS_PER_REQUEST
        else:
            page_size = rows

        def is_continue():
            return has_more and (rows is None or len(items) < rows)

        fields = (
            await self.field.list(app_token=info.app_token, table_id=info.table_id)
        ).data.items
        if field_names is not None:
            fields = [field for field in fields if field.field_name in field_names]
        while is_continue():
            response = await self.record.search(
                app_token=info.app_token,
                table_id=info.table_id,
                view_id=info.view_id,
                field_names=field_names,
                page_token=page_token,
                page_size=page_size,
                timeout=timeout,
            )
            has_more = response.data.has_more
            page_token = response.data.page_token
            items.extend(response.data.items)

        items = items[:rows] if rows else items
        if return_raw:
            return {"items": items, "fields": fields}
        else:
            return fields_records_to_dataframe(fields, items, timezone=timezone)

    async def append(
        self,
        url: str,
        *,
        data: pd.DataFrame,
        timezone: Union[str, None] = "Asia/Shanghai",
        timeout: Union[httpx.Timeout, None] = None,
    ) -> List[RecordResponseData]:
        """向多维表格中追加数据

        Args:
            url (str): 多维表格分享链接
            data (pd.DataFrame): 要追加的数据
            timezone (Union[str, None], optional): 时区. Defaults to "Asia/Shanghai".
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            List[RecordResponseData]: 追加的数据
        """
        info = await self.get_bitable_info(url)
        records = dataframe_to_records(data, timezone=timezone)
        response_records: List[RecordResponseData] = []
        for i in range(0, len(records), self.record.MAX_RECORDS_PER_REQUEST):
            response = await self.record.batch_create(
                app_token=info.app_token,
                table_id=info.table_id,
                records=records[i : i + self.record.MAX_RECORDS_PER_REQUEST],
                timeout=timeout,
            )
            response_records.extend(response.data.records)
        return response_records

    async def update(
        self,
        url: str,
        *,
        data: pd.DataFrame,
        timezone: Union[str, None] = "Asia/Shanghai",
        timeout: Union[httpx.Timeout, None] = None,
    ):
        """更新多维表格中的数据

        Args:
            url (str): 多维表格分享链接
            data (pd.DataFrame): 要更新的数据，index 为更新记录的 record id
            timezone (Union[str, None], optional): 时区. Defaults to "Asia/Shanghai".
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            List[RecordResponseData]: 更新的数据
        """
        info = await self.get_bitable_info(url)
        records = dataframe_to_records(data, timezone=timezone, use_index_as_record_id=True)
        response_records: List[RecordResponseData] = []
        for i in range(0, len(records), self.record.MAX_RECORDS_PER_REQUEST):
            response = await self.record.batch_update(
                app_token=info.app_token,
                table_id=info.table_id,
                records=records[i : i + self.record.MAX_RECORDS_PER_REQUEST],
                timeout=timeout,
            )
            response_records.extend(response.data.records)
        return response_records

    async def delete(
        self, url: str, *, record_ids: List[str], timeout: Union[httpx.Timeout, None] = None
    ) -> None:
        """删除多维表格中的数据

        Args:
            url (str): 多维表格分享链接
            record_ids (List[str]): 要删除的记录ID
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.
        """
        info = await self.get_bitable_info(url)
        delete_response = []
        for i in range(0, len(record_ids), self.record.MAX_RECORDS_PER_REQUEST):
            response = await self.record.batch_delete(
                app_token=info.app_token,
                table_id=info.table_id,
                record_ids=record_ids[i : i + self.record.MAX_RECORDS_PER_REQUEST],
                timeout=timeout,
            )
            delete_response.extend(response.data.records)
        return delete_response
