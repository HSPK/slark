import re
from typing import Union, List

import pandas as pd
from loguru import logger
from pydantic import BaseModel
from typing_extensions import Literal

from slark._constants import DEFAULT_WRITE_COL_BATCH_SIZE, DEFAULT_WRITE_ROW_BATCH_SIZE
from slark.resources._resources import AsyncAPIResource
from slark.types import CellTypes, Range
from slark.types._utils import cached_property
from slark.utils import dataframe_to_values, values_to_dataframe

from .data import AsyncData
from .table import AsyncTable
from .worksheet import AsyncWorksheet


class SheetInfo(BaseModel):
    spreadsheet_token: str
    sheet_id: str
    sheet_range: Range


class AsyncSpreadsheets(AsyncAPIResource):
    @cached_property
    def table(self):
        return AsyncTable(client=self._client)

    @cached_property
    def worksheet(self):
        return AsyncWorksheet(client=self._client)

    @cached_property
    def data(self):
        return AsyncData(client=self._client)

    async def get_sheet_info(self, url: str):
        if "/sheets/" in url:
            spreadsheet_token, sheet_id = re.findall(
                r"\/sheets\/([^\/\?]+)(?:\?sheet=([^\/]+))?", url
            )[0]
        elif "/wiki/" in url:
            wiki_token, sheet_id = re.findall(
                r"\/wiki\/([^\/\?]+)(?:\?sheet=([^\/]+))?", url
            )[0]
            node_info = (
                await self._client.knowledge_space.nodes.get_node_info(wiki_token)
            ).data.node
            if node_info.obj_type != "sheet":
                raise ValueError("The node is not a sheet")
            spreadsheet_token = node_info.obj_token
        assert spreadsheet_token, "Sheet token is not found"
        if not sheet_id:
            info = (
                await self.worksheet.get_all_worksheets_info(spreadsheet_token)
            ).data.sheets[0]
            sheet_id = info.sheet_id

        else:
            info = (
                await self.worksheet.get_worksheet_info(
                    spreadsheet_token, sheet_id=sheet_id
                )
            ).data.sheet
        sheet_range = Range(
            rows=info.grid_properties.row_count,
            cols=info.grid_properties.column_count,
            sheet_id=sheet_id,
        )
        return SheetInfo(
            spreadsheet_token=spreadsheet_token,
            sheet_id=sheet_id,
            sheet_range=sheet_range,
        )

    async def read(
        self,
        url: str,
        *,
        start_row: int = 0,
        start_col: int = 0,
        rows: Union[int, None] = None,
        cols: Union[int, None] = None,
        has_header: bool = True,
        dropna: bool = True,
    ) -> pd.DataFrame:
        """从电子表格读取数据

        Args:
            url (str): 电子表格的 URL 链接
            start_row (int, optional): 起始行数. Defaults to 0.
            start_col (int, optional): 起始列数. Defaults to 0.
            rows (Union[int, None], optional): 读取行数. Defaults to None.
            cols (Union[int, None], optional): 读取列数. Defaults to None.
            has_header (bool, optional): 是否包括标题. Defaults to True.
            dropna (bool, optional): 是否去除全为空的行/列. Defaults to True.

        Returns:
            pd.DataFrame: 读取的数据
        """
        info = await self.get_sheet_info(url)
        read_range = info.sheet_range.intersect(
            Range(
                start_row=start_row,
                start_col=start_col,
                rows=rows or info.sheet_range.rows,
                cols=cols or info.sheet_range.cols,
                sheet_id=info.sheet_id,
            )
        )
        data = await self.data.read_single_range_data(
            info.spreadsheet_token, range=read_range.excel
        )
        return values_to_dataframe(
            data.data.valueRange.values, has_header=has_header, dropna=dropna
        )

    async def _write_batch(
        self,
        spreadsheet_token: str,
        write_range: Range,
        values: List[List[CellTypes]],
        mode: Literal["overwrite", "append", "prepend"],
        row_batch_size: int = DEFAULT_WRITE_ROW_BATCH_SIZE,
        col_batch_size: int = DEFAULT_WRITE_COL_BATCH_SIZE,
    ):
        def batch_range_values():
            for start_row in range(0, write_range.rows, row_batch_size):
                for start_col in range(0, write_range.cols, col_batch_size):
                    rows = min(row_batch_size, write_range.rows - start_row)
                    cols = min(col_batch_size, write_range.cols - start_col)
                    yield (
                        Range(
                            start_row=write_range.start_row + start_row,
                            start_col=write_range.start_col + start_col,
                            rows=rows,
                            cols=cols,
                            sheet_id=write_range.sheet_id,
                        ),
                        [
                            row[start_col : start_col + cols]
                            for row in values[start_row : start_row + rows]
                        ],
                    )

        for range_, values_ in batch_range_values():
            write_kwargs = {
                "spreadsheet_token": spreadsheet_token,
                "range": range_.excel,
                "values": values_,
            }
            logger.debug(f"Writing data with mode {mode}, range {range_.excel}")
            if mode == "overwrite":
                res = await self.data.write_single_range_data(**write_kwargs)
            elif mode == "append":
                res = await self.data.append_data(**write_kwargs)
            elif mode == "prepend":
                res = await self.data.prepend_data(**write_kwargs)
            else:
                raise ValueError(f"Invalid mode {mode}")
        return res

    async def _write(
        self,
        url: str,
        *,
        data: pd.DataFrame,
        start_row: int = 0,
        start_col: int = 0,
        has_header: bool = True,
        mode: Literal["overwrite", "append", "prepend"] = "overwrite",
    ):
        write_cols = data.shape[1]
        values = dataframe_to_values(data, has_header=has_header)
        write_rows = len(values)

        info = await self.get_sheet_info(url)
        write_range = Range(
            start_row=start_row,
            start_col=start_col,
            rows=write_rows,
            cols=write_cols,
            sheet_id=info.sheet_id,
        )

        logger.debug(f"Writing data to {url} with mode {mode}, range {write_range}")
        return await self._write_batch(
            info.spreadsheet_token, write_range, values, mode=mode
        )

    async def write(
        self,
        url: str,
        *,
        data: pd.DataFrame,
        start_row: int = 0,
        start_col: int = 0,
        has_header: bool = True,
    ):
        return await self._write(
            url,
            data=data,
            start_row=start_row,
            start_col=start_col,
            has_header=has_header,
            mode="overwrite",
        )

    async def append(
        self,
        url: str,
        *,
        data: pd.DataFrame,
        start_row: int = 0,
        start_col: int = 0,
    ):
        return await self._write(
            url,
            data=data,
            start_row=start_row,
            start_col=start_col,
            has_header=False,
            mode="append",
        )

    async def prepend(
        self,
        url: str,
        *,
        data: pd.DataFrame,
        start_row: int = 0,
        start_col: int = 0,
    ):
        return await self._write(
            url,
            data=data,
            start_row=start_row,
            start_col=start_col,
            has_header=False,
            mode="prepend",
        )
