from typing import List, Union

from typing_extensions import Literal

from slark.types._common import BaseModel

from .common import CellTypes


class WriteDataValueRange(BaseModel):
    range: str
    """	写入数据的范围。格式为 <sheetId>!<开始位置>:<结束位置>。其中：

    sheetId 为工作表 ID，通过获取工作表 获取。

    <开始位置>:<结束位置> 为工作表中单元格的范围，数字表示行索引，字母表示列索引。如 A2:B2 表示该工作表第 2 行的 A 列到 B 列。range支持四种写法，详情参考电子表格概述。

    注意：range 所指定的范围需要大于等于写入的数据所占用的范围。"""
    values: List[List[CellTypes]]


class PrependDataBody(BaseModel):
    """指定工作表中的范围和在该范围中插入的数据。"""

    valueRange: WriteDataValueRange


class AppendDataBody(PrependDataBody):
    pass


class AppendDataParams(BaseModel):
    insertDataOption: Literal["OVERWRITE", "INSERT_ROWS"] = "OVERWRITE"
    """指定追加数据的方式，默认值为 OVERWRITE，即若空行数量小于追加数据的行数，则会覆盖已有数据。可选值：

    OVERWRITE：若空行的数量小于追加数据的行数，则会覆盖已有数据
    INSERT_ROWS：插入足够数量的行后再进行数据追加"""


class ReadSingleRangeParams(BaseModel):
    valueRenderOption: Union[str, None] = None
    """指定单元格数据的格式。可选值如下所示。当参数缺省时，默认不进行公式计算，返回公式本身，且单元格为数值格式。

    ToString：返回纯文本的值（数值类型除外）
    Formula：单元格中含有公式时，返回公式本身
    FormattedValue：计算并格式化单元格
    UnformattedValue：计算但不对单元格进行格式化"""

    dateTimeRenderOption: Union[str, None] = None
    """指定数据类型为日期、时间、或时间日期的单元格数据的格式。

    若不传值，默认返回浮点数值，整数部分为自 1899 年 12 月 30 日以来的天数；小数部分为该时间占 24 小时的份额。例如：若时间为 1900 年 1 月 1 日中午 12 点，则默认返回 2.5。其中，2 表示 1900 年 1 月 1 日为 1899 年12 月 30 日之后的 2 天；0.5 表示 12 点占 24 小时的二分之一，即 12/24=0.5。
    可选值为 FormattedString，此时接口将计算并对日期、时间、或时间日期类型的数据格式化并返回格式化后的字符串，但不会对数字进行格式化。"""

    user_id_type: Union[str, None] = None
    """当单元格中包含@用户等涉及用户信息的元素时，该参数可指定返回的用户 ID 类型。默认为 lark_id，建议选择 open_id 或 union_id。了解更多，参考用户身份概述。可选值：
    open_id：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。了解更多：如何获取 Open ID
    union_id：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。了解更多：如何获取 Union ID"""


class ReadMultiRangeParams(BaseModel):
    ranges: str
    """多个查询范围，范围之间使用逗号分隔，如 Q7PlXT!A2:B6,0b6377!B1:C8。range 的格式为 <sheetId>!<开始位置>:<结束位置>。其中：

    sheetId 为工作表 ID，通过 [获取工作表](https://open.feishu.cn/document/server-docs/docs/sheets-v3/spreadsheet-sheet/query) 获取
    <开始位置>:<结束位置> 为工作表中单元格的范围，数字表示行索引，字母表示列索引。如 A2:B2 表示该工作表第 2 行的 A 列到 B 列。
    range支持四种写法，详情参考[电子表格概述](https://open.feishu.cn/document/server-docs/docs/sheets-v3/overview)
    注意：若使用 <sheetId>!<开始单元格>:<结束列> 的写法时，仅支持获取 100 列数据。"""
    valueRenderOption: Union[str, None] = None
    """指定单元格数据的格式。可选值如下所示。当参数缺省时，默认不进行公式计算，返回公式本身，且单元格为数值格式。

    ToString：返回纯文本的值（数值类型除外）
    Formula：单元格中含有公式时，返回公式本身
    FormattedValue：计算并格式化单元格
    UnformattedValue：计算但不对单元格进行格式化"""

    dateTimeRenderOption: Union[str, None] = None
    """指定数据类型为日期、时间、或时间日期的单元格数据的格式。

    若不传值，默认返回浮点数值，整数部分为自 1899 年 12 月 30 日以来的天数；小数部分为该时间占 24 小时的份额。例如：若时间为 1900 年 1 月 1 日中午 12 点，则默认返回 2.5。其中，2 表示 1900 年 1 月 1 日为 1899 年12 月 30 日之后的 2 天；0.5 表示 12 点占 24 小时的二分之一，即 12/24=0.5。
    可选值为 FormattedString，此时接口将计算并对日期、时间、或时间日期类型的数据格式化并返回格式化后的字符串，但不会对数字进行格式化。"""

    user_id_type: Union[str, None] = None
    """当单元格中包含@用户等涉及用户信息的元素时，该参数可指定返回的用户 ID 类型。默认为 lark_id，建议选择 open_id 或 union_id。了解更多，参考用户身份概述。可选值：
    open_id：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。了解更多：如何获取 Open ID
    union_id：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以把同个用户在多个应用中的身份关联起来。了解更多：如何获取 Union ID"""


class WriteSingleRangeBody(BaseModel):
    valueRange: WriteDataValueRange


class WriteMultiRangeBody(BaseModel):
    valueRanges: List[WriteDataValueRange]
