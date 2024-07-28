from pydantic.v1 import BaseModel


class BaseElement(BaseModel):
    tag: str


class MDElement(BaseElement):
    tag: str = "markdown"
    content: str
    text_align: str = "left"
    text_size: str = "normal"


class PlainTextElement(BaseElement):
    tag: str = "plain_text"
    content: str
    text_size: str | None = None
    text_align: str | None = None
    text_color: str | None = None


class IconElement(BaseElement):
    tag: str = "standard_icon"
    token: str


class I18nBody(BaseModel):
    zh_cn: list[BaseElement] = []


class ColumnElement(BaseElement):
    tag: str = "column"
    elements: list[BaseElement]
    width: str = "weighted"
    weight: int = 1


class ColumnSetElement(BaseElement):
    tag: str = "column_set"
    flex_mode: str = "none"
    horizontal_spacing: str = "default"
    background_style: str = "default"
    columns: list[ColumnElement]


class DivElement(BaseElement):
    tag: str = "div"
    text: PlainTextElement


class TitleHeader(BaseModel):
    title: PlainTextElement
    subtitle: PlainTextElement
    template: str
    ud_icon: IconElement


class I18nHeader(BaseModel):
    zh_cn: TitleHeader


class InteractiveCard(BaseModel):
    config: dict = {}
    i18n_elements: I18nBody = I18nBody()
    i18n_header: I18nHeader | dict = {}
