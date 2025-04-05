from typing import List

from slark.types._common import BaseModel
from slark.types.response import BaseResponse

from .common import CellTypes


class PrependDataResponseDataUpdates(BaseModel):
    spreadsheetToken: str
    """电子表格的 token"""
    updatedRange: str
    """插入数据的范围"""
    updatedRows: int
    """更新的行总数"""
    updatedColumns: int
    """更新的列总数"""
    updatedCells: int
    """更新的单元格总数"""
    revision: int
    """工作表的版本号。从 0 开始计数，更新一次版本号加一。"""


class PrependDataResponseData(BaseModel):
    spreadsheetToken: str
    """电子表格的 token"""
    tableRange: str
    """插入数据的范围"""
    revision: int
    """	工作表的版本号。从 0 开始计数，更新一次版本号加一。"""
    updates: PrependDataResponseDataUpdates
    """插入数据的范围、更新的行列总数等"""


class PrependDataResponse(BaseResponse):
    data: PrependDataResponseData


class AppendDataResponse(PrependDataResponse):
    pass


class ReadDataValueRange(BaseModel):
    majorDimension: str = "ROWS"
    """返回的 values 数组中数据的呈现维度。固定取值 ROWS，即数据为从左到右、从上到下的读取顺序。"""
    range: str
    """读取的范围。为空时表示查询范围没有数据。"""
    revision: int
    """工作表的版本号。从 0 开始计数，更新一次版本号加一。"""
    values: List[List[CellTypes]]
    """指定范围中的数据"""


class ReadSingleRangeResponseData(BaseModel):
    revision: int
    spreadsheetToken: str
    valueRange: ReadDataValueRange


class ReadSingleRangeResponse(BaseResponse):
    data: ReadSingleRangeResponseData


class ReadMultiRangeResponseData(BaseModel):
    revision: int
    spreadsheetToken: str
    valueRanges: List[ReadDataValueRange]


class ReadMultiRangeResponse(BaseResponse):
    data: ReadMultiRangeResponseData


class WriteSingleRangeResponseData(PrependDataResponseDataUpdates):
    pass


class WriteSingleRangeResponse(BaseResponse):
    data: WriteSingleRangeResponseData


class WriteMultiRangeResponseDataResponse(BaseModel):
    spreadsheetToken: str
    updatedRange: str
    updatedRows: str
    updatedColumns: str
    updatedCells: str


class WriteMultiRangeResponseData(BaseModel):
    revision: int
    spreadsheetToken: str
    responses: List[WriteMultiRangeResponseDataResponse]


class WriteMultiRangeResponse(BaseResponse):
    data: WriteMultiRangeResponseData
