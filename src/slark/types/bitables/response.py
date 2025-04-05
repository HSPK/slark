from slark.types._common import BaseModel
from slark.types.response import BaseResponse


class BitableMeta(BaseModel):
    app_token: str
    """多维表格的 app_token"""
    name: str
    """多维表格的名字"""
    revision: int
    """多维表格的版本号（对多维表格进行修改时更新，如新增、删除数据表，修改数据表名等，初始为1，每次更新+1）"""
    is_advanced: bool
    """多维表格是否开启了高级权限。取值包括：
    true：表示开启了高级权限
    false：表示关闭了高级权限"""
    time_zone: str
    """文档时区"""


class UpdateBitableMeta(BaseModel):
    app_token: str


class UpdateBitableMetaResponseData(BaseModel):
    app: UpdateBitableMeta


class GetBitableMetaResponseData(BaseModel):
    app: BitableMeta


class GetBitableMetaResponse(BaseResponse):
    data: GetBitableMetaResponseData


class UpdateBitableMetaResponse(BaseResponse):
    data: UpdateBitableMetaResponseData
