import asyncio
import os

from pytest import fixture

from slark import AsyncLark

_client = None


@fixture(scope="session")
def client():
    global _client
    if _client is None:
        _client = AsyncLark(
            app_id=os.getenv("TEST_APP_ID"),
            app_secret=os.getenv("TEST_APP_SECRET"),
            webhook=os.getenv("TEST_WEBHOOK_URL"),
        )
    return _client


@fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()
