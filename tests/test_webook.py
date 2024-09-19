import pytest
from dotenv import find_dotenv, load_dotenv

import slark.types.card as card
from slark import AsyncLark

pytestmark = pytest.mark.asyncio(loop_scope="module")

load_dotenv(find_dotenv())


async def test_webhook(client: AsyncLark):
    await client.webhook.post_error_card("msg", "traceback", "title", "subtitle")
    await client.webhook.post_error_card("msg", "traceback", "title")
    await client.webhook.post_success_card("msg", "title", "subtitle")
    await client.webhook.post_success_card("msg", "title")


async def test_send_card(client: AsyncLark):
    demo = card.InteractiveCard(
        header=card.CardHeader(
            title=card.CardHeaderTitle(content="Interactive Card"),
            subtitle=card.CardHeaderSubtitle(content="This is an interactive card"),
            template=card.CardTemplate.BLUE,
            ud_icon=card.UDIconElement(
                token=card.UDIconToken.ADD_BOLD_OUTLINED,
                style=card.UDIconStyle(color=card.Color.ORANGE),
            ),
        ),
        elements=[
            card.ColumnSetElement(
                flex_mode="flow",
                columns=[
                    card.ColumnElement(
                        elements=[
                            card.DivElement(
                                text=card.PlainTextElement(content="This is a div element")
                            ),
                            card.MDElement(
                                content="This is a markdown element\n---\nThis is a new line",
                                icon=card.IconElement(token=card.UDIconToken.INFO_OUTLINED),
                                text_size=card.TextSize.XXX_LARGE,
                            ),
                            card.HlineElement(),
                        ]
                    ),
                    card.ColumnElement(
                        elements=[
                            card.DivElement(
                                text=card.PlainTextElement(
                                    tag="lark_md", content="## This is a lark markdown element"
                                )
                            ),
                            card.HlineElement(),
                            card.DivElement(
                                text=card.PlainTextElement(
                                    content="This is a div element", text_align="center"
                                )
                            ),
                        ]
                    ),
                    card.ColumnElement(
                        elements=[
                            card.DivElement(
                                text=card.PlainTextElement(
                                    tag="lark_md", content="## This is a lark markdown element"
                                )
                            ),
                            card.HlineElement(),
                            card.DivElement(
                                text=card.PlainTextElement(
                                    content="This is a div element", text_align="center"
                                )
                            ),
                        ]
                    ),
                    card.ColumnElement(
                        elements=[
                            card.DivElement(
                                text=card.PlainTextElement(
                                    tag="lark_md",
                                    content="## This is a lark markdown element\ngheagi\ngheag\nhgieahga",
                                    lines=1,
                                )
                            ),
                            card.HlineElement(),
                            card.DivElement(
                                text=card.PlainTextElement(
                                    content="This is a div element", text_align="center"
                                )
                            ),
                        ]
                    ),
                ],
            )
        ],
    )
    await client.webhook.send_card(demo)
