import enum
from typing import Dict, List, Union

from typing_extensions import Literal

from .._common import BaseModel
from .color import Color
from .header import CardHeader
from .ud_icon import UDIconColor, UDIconToken

"""飞书卡片文档链接 https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-json-structure"""


class BaseElement(BaseModel):
    tag: str


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


class PlainTextElement(BaseElement):
    tag: Literal["plain_text", "lark_md"] = "plain_text"
    """文本类型的标签。可取值：

    plain_text：普通文本内容
    lark_md：支持部分 Markdown 语法的文本内容。详情参考下文 lark_md 支持的 Markdown 语法
    注意：飞书卡片搭建工具中仅支持使用 plain_text 类型的普通文本组件。你可使用富文本组件添加 Markdown 格式的文本。"""

    content: str
    """文本内容。当 tag 为 lark_md 时，支持部分 Markdown 语法的文本内容。详情参考下文 lark_md 支持的 Markdown 语法。
    https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-components/content-components/plain-text#39ee4e65"""

    text_size: Union[TextSize, str, None] = TextSize.NORMAL.value
    """文本大小。可取值如下所示。如果你填写了其它值，卡片将展示为 normal 字段对应的字号。你也可分别为移动端和桌面端定义不同的字号，详细步骤参考下文 为移动端和桌面端定义不同的字号。"""
    text_align: Literal["left", "center", "right"] = "left"
    """文本对齐方式。可取值：

    left：左对齐
    center：居中对齐
    right：右对齐"""

    text_color: Union[str, Color] = "default"
    """文本的颜色。仅在 tag 为 plain_text 时生效。可取值：

    default：客户端浅色主题模式下为黑色；客户端深色主题模式下为白色"""

    lines: Union[int, None] = None
    """内容最大显示行数，超出设置行的内容用 ... 省略。"""


class IconElement(BaseElement):
    tag: str = "standard_icon"
    """图标类型的标签。可取值：

    standard_icon：使用图标库中的图标。
    custom_icon：使用用自定义图片作为图标。"""

    token: Union[UDIconToken, None] = None
    """图标库中图标的 token。当 tag 为 standard_icon 时生效。枚举值参见图标库。"""

    color: Union[UDIconColor, None] = None
    """图标的颜色。支持设置线性和面性图标（即 token 末尾为 outlined 或 filled 的图标）的颜色。当 tag 为 standard_icon 时生效。枚举值参见颜色枚举值。"""

    img_key: Union[str, None] = None
    """自定义前缀图标的图片 key。当 tag 为 custom_icon 时生效。

    图标 key 的获取方式：调用上传图片接口，上传用于发送消息的图片，并在返回值中获取图片的 image_key。"""


class MDHrefUrlVal(BaseModel):
    url: str
    pc_url: Union[str, None] = None
    android_url: Union[str, None] = None
    ios_url: Union[str, None] = None


class MDHref(BaseModel):
    urlVal: MDHrefUrlVal


class MDElement(BaseElement):
    tag: str = "markdown"
    content: str
    text_align: Literal["left", "center", "right"] = "left"
    """设置文本内容的对齐方式。可取值有：

    left：左对齐
    center：居中对齐
    right：右对齐"""

    text_size: Union[TextSize, str, None] = TextSize.NORMAL.value
    icon: Union[IconElement, None] = None
    href: Union[MDHref, None] = None


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


class ColumnSetActionMultiUrl(BaseModel):
    url: Union[str, None] = None
    android_url: Union[str, None] = None
    ios_url: Union[str, None] = None
    pc_url: Union[str, None] = None


class ColumnSetAction(BaseModel):
    multi_url: Union[ColumnSetActionMultiUrl, None] = None


class DivElement(BaseElement):
    tag: str = "div"
    text: PlainTextElement
    icon: Union[IconElement, None] = None


class HlineElement(BaseElement):
    tag: str = "hr"


ColumnSupportElementType = Union[
    MDElement, DivElement, PlainTextElement, ImageElement, HlineElement, "ColumnSetElement"
]


