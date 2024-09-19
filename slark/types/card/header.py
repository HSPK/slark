import enum
from typing import List, Union

from .._common import BaseModel
from .ud_icon import UDIconElement


class TextTagColor(enum.Enum):
    NEUTRAL = "neutral"
    BLUE = "blue"
    TURQUOISE = "turquoise"
    LIME = "lime"
    ORANGE = "orange"
    VIOLET = "violet"
    INDIGO = "indigo"
    WATHET = "wathet"
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"
    PURPLE = "purple"
    CARMINE = "carmine"


class CardTemplate(enum.Enum):
    BLUE = "blue"
    WATHET = "wath"
    TURQUOISE = "tuiquoise"
    GREEN = "green"
    YELLOW = "yellow"
    ORANGE = "orange"
    RED = "red"
    CARMINE = "carmine"
    VIOLET = "violet"
    PURPLE = "purple"
    INDIGO = "indigo"
    GREY = "grey"
    DEFAULT = "default"


class I18nText(BaseModel):
    zh_cn: Union[str, None] = None
    en_us: Union[str, None] = None
    ja_jp: Union[str, None] = None
    zh_hk: Union[str, None] = None
    zh_tw: Union[str, None] = None
    id_id: Union[str, None] = None
    vi_vn: Union[str, None] = None
    th_th: Union[str, None] = None
    pt_br: Union[str, None] = None
    es_es: Union[str, None] = None
    ko_kr: Union[str, None] = None
    de_de: Union[str, None] = None
    fr_fr: Union[str, None] = None
    it_it: Union[str, None] = None
    ru_ru: Union[str, None] = None
    ms_my: Union[str, None] = None


class CardHeaderTitle(BaseModel):
    tag: str = "plain_text"
    """固定值 plain_text。"""
    content: str
    """主标题内容。"""
    i18n: Union[I18nText, None] = None
    """多语言标题内容。必须配置 content 或 i18n 两个属性的其中一个。如果同时配置仅生效 i18n。"""


class CardHeaderSubtitle(BaseModel):
    tag: str = "plain_text"
    """固定值 plain_text。"""
    content: str
    """副标题内容。"""
    i18n: Union[I18nText, None] = None
    """多语言副标题内容。必须配置 content 或 i18n 两个属性的其中一个。如果同时配置仅生效 i18n。"""


class CardHeaderTextTagText(BaseModel):
    tag: str = "plain_text"
    content: str


class CardHeaderTextTag(BaseModel):
    tag: str = "text_tag"
    text: CardHeaderTextTagText
    """标签内容"""
    color: TextTagColor = TextTagColor.NEUTRAL
    """标签颜色"""


class CardHeaderI18nTextTag(BaseModel):
    zh_cn: Union[List[CardHeaderTextTag], None] = None
    en_us: Union[List[CardHeaderTextTag], None] = None
    ja_jp: Union[List[CardHeaderTextTag], None] = None
    zh_hk: Union[List[CardHeaderTextTag], None] = None
    zh_tw: Union[List[CardHeaderTextTag], None] = None
    id_id: Union[List[CardHeaderTextTag], None] = None
    vi_vn: Union[List[CardHeaderTextTag], None] = None
    th_th: Union[List[CardHeaderTextTag], None] = None
    pt_br: Union[List[CardHeaderTextTag], None] = None
    es_es: Union[List[CardHeaderTextTag], None] = None
    ko_kr: Union[List[CardHeaderTextTag], None] = None
    de_de: Union[List[CardHeaderTextTag], None] = None
    fr_fr: Union[List[CardHeaderTextTag], None] = None
    it_it: Union[List[CardHeaderTextTag], None] = None
    ru_ru: Union[List[CardHeaderTextTag], None] = None
    ms_my: Union[List[CardHeaderTextTag], None] = None


class CardHeaderIcon(BaseModel):
    img_key: str
    """用作前缀图标的图片 key。"""


class CardHeader(BaseModel):
    title: CardHeaderTitle
    """卡片主标题。必填。"""
    subtitle: Union[CardHeaderSubtitle, None] = None
    """卡片副标题。可选。"""
    text_tag_list: Union[List[CardHeaderTextTag], None] = None
    """标题后缀标签，最多设置 3 个 标签，超出不展示。可选。"""
    i18n_text_tag_list: Union[CardHeaderI18nTextTag, None] = None
    """国际化标题后缀标签。每个语言环境最多设置 3 个 tag，超出不展示。可选。同时配置原字段和国际化字段，优先生效国际化配置。"""
    template: CardTemplate = CardTemplate.DEFAULT.value
    """标题主题颜色。"""
    icon: Union[CardHeaderIcon, None] = None
    """自定义前缀图标"""
    ud_icon: Union[UDIconElement, None] = None
    """图标库中的前缀图标，和 icon 同时设置时以 ud_icon 为准。"""
