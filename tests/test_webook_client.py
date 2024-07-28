import os

from dotenv import find_dotenv, load_dotenv

from slark.client.robot.webhook import WebhookRobot
import pytest

pytestmark = pytest.mark.anyio

load_dotenv(find_dotenv())
client = WebhookRobot(url=os.getenv("TEST_WEBHOOK_URL"))


async def test_webhook():
    await client.send_error_card("msg", "traceback", "title", "subtitle")
    await client.send_error_card("msg", "traceback", "title")
    await client.send_success_card("msg", "title", "subtitle")
    await client.send_success_card("msg", "title")
