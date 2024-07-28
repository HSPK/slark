from pydantic import BaseModel, ConfigDict
from typing import Any


class BaseResponse(BaseModel):
    code: int
    """错误码，非 0 表示失败"""
    msg: str
    """错误描述"""
    data: Any | None = None
    """返回数据"""
    error: Any | None = None
    """错误信息"""

    model_config = ConfigDict(extra="allow")
