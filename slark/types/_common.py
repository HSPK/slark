from typing import Any

import pydantic


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        use_enum_values=True,
        arbitrary_types_allowed=True,
    )

    def model_dump(
        self,
        *,
        exclude_none: bool = True,
        **kwargs: Any,
    ) -> dict[str, Any]:
        return super().model_dump(exclude_none=exclude_none, **kwargs)
