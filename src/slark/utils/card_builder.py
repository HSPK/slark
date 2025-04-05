from typing import List, Union

import slark.types.card as card


def build_card(
    elements: List[card.ElementType], header: Union[card.CardHeader, None] = None
) -> card.InteractiveCard:
    _header = {} if header is None else header
    return card.InteractiveCard(
        elements=elements,
        header=_header,
    )


def build_heading_text_element(content: str):
    return card.PlainTextElement(
        content=content,
        text_size=card.TextSize.HEADING,
        text_align="left",
    )


def build_single_column_set_element(elements: List[card.ElementType]) -> card.ColumnSetElement:
    return card.ColumnSetElement(columns=[card.ColumnElement(elements=elements)])


def build_header_with_icon(title: str, subtitle: str, template: str, icon: str) -> card.CardHeader:
    return card.CardHeader(
        title=card.CardHeaderTitle(content=title),
        subtitle=card.CardHeaderSubtitle(content=subtitle),
        template=template,
        ud_icon=card.UDIconElement(token=icon),
    )


def build_success_msg_card(msg: str, title: str, subtitle: str):
    return build_card(
        elements=[
            build_single_column_set_element(
                [card.DivElement(text=build_heading_text_element("Message"))]
            ),
            card.MDElement(content=f"```txt\n{msg}\n```"),
        ],
        header=build_header_with_icon(
            title, subtitle, card.CardTemplate.GREEN, card.UDIconToken.YES_FILLED
        ),
    )


def build_error_msg_card(
    msg: str, traceback: str, title: str, subtitle: str
) -> card.InteractiveCard:
    return build_card(
        elements=[
            build_single_column_set_element(
                [card.DivElement(text=build_heading_text_element("Message"))]
            ),
            card.MDElement(content=f"```txt\n{msg}\n```"),
            build_single_column_set_element(
                [card.DivElement(text=build_heading_text_element("Traceback"))]
            ),
            card.MDElement(content=f"```\n{traceback.strip()}\n```"),
        ],
        header=build_header_with_icon(
            title, subtitle, card.CardTemplate.RED, card.UDIconToken.ERROR_FILLED
        ),
    )
