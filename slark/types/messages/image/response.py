from slark.types._common import BaseModel
from slark.types.response.base import BaseResponse


class UploadImageData(BaseModel):
    image_key: str
    """图片key，用于后续获取图片信息"""


class UploadImageResponse(BaseResponse):
    data: UploadImageData
