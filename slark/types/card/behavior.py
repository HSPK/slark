from typing import Dict, Union

from typing_extensions import Literal

from .base import BaseModel


class OpenURLBehavior(BaseModel):
    type: str = "open_url"
    default_url: str
    android_url: Union[str, None] = None
    ios_url: Union[str, None] = None
    pc_url: Union[str, None] = None
    """可配置为 `lark://msgcard/unsupported_action` 声明当前端不允许跳转。"""


class CallbackBehavior(BaseModel):
    type: str = "callback"
    value: Union[str, Dict, None] = None


class FormActionBehavior(BaseModel):
    type: str = "form_action"
    value: Literal["submit", "reset"] = "submit"
    """表单事件类型。可取值：

    submit：提交整个表单
    reset：重置整个表单"""


BehaviorType = Union[OpenURLBehavior, CallbackBehavior, FormActionBehavior]
