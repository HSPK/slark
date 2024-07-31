import os

import pandas as pd
import pytest
from dotenv import find_dotenv, load_dotenv

from slark import AsyncLark

pytestmark = pytest.mark.asyncio(loop_scope="module")

load_dotenv(find_dotenv())
url = os.getenv("TEST_SHEET_URL")


async def test_get_sheet_info(client: AsyncLark):
    await client.sheets.get_sheet_info(url)


async def test_read(client: AsyncLark):
    await client.sheets.read(url, has_header=False)


async def test_write(client: AsyncLark):
    example_df = pd.DataFrame({"a": [11, 22, 33], "b": [44, 55, 66]})
    await client.sheets.write(url, data=example_df, start_row=8)
    await client.sheets.prepend(url, data=example_df, start_row=8)
    await client.sheets.append(url, data=example_df, start_row=8)
