import os

import pytest
from dotenv import find_dotenv, load_dotenv

from slark import AsyncLark

pytestmark = pytest.mark.anyio

load_dotenv(find_dotenv())
app_token = os.getenv("TEST_APP_TOKEN")
url = os.getenv("TEST_BITABLE_URL")

table_id = None


async def test_get_bitable_meta(client: AsyncLark):
    response = await client.bitables.get_bitable_meta(app_token)
    assert response.code == 0


async def test_write_bitable_meta(client: AsyncLark):
    response = await client.bitables.update_bitable_meta(app_token, name="update test")
    assert response.code == 0


async def test_list_tables(client: AsyncLark):
    global table_id

    response = await client.bitables.table.list(app_token)

    assert response.code == 0
    table_id = response.data.items[0].table_id


async def test_create_table(client: AsyncLark):
    response = await client.bitables.table.create(app_token, table={"name": "test"})
    assert response.code == 0