class ColumnElement(BaseElement):
    tag: str = "column"
    background_style: str = "default"
    """列的背景色样式。可取值：

    default：默认的白底样式，客户端深色主题下为黑底样式
    卡片支持的颜色枚举值和 RGBA 语法自定义颜色。参考颜色枚举值。"""

    elements: List[ColumnSupportElementType] = []
    """列容器内嵌的组件，不支持内嵌表格组件、多图混排组件和表单容器。"""

    width: Union[Literal["auto", "weighted"], str] = "auto"
    """列宽度。仅 flex_mode 为 none 时，生效此属性。取值：

    auto：列宽度与列内元素宽度一致
    weighted：列宽度按 weight 参数定义的权重分布
    具体数值，如 100px。取值范围为 [16,600]px。V7.4 及以上版本支持该枚举"""

    weight: int = 1
    """当 width 字段取值为 weighted 时生效，表示当前列的宽度占比。取值范围为 1 ~ 5 之间的整数。"""

    vertical_align: Literal["top", "center", "bottom"] = "top"
    """列垂直居中的方式。可取值：

    top：上对齐
    center：居中对齐
    bottom：下对齐"""

    vertical_spacing: Union[Literal["default", "medium", "large"], str] = "default"
    """列内组件的纵向间距。取值：

    default：默认间距，8px
    medium：中等间距
    large：大间距
    具体数值，如 8px。取值范围为 [0,28]px"""

    padding: Union[str, None] = None
    """列的内边距。值的取值范围为 [0,28]px。可选值：

    单值，如 "10px"，表示列的四个外边距都为 10 px。
    多值，如 "4px 12px 4px 12px"，表示列的上、右、下、左的外边距分别为 4px，12px，4px，12px。四个值必填，使用空格间隔。"""

    action: Union[ColumnSetAction, None] = None


class ColumnSetElement(BaseElement):
    tag: str = "column_set"
    """组件的标签。分栏组件的固定值为 column_set。"""
    flex_mode: Literal["none", "stretch", "flow", "bisect", "trisect"] = "none"
    """移动端和 PC 端的窄屏幕下，各列的自适应方式。取值：
    none：不做布局上的自适应，在窄屏幕下按比例压缩列宽度
    stretch：列布局变为行布局，且每列（行）宽度强制拉伸为 100%，所有列自适应为上下堆叠排布
    flow：列流式排布（自动换行），当一行展示不下一列时，自动换至下一行展示
    bisect：两列等分布局
    trisect：三列等分布局"""

    horizontal_spacing: Union[Literal["default", "small", "large"], str] = "default"
    """各列之间的水平分栏间距。取值：
    default：默认间距，8px
    small：窄间距，4px
    large：大间距，12px
    [0, 28px]：自定义间距"""

    horizontal_align: Literal["left", "center", "right"] = "left"
    """列容器水平对齐的方式。可取值：
    left：左对齐
    center：居中对齐
    right：右对齐"""

    margin: Union[str, None] = None
    """列的外边距。值的取值范围为 [0,28]px。可选值：
    单值，如 "10px"，表示列的四个外边距都为 10 px。
    多值，如 "4px 12px 4px 12px"，表示列的上、右、下、左的外边距分别为 4px，12px，4px，12px。四个值必填，使用空格间隔。
    注意：首行列的上外边距强制为 0，末行列的下外边距强制为 0。"""

    background_style: str = "default"
    """分栏的背景色样式。可取值：
    default：默认的白底样式，客户端深色主题下为黑底样式
    卡片支持的颜色枚举值和 RGBA 语法自定义颜色。参考颜色枚举值。
    注意：当存在分栏的嵌套时，上层分栏的颜色覆盖下层分栏的颜色。"""

    columns: List[ColumnElement] = []
    """分栏中列的配置。"""

    action: Union[ColumnSetAction, None] = None


class CardConfigStyleTextSize(BaseModel):
    default: str = "medium"
    """在无法差异化配置字号的旧版飞书客户端上，生效的字号属性。选填。"""
    pc: str = "medium"
    """桌面端的字号。"""
    mobile: str = "medium"
    """移动端的字号。"""


