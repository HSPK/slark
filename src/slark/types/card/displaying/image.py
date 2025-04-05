from typing import Union

from typing_extensions import Literal

from ..base import BaseElement


class ImageTextElement(BaseElement):
    tag: str = "plain_text"
    content: str


class ImageElement(BaseElement):
    tag: str = "img"
    img_key: str
    alt: ImageTextElement
    title: Union[ImageTextElement, None] = None
    corner_radius: Union[str, None] = None
    scale_type: Literal["crop_center", "crop_top", "fit_horizontal"] = "crop_center"
    """图片的裁剪模式，当 size 字段的比例和图片的比例不一致时会触发裁剪。可取值：

    crop_center：居中裁剪
    crop_top：顶部裁剪
    fit_horizontal：完整展示不裁剪"""

    size: Union[str, None] = None
    """图片尺寸。仅在 scale_type 字段为 crop_center 或 crop_top 时生效。可取值：

    large：大图，尺寸为 160 × 160，适用于多图混排。
    medium：中图，尺寸为 80 × 80，适用于图文混排的封面图。
    small：小图，尺寸为 40 × 40，适用于人员头像。
    tiny：超小图，尺寸为 16 × 16，适用于图标、备注。
    stretch：超大图，适用于高宽比小于 16:9 的图片。
    stretch_without_padding：通栏图，适用于高宽比小于 16:9 的图片，图片的宽度将撑满卡片宽度。
    注意： 卡片 JSON 2.0 结构不再支持 stretch_without_padding 属性。
    你可设置 margin 字段为负数实现通栏效果。如："margin": "4px -12px"。详情参考组件统一支持布局相关能力。
    [1,999]px [1,999]px：自定义图片尺寸，单位为像素，中间用空格分隔。"""

    transparent: bool = False
    """是否为透明底色。默认为 false，即图片为白色底色。"""

    preview: bool = True
    """点击后是否放大图片。

    true：点击图片后，弹出图片查看器放大查看当前点击的图片。
    false：点击图片后，响应卡片本身的交互事件，不弹出图片查看器。
    提示：如果你为卡片配置了跳转链接card_link参数，可将该参数设置为 false，
    后续用户点击卡片上的图片也能响应 card_link 链接跳转。"""