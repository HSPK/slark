from slark.types._common import BaseModel
from slark.types.messages.common import LarkEventMessageBody, LarkUserID


class LarkEventSender(BaseModel):
    sender_id: LarkUserID
    sender_type: str
    tenant_key: str
    """tenant key，为租户在飞书上的唯一标识，用来换取对应的tenant_access_token，也可以用作租户在应用里面的唯一标识"""


class MessageEvent(BaseModel):
    sender: LarkEventSender
    message: LarkEventMessageBody