class CardConfigStyleColor(BaseModel):
    light_mode: str = "rgba(5,157,178,0.52)"
    """浅色主题下的自定义颜色语法"""
    dark_mode: str = "rgba(78,23,108,0.49)"
    """深色主题下的自定义颜色语法"""


class CardConfigStyle(BaseModel):
    text_size: Dict[str, CardConfigStyleTextSize] = {"cus-0": CardConfigStyleTextSize()}
    """分别为移动端和桌面端添加自定义字号，同时添加兜底字号。用于在组件 JSON 中设置字号属性。支持添加多个自定义字号对象。"""
    color: Dict[str, CardConfigStyleColor] = {"cus-0": CardConfigStyleColor()}
    """分别为飞书客户端浅色主题和深色主题添加 RGBA 语法。用于在组件 JSON 中设置颜色属性。支持添加多个自定义颜色对象。"""


class CardConfig(BaseModel):
    enable_forward: bool = True
    """是否支持转发卡片。默认值 true"""
    update_multi: bool = True
    """是否为共享卡片。为 true 时即更新卡片的内容对所有收到这张卡片的人员可见。默认值 false。"""
    width_mode: Literal["fill", "compact", "default"] = "fill"
    """卡片宽度模式。支持 "compact"（紧凑宽度 400px）模式、"fill"（撑满聊天窗口宽度）模式和 "default" 默认模式(宽度上限为 600px)。"""
    compact_width: bool = True
    """已废弃字段。是否为紧凑型卡片宽度。与 width_mode 属性同时设置时，width_mode 将生效。"""
    use_custom_translation: bool = False
    """是否使用自定义翻译数据。默认值 false。为 true 时则在用户点击消息翻译后，使用 i18n 对应的目标语种作为翻译结果。若 i18n 取不到，则使用当前内容请求翻译，不使用自定义翻译数据。"""
    enable_forward_interaction: bool = False
    """转发的卡片是否仍然支持回传交互。默认值 false。"""
    style: CardConfigStyle = CardConfigStyle()


FormElementElementType = Union[PlainTextElement, MDElement, ImageElement, DivElement, HlineElement]


class FormElement(BaseElement):
    tag: str = "form"
    """表单容器的标签。固定值为 form。"""
    name: str
    """表单容器的唯一标识。用于识别用户提交的数据属于哪个表单容器。在同一张卡片内，该字段的值全局唯一。"""
    elements: List[BaseElement]
    """表单容器的子节点。可内嵌其它容器类组件和展示、交互组件，不支持内嵌表格、图表、和表单容器组件。"""


class CardLink(BaseModel):
    url: str
    android_url: Union[str, None] = None
    ios_url: Union[str, None] = None
    pc_url: Union[str, None] = None


ElementType = Union[
    MDElement,
    ImageElement,
    ColumnSetElement,
    DivElement,
    HlineElement,
    FormElement,
]


class I18nBody(BaseModel):
    zh_cn: List[ElementType] = []


class InteractiveCard(BaseModel):
    config: Union[CardConfig, None] = None
    """config 用于配置卡片的全局行为，包括是否允许被转发、是否为共享卡片等。"""
    card_link: Union[CardLink, None] = None
    """card_link 字段用于指定卡片整体的点击跳转链接。你可以配置一个默认链接，也可以分别为 PC 端、Android 端、iOS 端配置不同的跳转链接。"""
    i18n_elements: Union[I18nBody, None] = None
    """飞书卡片支持多语言设置。设置多语言后，卡片将根据用户的飞书客户端语言，自动展示对应语言的卡片内容，满足国际化业务需求。详情参考配置卡片多语言。"""
    header: Union[CardHeader, None] = None
    """标题组件 JSON 代码。详细字段说明参考标题组件。"""
    elements: Union[List[ElementType], None] = None
    """在 elements 字段中添加各个组件的 JSON 数据，组件将按数组顺序纵向流式排列。了解各个组件，参考组件概述。"""
    fallback: Union[Dict, None] = None
    """fallback 用于为卡片添加全局降级规则。触发降级时，卡片将全局展示“请升级客户端至最新版本后查看”占位图。
    注意：该字段要求飞书客户端的版本为 V7.7 及以上。"""
