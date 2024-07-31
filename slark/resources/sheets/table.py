from typing import Union

import httpx
from typing_extensions import Literal

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.spreadsheets import GetSpreadsheetInfoResponse


class AsyncTable(AsyncAPIResource):
    async def get_spreadsheet_info(
        self,
        sheet_token: str,
        *,
        user_id_type: Literal["open_id", "union_id", "user_id"] = "open_id",
        timeout: Union[httpx.Timeout, None] = None,
    ) -> GetSpreadsheetInfoResponse:
        """根据电子表格 token 获取电子表格的基础信息，包括电子表格的所有者、URL 链接等。
        https://open.feishu.cn/document/server-docs/docs/sheets-v3/spreadsheet/get
        Args:
            sheet_token (str): 电子表格的 token。
            user_id_type (Literal[&quot;open_id&quot;, &quot;union_id&quot;, &quot;user_id&quot;], optional): 用户 ID 类型
                示例值："open_id"
                可选值有：
                open_id：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。
                union_id：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。
                user_id：标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。
                默认值：open_id。当值为 user_id，字段权限要求：获取用户 user ID.

        Returns:
            GetSpreadsheetInfoResponse: 电子表格的基础信息
        """
        return await self._get(
            API_PATH.spreadsheets.get_spreadsheet_info.format(spreadsheet_token=sheet_token),
            cast_to=GetSpreadsheetInfoResponse,
            options={"timeout": timeout, "params": {"user_id_type": user_id_type}},
        )
