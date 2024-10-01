from .base import BaseModel
from .text import PlainText


class ConfirmDialogue(BaseModel):
    title: PlainText
    text: PlainText