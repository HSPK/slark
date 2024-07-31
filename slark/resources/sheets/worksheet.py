from typing import Union

import httpx

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.spreadsheets import (
    GetAllWorksheetsInfoResponse,
    GetWorksheetInfoResponse,
)


class AsyncWorksheet(AsyncAPIResource):
    async def get_all_worksheets_info(
        self,
        sheet_token: str,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> GetAllWorksheetsInfoResponse:
        """根据电子表格 token 获取表格中所有工作表及其属性信息，包括工作表 ID、标题、索引位置、是否被隐藏等。
        https://open.feishu.cn/document/server-docs/docs/sheets-v3/spreadsheet-sheet/query

        Args:
            sheet_token (str): 	电子表格的 token。
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            GetAllWorksheetsInfoResponse: 所有工作表信息。
        """
        return await self._get(
            API_PATH.spreadsheets.get_all_worksheets.format(spreadsheet_token=sheet_token),
            cast_to=GetAllWorksheetsInfoResponse,
            options={"timeout": timeout},
        )

    async def get_worksheet_info(
        self,
        sheet_token: str,
        *,
        sheet_id: str,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> GetWorksheetInfoResponse:
        return await self._get(
            API_PATH.spreadsheets.get_worksheet_info.format(
                spreadsheet_token=sheet_token, sheet_id=sheet_id
            ),
            options={"timeout": timeout},
            cast_to=GetWorksheetInfoResponse,
        )
