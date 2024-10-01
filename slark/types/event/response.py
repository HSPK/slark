from typing import Dict, Union

from typing_extensions import Literal

from .._common import BaseModel
from ..card import I18nText, InteractiveCard


class TemplateCard(BaseModel):
    template_id: str
    template_variable: Union[Dict, None] = None
    template_version_name: Union[str, None] = None

class CallbackCard(BaseModel):
    type: Literal["raw", "template"]
    data: Union[InteractiveCard, TemplateCard]


class CallbackToast(BaseModel):
    type: Literal["info", "success", "error", "warning"]
    """info、success、error、和 warning。"""
    content: Union[str, None] = None
    """提示内容。"""
    i18n: Union[I18nText, None] = None


class CallbackResponse(BaseModel):
    toast: Union[CallbackToast, None] = None
    card: Union[CallbackCard, None] = None
