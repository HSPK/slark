from pydantic import BaseModel

from slark.types.response import BaseResponse


class DocumentDisplaySetting(BaseModel):
    show_authors: bool
    """文档信息中是否展示文档作者"""
    show_create_time: bool
    """文档信息中是否展示文档创建时间"""
    show_pv: bool
    """文档信息中是否展示文档访问次数"""
    show_uv: bool
    """文档信息中是否展示文档访问人数"""
    show_like_count: bool
    """文档信息中是否展示点赞总数"""
    show_comment_count: bool
    """文档信息中是否展示评论总数"""
    show_related_matters: bool
    """文档信息中是否展示关联事项。暂未支持"""


class DocumentCover(BaseModel):
    token: str
    offset_ratio_x: float
    offset_ratio_y: float


class DocumentInfo(BaseModel):
    document_id: str
    """文档的唯一标识。"""
    revision_id: int
    """文档版本 ID。起始值为 1"""
    title: str
    """文档标题"""
    display_setting: DocumentDisplaySetting
    """文档展示设置"""
    cover: DocumentCover
    """文档封面"""


class DocumentResponseData(BaseModel):
    document: DocumentInfo


class DocumentResponse(BaseResponse):
    data: DocumentResponseData


class GetRawContentResponseData(BaseModel):
    content: str
    """文档纯文本"""


class GetRawContentResponse(BaseResponse):
    data: GetRawContentResponseData
