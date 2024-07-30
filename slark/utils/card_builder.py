from typing import List, Union

from slark.types.card.card import (
    BaseElement,
    ColumnElement,
    ColumnSetElement,
    DivElement,
    I18nBody,
    I18nHeader,
    IconElement,
    InteractiveCard,
    MDElement,
    PlainTextElement,
    TitleHeader,
)


class InteractiveCardBuilder:
    def __init__(self):
        self.elements = []
        self.header = None

    def add_element(self, element: BaseElement):
        self.elements.append(element)
        return self

    def add_div_element(self, text: PlainTextElement):
        self.elements.append(DivElement(text=text))
        return self

    def add_md_element(self, content: str):
        self.elements.append(MDElement(content=content))
        return self

    def add_heading_text_element(self, content: str):
        self.elements.append(build_heading_text_element(content))
        return self

    def add_single_column_set_element(self, elements: List[BaseElement]):
        self.elements.append(build_single_column_set_element(elements))
        return self

    def set_header(self, header: TitleHeader):
        self.header = header
        return self

    def set_header_with_icon(self, title: str, subtitle: str, template: str, icon: str):
        self.header = build_header_with_icon(title, subtitle, template, icon)
        return self

    def build(self, header: Union[TitleHeader, None] = None) -> InteractiveCard:
        return build_card(self.elements, header)


def build_card(
    elements: List[BaseElement], header: Union[TitleHeader, None] = None
) -> InteractiveCard:
    _header = {} if header is None else I18nHeader(zh_cn=header)
    return InteractiveCard(
        i18n_elements=I18nBody(zh_cn=elements),
        i18n_header=_header,
    )


def build_heading_text_element(content: str):
    return PlainTextElement(
        content=content, text_size="heading", text_align="left", text_color="default"
    )


def build_single_column_set_element(elements: List[BaseElement]) -> ColumnSetElement:
    return ColumnSetElement(columns=[ColumnElement(elements=elements)])


def build_header_with_icon(title: str, subtitle: str, template: str, icon: str) -> TitleHeader:
    return TitleHeader(
        title=PlainTextElement(content=title),
        subtitle=PlainTextElement(content=subtitle),
        template=template,
        ud_icon=IconElement(token=icon),
    )


def build_success_msg_card(msg: str, title: str, subtitle: str):
    return build_card(
        elements=[
            build_single_column_set_element(
                [DivElement(text=build_heading_text_element("Message"))]
            ),
            MDElement(content=f"```txt\n{msg}\n```"),
        ],
        header=build_header_with_icon(title, subtitle, "green", "yes_filled"),
    )


def build_error_msg_card(msg: str, traceback: str, title: str, subtitle: str) -> InteractiveCard:
    return build_card(
        elements=[
            build_single_column_set_element(
                [DivElement(text=build_heading_text_element("Message"))]
            ),
            MDElement(content=f"```txt\n{msg}\n```"),
            build_single_column_set_element(
                [DivElement(text=build_heading_text_element("Traceback"))]
            ),
            MDElement(content=f"```\n{traceback.strip()}\n```"),
        ],
        header=build_header_with_icon(title, subtitle, "red", "error_filled"),
    )
