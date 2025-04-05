from typing import Dict, List, Union

import arrow
import pandas as pd

from slark.types.bitables.field.common import Field, UIType
from slark.types.bitables.record.common import Empty
from slark.types.bitables.record.response import FieldValueType, RecordResponseData


def fields_records_to_dataframe(
    fields: List[Field],
    records: List[RecordResponseData],
    timezone: Union[str, None] = "Asia/Shanghai",
) -> pd.DataFrame:
    def field_value_to_text(field: FieldValueType) -> str:
        if hasattr(field, "text"):
            return field.text
        if isinstance(field, list):
            return ", ".join([field_value_to_text(f) for f in field])
        if isinstance(field, Empty):
            return None
        return field

    data = [{k: field_value_to_text(v) for k, v in record.fields.items()} for record in records]
    index = [record.record_id for record in records]
    df = pd.DataFrame(data, index=index)
    for field in fields:
        if field.ui_type in [
            UIType.DATE_TIME.value,
            UIType.CREATED_TIME.value,
            UIType.MODIFIED_TIME.value,
        ]:
            df[field.field_name] = (
                pd.to_datetime(df[field.field_name], unit="ms") + arrow.now(timezone).utcoffset()
            )

    return df


def dataframe_to_records(
    df: pd.DataFrame,
    timezone: Union[str, None] = "Asia/Shanghai",
    use_index_as_record_id: bool = False,
) -> List[Dict[str, FieldValueType]]:
    for col in df.columns:
        if df[col].dtype == "datetime64[ns]":
            # 转为 unix timestamp，单位为 ms
            df[col] = df[col].dt.tz_localize(timezone).astype(int) // 10**6
    df_records = df.to_dict(orient="records")
    if use_index_as_record_id:
        return [
            {"record_id": index, "fields": record} for index, record in zip(df.index, df_records)
        ]
    else:
        return df_records
