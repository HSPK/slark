import os

import pytest
from dotenv import find_dotenv, load_dotenv

from slark import AsyncLark

pytestmark = pytest.mark.anyio

load_dotenv(find_dotenv())
client = AsyncLark(webhook=os.getenv("TEST_WEBHOOK_URL"))


async def test_webhook():
    await client.webhook.post_error_card("msg", "traceback", "title", "subtitle")
    await client.webhook.post_error_card("msg", "traceback", "title")
    await client.webhook.post_success_card("msg", "title", "subtitle")
    await client.webhook.post_success_card("msg", "title")
