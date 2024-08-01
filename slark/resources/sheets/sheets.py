import re
from typing import List, Union

import httpx
import pandas as pd
from loguru import logger
from typing_extensions import Literal

from slark._constants import DEFAULT_WRITE_COL_BATCH_SIZE, DEFAULT_WRITE_ROW_BATCH_SIZE
from slark.resources._resources import AsyncAPIResource
from slark.types._common import BaseModel
from slark.types._utils import cached_property
from slark.types.spreadsheets.data import CellTypes, Range
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

    async def get_sheet_info(self, url: str) -> SheetInfo:
        if "/sheets/" in url:
            spreadsheet_token, sheet_id = re.findall(
                r"\/sheets\/([^\/\?]+)(?:\?sheet=([^\/]+))?", url
            )[0]
        elif "/wiki/" in url:
            wiki_token, sheet_id = re.findall(r"\/wiki\/([^\/\?]+)(?:\?sheet=([^\/]+))?", url)[0]
            node_info = (
                await self._client.knowledge_space.nodes.get_node_info(wiki_token)
            ).data.node
            if node_info.obj_type != "sheet":
                raise ValueError("The node is not a sheet")
            spreadsheet_token = node_info.obj_token
        assert spreadsheet_token, "Sheet token is not found"
        if not sheet_id:
            info = (await self.worksheet.get_all_worksheets_info(spreadsheet_token)).data.sheets[0]
            sheet_id = info.sheet_id

        else:
            info = (
                await self.worksheet.get_worksheet_info(spreadsheet_token, sheet_id=sheet_id)
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
        valueRenderOption: Union[
            Literal["ToString", "Formula", "FormattedValue", "UnformattedValue"], None
        ] = None,
        dateTimeRenderOption: Union[Literal["FormattedString"], None] = None,
        user_id_type: Union[Literal["open_id", "union_id"], None] = None,
        return_raw: bool = False,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> Union[pd.DataFrame, List[List[CellTypes]]]:
        """从电子表格读取数据，该接口返回数据的最大限制为 10 MB。该接口不支持获取跨表引用和数组公式的计算结果。

        Args:
            url (str): 电子表格的 URL 链接
            start_row (int, optional): 起始行数. Defaults to 0.
            start_col (int, optional): 起始列数. Defaults to 0.
            rows (Union[int, None], optional): 读取行数. Defaults to None.
            cols (Union[int, None], optional): 读取列数. Defaults to None.
            has_header (bool, optional): 是否包括标题. Defaults to True.
            dropna (bool, optional): 是否去除全为空的行/列. Defaults to True.
            valueRenderOption (Literal[ &quot;ToString&quot;, &quot;Formula&quot;, &quot;FormattedValue&quot;, &quot;UnformattedValue&quot; ], None, optional): \
                指定单元格数据的格式。可选值如下所示。\
                当参数缺省时，默认不进行公式计算，返回公式本身，且单元格为数值格式。\
                ToString：返回纯文本的值（数值类型除外）。\
                Formula：单元格中含有公式时，返回公式本身。\
                FormattedValue：计算并格式化单元格。\
                UnformattedValue：计算但不对单元格进行格式化. Defaults to None.
            dateTimeRenderOption (Literal[&quot;FormattedString&quot;], None, optional):\
                指定数据类型为日期、时间、或时间日期的单元格数据的格式。\
                若不传值，默认返回浮点数值，整数部分为自 1899 年 12 月 30 日以来的天数；\
                小数部分为该时间占 24 小时的份额。\
                例如：若时间为 1900 年 1 月 1 日中午 12 点，则默认返回 2.5。\
                其中，2 表示 1900 年 1 月 1 日为 1899 年12 月 30 日之后的 2 天；\
                0.5 表示 12 点占 24 小时的二分之一，即 12/24=0.5。\
                可选值为 FormattedString，此时接口将计算并对日期、时间、或时间日期类型的数据格式化并返回格式化后的字符串，但不会对数字进行格式化。. Defaults to None.
            user_id_type (Literal[&quot;open_id&quot;, &quot;union_id&quot;], None, optional):\
                当单元格中包含@用户等涉及用户信息的元素时，该参数可指定返回的用户 ID 类型。\
                默认为 lark_id，建议选择 open_id 或 union_id. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): _description_. Defaults to None.

        Returns:
            Union[pd.DataFrame, List[List[CellTypes]]]: 读取的数据，\
                如果 return_raw 为 True 则返回 List[List[CellTypes]]，否则返回 pd.DataFrame
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
            info.spreadsheet_token,
            range=read_range.excel,
            valueRenderOption=valueRenderOption,
            dateTimeRenderOption=dateTimeRenderOption,
            user_id_type=user_id_type,
            timeout=timeout,
        )
        if return_raw:
            return data.data.valueRange.values
        else:
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
        insertDataOption: Literal["OVERWRITE", "INSERT_ROWS"] = "OVERWRITE",
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
                res = await self.data.append_data(**write_kwargs, insertDataOption=insertDataOption)
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
        insertDataOption: Literal["OVERWRITE", "INSERT_ROWS"] = "OVERWRITE",
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
            info.spreadsheet_token,
            write_range,
            values,
            mode=mode,
            insertDataOption=insertDataOption,
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
        insertDataOption: Literal["OVERWRITE", "INSERT_ROWS"] = "OVERWRITE",
    ):
        return await self._write(
            url,
            data=data,
            start_row=start_row,
            start_col=start_col,
            has_header=False,
            mode="append",
            insertDataOption=insertDataOption,
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
