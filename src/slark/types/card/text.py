import enum

from .base import BaseModel


class PlainText(BaseModel):
    tag: str = "plain_text"
    content: str
    """文本的内容，最多支持 100 个字符。"""


class TextSize(enum.Enum):
    HEADING_0 = "heading-0"
    """特大标题（30px）"""
    HEADING_1 = "heading-1"
    """一级标题（24px）"""
    HEADING_2 = "heading-2"
    """二级标题（20 px）"""
    HEADING_3 = "heading-3"
    """三级标题（18px）"""
    HEADING_4 = "heading-4"
    """四级标题（16px）"""
    HEADING = "heading"
    """标题（16px）"""
    NORMAL = "normal"
    """正文（14px）"""
    NOTATION = "notation"
    """辅助信息（12px）"""
    XXXX_LARGE = "xxxx-large"
    """30px"""
    XXX_LARGE = "xxx-large"
    """24px"""
    XX_LARGE = "xx-large"
    """20px"""
    X_LARGE = "x-large"
    """18px"""
    LARGE = "large"
    """16px"""
    MEDIUM = "medium"
    """14px"""
    SMALL = "small"
    """12px"""
    X_SMALL = "x-small"
    """10px"""