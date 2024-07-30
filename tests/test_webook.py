import pytest
from dotenv import find_dotenv, load_dotenv

from slark import AsyncLark

pytestmark = pytest.mark.anyio

load_dotenv(find_dotenv())


async def test_webhook(client: AsyncLark):
    await client.webhook.post_error_card("msg", "traceback", "title", "subtitle")
    await client.webhook.post_error_card("msg", "traceback", "title")
    await client.webhook.post_success_card("msg", "title", "subtitle")
    await client.webhook.post_success_card("msg", "title")
