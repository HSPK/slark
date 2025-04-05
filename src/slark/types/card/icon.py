from typing import Union

from .base import BaseElement
from .color import Color
from .ud_icon import UDIconToken


class IconElement(BaseElement):
    tag: str = "standard_icon"
    """图标类型的标签。可取值：

    standard_icon：使用图标库中的图标。
    custom_icon：使用用自定义图片作为图标。"""

    token: Union[UDIconToken, None] = None
    """图标库中图标的 token。当 tag 为 standard_icon 时生效。枚举值参见图标库。"""

    color: Union[Color, None] = None
    """图标的颜色。支持设置线性和面性图标（即 token 末尾为 outlined 或 filled 的图标）的颜色。当 tag 为 standard_icon 时生效。枚举值参见颜色枚举值。"""

    img_key: Union[str, None] = None
    """自定义前缀图标的图片 key。当 tag 为 custom_icon 时生效。

    图标 key 的获取方式：调用上传图片接口，上传用于发送消息的图片，并在返回值中获取图片的 image_key。"""
