import os

from pytest import fixture

from slark import AsyncLark


@fixture
def client():
    return AsyncLark(
        app_id=os.getenv("TEST_APP_ID"),
        app_secret=os.getenv("TEST_APP_SECRET"),
        webhook=os.getenv("TEST_WEBHOOK_URL"),
    )
