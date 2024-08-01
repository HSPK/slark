import os
import time
import uuid

import pytest
from dotenv import find_dotenv, load_dotenv

from slark import AsyncLark
from slark.types.bitables import common as bc
from slark.types.bitables.table.common import TableData, TableField

pytestmark = pytest.mark.asyncio(loop_scope="session")

load_dotenv(find_dotenv())
app_token = os.getenv("TEST_APP_TOKEN")
url = os.getenv("TEST_BITABLE_URL")

table_id = None
table_ids = []


async def test_get_bitable_meta(client: AsyncLark):
    response = await client.bitables.meta.get(app_token)
    assert response.code == 0


async def test_write_bitable_meta(client: AsyncLark):
    response = await client.bitables.meta.update(app_token, name="update test")
    assert response.code == 0


async def test_list_tables(client: AsyncLark):
    global table_id

    response = await client.bitables.table.list(app_token)

    assert response.code == 0
    table_id = response.data.items[0].table_id


async def test_create_table(client: AsyncLark):
    global table_ids

    table = TableData(
        name=f"test/{str(uuid.uuid4())}",
        default_view_name="test default view",
        fields=[
            TableField(
                field_name="test text",
                type=bc.FieldType.TEXT,
            ),
            TableField(
                field_name="test barcode",
                type=bc.FieldType.TEXT,
                ui_type=bc.UIType.BARCODE,
            ),
            TableField(
                field_name="test number",
                type=bc.FieldType.NUMBER,
            ),
            TableField(
                field_name="test money",
                type=bc.FieldType.NUMBER,
                ui_type=bc.UIType.CURRENCY,
                property=bc.CurrencyFieldProperty(
                    formatter="0.00",
                    currency_code="CNY",
                ),
            ),
            TableField(
                field_name="test date",
                type=bc.FieldType.DATE,
                property=bc.DateTimeFieldProperty(
                    date_formatter="yyyy-MM-dd HH:mm",
                ),
            ),
            TableField(
                field_name="test person",
                type=bc.FieldType.PERSON,
                property=bc.PersonFieldProperty(
                    multiple=False,
                ),
            ),
            TableField(
                field_name="test lookup",
                type=bc.FieldType.LOOKUP,
                property=bc.LookupFieldProperty(
                    table_id=table_id,
                ),
            ),
            TableField(
                field_name="test duplex link",
                type=bc.FieldType.DUPLEX_LINK,
                property=bc.DuplexLinkFieldProperty(
                    table_id=table_id,
                ),
            ),
            TableField(
                field_name="test checkbox",
                type=bc.FieldType.CHECKBOX,
            ),
            TableField(
                field_name="test create time",
                type=bc.FieldType.CREATED_TIME,
                property=bc.CreateUpdateTimeFieldProperty(
                    date_formatter="yyyy-MM-dd HH:mm",
                ),
            ),
            TableField(
                field_name="test progress",
                type=bc.FieldType.NUMBER,
                ui_type=bc.UIType.PROGRESS,
                property=bc.ProgressFieldProperty(
                    formatter="0.0",
                    range_customize=True,
                    min=0,
                    max=100,
                ),
            ),
            TableField(
                field_name="test rating",
                type=bc.FieldType.NUMBER,
                ui_type=bc.UIType.RATING,
                property=bc.RatingFieldProperty(
                    rating=bc.RatingFieldPropertyRating(symbol="fire"),
                    min=0,
                    max=5,
                ),
            ),
            TableField(
                field_name="test single option",
                type=bc.FieldType.SINGLE_SELECT,
                property=bc.OptionFieldProperty(
                    options=[
                        bc.OptionFieldPropertyOption(
                            name="option 1",
                            color=0,
                        ),
                        bc.OptionFieldPropertyOption(
                            name="option 2",
                            color=1,
                        ),
                    ],
                ),
            ),
        ],
    )
    response = await client.bitables.table.create(app_token, table=table)
    assert response.code == 0
    table_ids.append(response.data.table_id)


async def test_list_fields(client: AsyncLark):
    response = await client.bitables.field.list(app_token, table_id=table_id)
    assert response.code == 0


field_id = None


async def test_create_field(client: AsyncLark):
    global field_id
    response = await client.bitables.field.create(
        app_token,
        table_id=table_id,
        field_name="test field",
        type=bc.FieldType.TEXT,
        ui_type=bc.UIType.BARCODE,
    )
    assert response.code == 0
    field_id = response.data.field.field_id


async def test_update_field(client: AsyncLark):
    response = await client.bitables.field.update(
        app_token,
        table_id=table_id,
        field_id=field_id,
        field_name="update field",
        type=bc.FieldType.TEXT,
        ui_type=bc.UIType.TEXT,
    )
    assert response.code == 0


async def test_delete_field(client: AsyncLark):
    response = await client.bitables.field.delete(app_token, table_id=table_id, field_id=field_id)
    assert response.code == 0


record_ids = []


