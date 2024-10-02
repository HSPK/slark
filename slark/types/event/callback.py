from typing import Dict, List, Union

from .._common import BaseModel


class CallbackOperator(BaseModel):
    tenant_key: Union[str, None] = None
    user_id: Union[str, None] = None
    open_id: Union[str, None] = None


class CallbackAction(BaseModel):
    value: Union[Dict, str]
    tag: str
    timezone: str
    name: str
    form_value: Union[Dict, None] = None
    input_value: Union[str, None] = None
    option: Union[str, None] = None
    options: Union[List[str], None] = None
    checked: Union[bool, None] = None


class CallbackContext(BaseModel):
    url: Union[str, None] = None
    preview_token: Union[str, None] = None
    open_message_id: str
    open_chat_id: str


class CallbackEvent(BaseModel):
    operator: CallbackOperator
    token: str
    action: CallbackAction
    host: str
    delivery_type: Union[str, None] = None
    context: CallbackContext
