from typing import List, Union

import httpx
from typing_extensions import Literal

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH as path
from slark.types.spreadsheets import data


class AsyncData(AsyncAPIResource):
    async def prepend_data(
        self,
        spreadsheet_token: str,
        *,
        range: str,
        values: List[List[data.CellTypes]],
        timeout: Union[httpx.Timeout, None] = None,
    ) -> data.PrependDataResponse:
        return await self._post(
            path.spreadsheets.data.prepend_data.format(spreadsheetToken=spreadsheet_token),
            body=data.PrependDataBody(
                valueRange=data.WriteDataValueRange(range=range, values=values)
            ).model_dump(),
            cast_to=data.PrependDataResponse,
            options={"timeout": timeout},
        )

    async def append_data(
        self,
        spreadsheet_token: str,
        *,
        insertDataOption: Literal["OVERWRITE", "INSERT_ROWS"] = "OVERWRITE",
        range: str,
        values: List[List[data.CellTypes]],
        timeout: Union[httpx.Timeout, None] = None,
    ) -> data.AppendDataResponse:
        """在电子表格工作表的指定范围中，在空白位置中追加数据。例如，若指定范围参数 range 为 6e5ed3!A1:B2，该接口将会依次寻找 A1、A2、A3...单元格，在找到的第一个空白位置中写入数据。

            使用限制
            单次写入范围不可超过 5,000 行、100 列。
            每个单元格不超过 50,000 字符，由于服务端会增加控制字符，因此推荐每个单元格不超过 40,000 字符。


        Args:
            spreadsheet_token (str): 电子表格的 token
            range (str): 追加数据的范围。格式为 <sheetId>!<开始位置>:<结束位置>
            values (List[List[data.CellTypes]]): 追加的数据

            insertDataOption (Literal[&quot;OVERWRITE&quot;, &quot;INSERT_ROWS&quot;], optional):
            指定追加数据的方式，默认值为 OVERWRITE，即若空行数量小于追加数据的行数，则会覆盖已有数据。可选值：

            OVERWRITE：若空行的数量小于追加数据的行数，则会覆盖已有数据
            INSERT_ROWS：插入足够数量的行后再进行数据追加. Defaults to "OVERWRITE".

            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            AppendDataResponse: AppendDataResponse
        """
        return await self._post(
            path.spreadsheets.data.append_data.format(spreadsheetToken=spreadsheet_token),
            body=data.AppendDataBody(
                valueRange=data.WriteDataValueRange(range=range, values=values)
            ).model_dump(),
            cast_to=data.AppendDataResponse,
            options={
                "timeout": timeout,
                "params": data.AppendDataParams(insertDataOption=insertDataOption).model_dump(),
            },
        )

    async def write_single_range_data(
        self,
        spreadsheet_token: str,
        *,
        range: str,
        values: List[List[data.CellTypes]],
        timeout: Union[httpx.Timeout, None] = None,
    ) -> data.WriteSingleRangeResponse:
        """向电子表格某个工作表的单个指定范围中写入数据。若指定范围已内有数据，将被新写入的数据覆盖。

            使用限制
            单次写入数据不得超过 5000 行、100列。
            每个单元格不超过 50,000 字符，由于服务端会增加控制字符，因此推荐每个单元格不超过 40,000 字符。

        Args:
            spreadsheet_token (str): _description_
            range (str): 写入数据的范围。格式为 <sheetId>!<开始位置>:<结束位置>。其中：

            sheetId 为工作表 ID，通过获取工作表 获取。

            <开始位置>:<结束位置> 为工作表中单元格的范围，数字表示行索引，字母表示列索引。如 A2:B2 表示该工作表第 2 行的 A 列到 B 列。range支持四种写法，详情参考电子表格概述。

            注意：range 所指定的范围需要大于等于写入的数据所占用的范围。
            values (List[List[data.CellTypes]]): 写入的数据。如要写入公式、超链接、email、@人等，可参考电子表格支持写入的数据类型。
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            WriteSingleRangeResponse: WriteSingleRangeResponse
        """
        return await self._put(
            path.spreadsheets.data.write_single_range_data.format(
                spreadsheetToken=spreadsheet_token
            ),
            body=data.WriteSingleRangeBody(
                valueRange=data.WriteDataValueRange(range=range, values=values)
            ).model_dump(),
            cast_to=data.WriteSingleRangeResponse,
            options={"timeout": timeout},
        )

    async def write_multi_range_data(
        self,
        spreadsheet_token: str,
        *,
        value_ranges: List[data.WriteDataValueRange],
        timeout: Union[httpx.Timeout, None] = None,
    ) -> data.WriteMultiRangeResponse:
        return await self._post(
            path.spreadsheets.data.write_multi_range_data.format(
                spreadsheetToken=spreadsheet_token
            ),
            body=data.WriteMultiRangeBody(valueRanges=value_ranges).model_dump(),
            cast_to=data.WriteMultiRangeResponse,
            options={"timeout": timeout},
        )

    async def read_single_range_data(
        self,
        spreadsheet_token: str,
        *,
        range: str,
        valueRenderOption: Union[
            Literal["ToString", "Formula", "FormattedValue", "UnformattedValue"], None
        ] = None,
        dateTimeRenderOption: Union[Literal["FormattedString"], None] = None,
        user_id_type: Union[Literal["open_id", "union_id"], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> data.ReadSingleRangeResponse:
        """读取电子表格中单个指定范围的数据。

        使用限制
        该接口返回数据的最大限制为 10 MB。
        该接口不支持获取跨表引用和数组公式的计算结果。

        Args:
            spreadsheet_token (str): 电子表格的 token
            range (str): 查询范围。格式为 `<sheetId>!<开始位置>:<结束位置>`

            valueRenderOption (Literal[ &quot;ToString&quot;, &quot;Formula&quot;, &quot;FormattedValue&quot;, &quot;UnformattedValue&quot; ], None, optional): 指定单元格数据的格式。可选值如下所示。当参数缺省时，默认不进行公式计算，返回公式本身，且单元格为数值格式。
            ToString：返回纯文本的值（数值类型除外）
            Formula：单元格中含有公式时，返回公式本身
            FormattedValue：计算并格式化单元格
            UnformattedValue：计算但不对单元格进行格式化. Defaults to None.

            dateTimeRenderOption (Literal[&quot;FormattedString&quot;], None, optional):
            指定数据类型为日期、时间、或时间日期的单元格数据的格式。
            若不传值，默认返回浮点数值，整数部分为自 1899 年 12 月 30 日以来的天数；小数部分为该时间占 24 小时的份额。例如：若时间为 1900 年 1 月 1 日中午 12 点，则默认返回 2.5。其中，2 表示 1900 年 1 月 1 日为 1899 年12 月 30 日之后的 2 天；0.5 表示 12 点占 24 小时的二分之一，即 12/24=0.5。
            可选值为 FormattedString，此时接口将计算并对日期、时间、或时间日期类型的数据格式化并返回格式化后的字符串，但不会对数字进行格式化。. Defaults to None.

            user_id_type (Literal[&quot;open_id&quot;, &quot;union_id&quot;], None, optional):
            当单元格中包含@用户等涉及用户信息的元素时，该参数可指定返回的用户 ID 类型。默认为 lark_id，建议选择 open_id 或 union_id. Defaults to None.

            timeout (Union[httpx.Timeout, None], optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return await self._get(
            path.spreadsheets.data.read_single_range_data.format(
                spreadsheetToken=spreadsheet_token, range=range
            ),
            cast_to=data.ReadSingleRangeResponse,
            options={
                "params": data.ReadSingleRangeParams(
                    valueRenderOption=valueRenderOption,
                    dateTimeRenderOption=dateTimeRenderOption,
                    user_id_type=user_id_type,
                ).model_dump(),
                "timeout": timeout,
            },
        )

    async def read_multi_range_data(
        self,
        spreadsheet_token: str,
        *,
        ranges: str,
        valueRenderOption: Union[
            Literal["ToString", "Formula", "FormattedValue", "UnformattedValue"], None
        ] = None,
        dateTimeRenderOption: Union[Literal["FormattedString"], None] = None,
        user_id_type: Union[Literal["open_id", "union_id"], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> data.ReadMultiRangeResponse:
        return await self._get(
            path.spreadsheets.data.read_multi_range_data.format(spreadsheetToken=spreadsheet_token),
            cast_to=data.ReadMultiRangeResponse,
            options={
                "params": data.ReadMultiRangeParams(
                    ranges=ranges,
                    valueRenderOption=valueRenderOption,
                    dateTimeRenderOption=dateTimeRenderOption,
                    user_id_type=user_id_type,
                ).model_dump(),
                "timeout": timeout,
            },
        )
