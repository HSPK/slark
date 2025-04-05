from typing import Dict, List, Union

from typing_extensions import Literal

from .._common import BaseModel
from .container.collapsible import CollapsibleElement
from .container.column import ColumnSetElement
from .container.form import FormElement
from .container.interactive_container import InteractiveContainerElement
from .displaying.chart import ChartElement
from .displaying.divider import HlineElement
from .displaying.header import CardHeader, CardHeaderTextTag, CardTemplate
from .displaying.image import ImageElement
from .displaying.image_combination import ImageCombinationElement
from .displaying.markdown import MDElement
from .displaying.note import NoteElement
from .displaying.person import PersonElement
from .displaying.person_list import PersonListElement
from .displaying.plain_text import DivElement, PlainTextElement
from .displaying.table import TableElement
from .icon import IconElement
from .interactive.button import ButtonElement
from .interactive.checker import CheckerElement
from .interactive.date_picker import DatePickerElement
from .interactive.input_box import InputBoxElement
from .interactive.multi_select_person import MultiSelectPersonElement
from .interactive.multi_select_static import MultiSelectStaticElement
from .interactive.overflow import OverflowElement
from .interactive.picker_datetime import PickerDatetimeElement
from .interactive.picker_time import PickerTimeElement
from .interactive.select_img import SelectImgElement
from .interactive.select_person import SelectPersonElement
from .interactive.select_static import SelectStaticElement

"""飞书卡片文档链接 https://open.feishu.cn/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-json-structure"""


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
    enable_forward: Union[bool, None] = None
    """是否支持转发卡片。默认值 true"""
    update_multi: Union[bool, None] = None
    """是否为共享卡片。为 true 时即更新卡片的内容对所有收到这张卡片的人员可见。默认值 false。"""
    width_mode: Union[Literal["fill", "compact", "default"], None] = None
    """卡片宽度模式。支持 "compact"（紧凑宽度 400px）模式、"fill"（撑满聊天窗口宽度）模式和 "default" 默认模式(宽度上限为 600px)。"""
    compact_width: Union[bool, None] = None
    """已废弃字段。是否为紧凑型卡片宽度。与 width_mode 属性同时设置时，width_mode 将生效。"""
    use_custom_translation: Union[bool, None] = None
    """是否使用自定义翻译数据。默认值 false。为 true 时则在用户点击消息翻译后，使用 i18n 对应的目标语种作为翻译结果。若 i18n 取不到，则使用当前内容请求翻译，不使用自定义翻译数据。"""
    enable_forward_interaction: Union[bool, None] = None
    """转发的卡片是否仍然支持回传交互。默认值 false。"""
    style: Union[CardConfigStyle, None] = None


class CardLink(BaseModel):
    url: str
    android_url: Union[str, None] = None
    ios_url: Union[str, None] = None
    pc_url: Union[str, None] = None


ElementType = Union[
    ChartElement,
    HlineElement,
    DivElement,
    ImageCombinationElement,
    ImageElement,
    MDElement,
    NoteElement,
    PersonElement,
    PersonListElement,
    PlainTextElement,
    TableElement,
    ColumnSetElement,
    FormElement,
    InteractiveContainerElement,
    CollapsibleElement,
    ButtonElement,
    CheckerElement,
    DatePickerElement,
    InputBoxElement,
    MultiSelectPersonElement,
    MultiSelectStaticElement,
    OverflowElement,
    PickerDatetimeElement,
    PickerTimeElement,
    SelectImgElement,
    SelectPersonElement,
    SelectStaticElement,
]


class I18nBody(BaseModel):
    zh_cn: Union[List[ElementType], None] = None
    en_us: Union[List[ElementType], None] = None
    ja_jp: Union[List[ElementType], None] = None
    zh_hk: Union[List[ElementType], None] = None
    zh_tw: Union[List[ElementType], None] = None
    id_id: Union[List[ElementType], None] = None
    vi_vn: Union[List[ElementType], None] = None
    th_th: Union[List[ElementType], None] = None
    pt_br: Union[List[ElementType], None] = None
    es_es: Union[List[ElementType], None] = None
    ko_kr: Union[List[ElementType], None] = None
    de_de: Union[List[ElementType], None] = None
    fr_fr: Union[List[ElementType], None] = None
    it_it: Union[List[ElementType], None] = None
    ru_ru: Union[List[ElementType], None] = None
    ms_my: Union[List[ElementType], None] = None


class I18nHeaderElement(BaseModel):
    title: Union[PlainTextElement, None] = None
    subtitle: Union[PlainTextElement, None] = None
    template: Union[CardTemplate, None] = None
    ud_icon: Union[IconElement, None] = None
    text_tag_list: Union[List[CardHeaderTextTag], None] = None


class I18nHeader(BaseModel):
    zh_cn: Union[I18nHeaderElement, None] = None
    en_us: Union[I18nHeaderElement, None] = None
    ja_jp: Union[I18nHeaderElement, None] = None
    zh_hk: Union[I18nHeaderElement, None] = None
    zh_tw: Union[I18nHeaderElement, None] = None
    id_id: Union[I18nHeaderElement, None] = None
    vi_vn: Union[I18nHeaderElement, None] = None
    th_th: Union[I18nHeaderElement, None] = None
    pt_br: Union[I18nHeaderElement, None] = None
    es_es: Union[I18nHeaderElement, None] = None
    ko_kr: Union[I18nHeaderElement, None] = None
    de_de: Union[I18nHeaderElement, None] = None
    fr_fr: Union[I18nHeaderElement, None] = None
    it_it: Union[I18nHeaderElement, None] = None
    ru_ru: Union[I18nHeaderElement, None] = None
    ms_my: Union[I18nHeaderElement, None] = None


class InteractiveCard(BaseModel):
    config: Union[CardConfig, None] = None
    """config 用于配置卡片的全局行为，包括是否允许被转发、是否为共享卡片等。"""
    card_link: Union[CardLink, None] = None
    """card_link 字段用于指定卡片整体的点击跳转链接。你可以配置一个默认链接，也可以分别为 PC 端、Android 端、iOS 端配置不同的跳转链接。"""
    i18n_elements: Union[I18nBody, None] = None
    """飞书卡片支持多语言设置。设置多语言后，卡片将根据用户的飞书客户端语言，自动展示对应语言的卡片内容，满足国际化业务需求。详情参考配置卡片多语言。"""
    header: Union[CardHeader, None] = None
    """标题组件 JSON 代码。详细字段说明参考标题组件。"""
    i18n_header: Union[I18nHeader, None] = None
    """多语言表头"""
    elements: Union[List[ElementType], None] = None
    """在 elements 字段中添加各个组件的 JSON 数据，组件将按数组顺序纵向流式排列。了解各个组件，参考组件概述。"""
    fallback: Union[Dict, None] = None
    """fallback 用于为卡片添加全局降级规则。触发降级时，卡片将全局展示“请升级客户端至最新版本后查看”占位图。
    注意：该字段要求飞书客户端的版本为 V7.7 及以上。"""
