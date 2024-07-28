from pydantic import BaseModel
from slark.settings import Settings


class Context(BaseModel):
    settings: Settings | None = None
