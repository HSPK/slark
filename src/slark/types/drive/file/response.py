from pydantic import BaseModel

from slark.types.response import BaseResponse


class FileInfo(BaseModel):
    file_path: str
    file_token: str
    file_name: str
    mime_type: str
    

class FileDownloadResponse(BaseResponse):
    data: FileInfo