import os

import pytest
from dotenv import find_dotenv, load_dotenv

from slark import AsyncLark

pytestmark = pytest.mark.asyncio(loop_scope="module")

load_dotenv(find_dotenv())
url = os.getenv("TEST_DOCUMENT_URL")


async def test_document_info(client: AsyncLark):
    await client.docs.get_document_info(url)


async def test_read_blocks(client: AsyncLark):
    await client.docs.read_markdown(url)


async def test_read_raw_content(client: AsyncLark):
    await client.docs.read_raw(url)
