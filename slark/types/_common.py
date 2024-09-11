from typing import Any, Dict

import pydantic


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        use_enum_values=True,
        arbitrary_types_allowed=True,
        extra="allow",
    )

    def model_dump(
        self,
        *,
        exclude_none: bool = True,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        return super().model_dump(exclude_none=exclude_none, **kwargs)
