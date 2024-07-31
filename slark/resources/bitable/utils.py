from typing import List, Optional

import arrow
import pandas as pd

from slark.types.bitables.field.common import Field, UIType
from slark.types.bitables.record.response import FieldValueType, RecordResponseData


def fields_records_to_dataframe(
    fields: List[Field],
    records: List[RecordResponseData],
    timezone: Optional[str] = "Asia/Shanghai",
) -> pd.DataFrame:
    def field_value_to_text(field: FieldValueType) -> str:
        if hasattr(field, "text"):
            return field.text
        if isinstance(field, list):
            return ", ".join([field_value_to_text(f) for f in field])
        return field

    data = [{k: field_value_to_text(v) for k, v in record.fields.items()} for record in records]
    df = pd.DataFrame(data)
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