async def test_create_record(client: AsyncLark):
    global record_ids

    response = await client.bitables.record.create(
        app_token,
        table_id=table_ids[0],
        fields={
            "test text": "test text",
            "test barcode": "test barcode",
            "test number": 1,
            "test money": 1.0,
            "test date": int(time.time() * 1000),
            # "test person": "test person",
            # "test lookup": "test lookup",
            # "test duplex link": "test duplex link",
            "test checkbox": True,
            "test create time": int(time.time() * 1000),
            "test progress": 50.0,
            "test rating": 3,
            "test single option": "option 1",
        },
    )
    assert response.code == 0
    record_ids.append(response.data.record.record_id)


bitable_df = None


async def test_read_bitable(client: AsyncLark):
    global bitable_df

    bitable_df = await client.bitables.read(url)


async def test_update_bitable(client: AsyncLark):
    bitable_df["test text"] = "update text"
    items = await client.bitables.update(url, data=bitable_df)
    assert len(items) == bitable_df.shape[0]
    df = await client.bitables.read(url)
    assert df["test text"].values[0] == "update text"


async def test_append_bitable(client: AsyncLark):
    items = await client.bitables.append(url, data=bitable_df)
    assert len(items) == bitable_df.shape[0]
    df = await client.bitables.read(url)
    assert df.shape[0] == bitable_df.shape[0] * 2


async def test_delete_bitable(client: AsyncLark):
    items = await client.bitables.delete(url, record_ids=bitable_df.index.tolist())
    assert len(items) == bitable_df.shape[0]
    df = await client.bitables.read(url)
    assert df.shape[0] == bitable_df.shape[0]


async def test_batch_create_record(client: AsyncLark):
    global record_ids

    response = await client.bitables.record.batch_create(
        app_token,
        table_id=table_ids[0],
        records=[
            {
                "test text": "test text",
                "test barcode": "test barcode",
                "test number": 1,
                "test money": 1.0,
                "test date": int(time.time() * 1000),
                "test checkbox": True,
                "test create time": int(time.time() * 1000),
                "test progress": 50.0,
                "test rating": 3,
                "test single option": "option 1",
            },
            {
                "test text": "test text",
                "test barcode": "test barcode",
                "test number": 1,
                "test money": 1.0,
                "test date": int(time.time() * 1000),
                "test checkbox": True,
                "test create time": int(time.time() * 1000),
                "test progress": 50.0,
                "test rating": 3,
                "test single option": "option 1",
            },
        ],
    )
    assert response.code == 0
    record_ids.extend([record.record_id for record in response.data.records])


async def test_list_records(client: AsyncLark):
    response = await client.bitables.record.search(app_token, table_id=table_ids[0])
    assert response.code == 0
    assert record_ids == [record.record_id for record in response.data.items]


async def test_batch_get_record(client: AsyncLark):
    response = await client.bitables.record.batch_get(
        app_token, table_id=table_ids[0], record_ids=record_ids
    )
    assert response.code == 0
    assert record_ids == [record.record_id for record in response.data.records]


async def test_update_record(client: AsyncLark):
    response = await client.bitables.record.update(
        app_token,
        table_id=table_ids[0],
        record_id=record_ids[0],
        fields={
            "test text": "update text",
            "test barcode": "test barcode",
            "test number": 1,
            "test money": 1.0,
            "test date": int(time.time() * 1000),
            "test checkbox": True,
            "test create time": int(time.time() * 1000),
            "test progress": 30.0,
            "test rating": 3,
            "test single option": "option 2",
        },
    )
    assert response.code == 0
    assert response.data.record.record_id == record_ids[0]


async def test_delete_record(client: AsyncLark):
    global record_ids

    response = await client.bitables.record.delete(
        app_token, table_id=table_ids[0], record_id=record_ids[0]
    )
    assert response.code == 0
    record_ids.pop(0)


async def test_batch_delete_record(client: AsyncLark):
    global record_ids

    response = await client.bitables.record.batch_delete(
        app_token, table_id=table_ids[0], record_ids=record_ids
    )
    assert response.code == 0
    record_ids = []


async def test_batch_create_table(client: AsyncLark):
    names = [f"test/{str(uuid.uuid4())}" for _ in range(2)]
    response = await client.bitables.table.batch_create(app_token, names=names)
    assert response.code == 0

    table_ids.extend(response.data.table_ids)


async def test_update_table(client: AsyncLark):
    global table_ids
    name = "update test"
    reponse = await client.bitables.table.update(app_token, table_id=table_ids[0], name=name)
    assert reponse.code == 0


async def test_delete_table(client: AsyncLark):
    global table_ids

    response = await client.bitables.table.delete(app_token, table_id=table_ids[0])
    assert response.code == 0
    table_ids.pop(0)


async def test_batch_delete_table(client: AsyncLark):
    global table_ids

    response = await client.bitables.table.batch_delete(app_token, table_ids=table_ids)
    assert response.code == 0
    table_ids = []
