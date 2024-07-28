from slark.types.response import BaseResponse
from typing import Literal
from pydantic import BaseModel


class GetSpreadsheetInfoResponseDataSpreadsheet(BaseModel):
    title: str
    """电子表格标题"""
    owner_id: str
    """电子表格的所有者 ID。ID 类型由查询参数 user_id_type 决定。"""
    token: str
    """电子表格 token"""
    url: str
    """电子表格的 URL 链接"""


class GetSpreadsheetInfoResponseData(BaseModel):
    spreadsheet: GetSpreadsheetInfoResponseDataSpreadsheet


class GetSpreadsheetInfoResponse(BaseResponse):
    data: GetSpreadsheetInfoResponseData


class WorksheetGridProperties(BaseModel):
    frozen_row_count: int
    frozen_column_count: int
    row_count: int
    column_count: int


class WorksheetMerge(BaseModel):
    start_row_index: int
    end_row_index: int
    start_column_index: int
    end_column_index: int


class GetAllWorksheetsInfoResponseDataWorksheet(BaseModel):
    sheet_id: str
    """工作表 ID"""
    title: str
    """	工作表标题"""
    index: int
    """工作表索引位置，索引从 0 开始计数。"""
    hidden: bool
    """工作表是否被隐藏"""
    grid_properties: WorksheetGridProperties | None = None
    """单元格属性，仅当 resource_type 为 sheet 即工作表类型为电子表格时返回。"""
    resource_type: Literal["sheet", "bitable", "#UNSUPPORTED_TYPE"]
    """工作表类型，sheet 为工作表，bitable 为多维表格，#UNSUPPORTED_TYPE 为不支持的类型。"""
    merges: list[WorksheetMerge] | None = None
    """合并单元格的相关信息。没有合并单元格则不返回。"""


class GetAllWorksheetsInfoResponseData(BaseModel):
    sheets: list[GetAllWorksheetsInfoResponseDataWorksheet]


class GetAllWorksheetsInfoResponse(BaseResponse):
    data: GetAllWorksheetsInfoResponseData
