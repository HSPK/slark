import pytest
from dotenv import find_dotenv, load_dotenv

import slark.types.card as card
from slark import AsyncLark

pytestmark = pytest.mark.asyncio(loop_scope="module")

load_dotenv(find_dotenv())


async def test_image_upload(client: AsyncLark):
    with open("tests/assets/test.png", "rb") as f:
        resp = await client.messages.image.upload(f.read(), image_type="message")
    img_key = resp.data.image_key

    demo = card.InteractiveCard(
        header=card.CardHeader(
            title=card.CardHeaderTitle(content="Test Image"),
            ud_icon=card.UDIconElement(token=card.UDIconToken.IMAGE_OUTLINED),
        ),
        elements=[
            card.ImageElement(img_key=img_key, alt=card.ImageTextElement(content="Test Image")),
        ],
    )

    await client.webhook.send_card(demo)
