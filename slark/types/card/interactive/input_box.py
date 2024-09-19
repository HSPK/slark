from typing import Dict, Union

from typing_extensions import Literal

from ..._common import BaseModel
from ..base import BaseElement


class InputBoxText(BaseModel):
    content: str
    tag: str = "plain_text"


class InputBoxConfirm(BaseModel):
    title: InputBoxText
    text: InputBoxText


class InputBoxFallback(BaseModel):
    tag: str = "fallback_text"
    text: Union[InputBoxText, None] = None


class InputBoxElement(BaseElement):
    tag: str = "input"
    name: Union[str, None] = None
    """输入框的唯一标识。当输入框内嵌在表单容器时，该属性生效，用于识别用户提交的文本属于哪个输入框。\n
    注意：当输入框组件嵌套在表单容器中时，该字段必填且需在卡片全局内唯一。"""
    required: Union[bool, None] = None
    """输入框的内容是否必填。当输入框内嵌在表单容器时，该属性可用。其它情况将报错或不生效。可取值：\n
    true：输入框必填。当用户点击表单容器的“提交”时，未填写输入框，则前端提示“有必填项未填写”，不会向开发者的服务端发起回传请求。\n
    false：输入框选填。当用户点击表单容器的“提交”时，未填写输入框，仍提交表单容器中的数据。"""
    disabled: Union[bool, None] = None
    """是否禁用该输入框。该属性仅支持飞书 V7.4 及以上版本的客户端。可选值：\n
    true：禁用输入框组件\n
    false：输入框组件保持可用状态"""
    placeholder: Union[InputBoxText, None] = None
    """输入框中的占位文本。占位文本的内容，最多支持 100 个字符。"""
    default_value: Union[str, None] = None
    """输入框中为用户预填写的内容。展示为用户在输入框中输入文本后待提交的样式。"""
    width: Union[str, None] = None
    """输入框的宽度。支持以下枚举值：\n
    default：默认宽度\n
    fill：卡片最大支持宽度\n
    [100,∞)px：自定义宽度。超出卡片宽度时将按最大支持宽度展示"""
    max_length: Union[int, None] = None
    """输入框可容纳的最大文本长度，可取 1~1,000 范围内的整数。当用户输入的文本字符数超过最大文本长度，组件将报错提示。"""
    input_type: Union[Literal["text", "multiline_text", "password"], None] = None
    """指定输入框的输入类型。默认为 text，即文本类型。支持以下枚举值：
    text：普通文本\n
    multiline_text：多行文本，即可输入包含换行符的多行文本内容。换行符在回调中以 \\n 返回\n
    password：密码。用户输入的文本内容将以“•”显示"""
    show_icon: Union[bool, None] = None
    """当输入类型为密码类型时，是否展示如下所示的前缀图标。仅当 input_type 为 password 时有效。"""
    rows: Union[int, None] = None
    """当输入类型为多行文本时，输入框的默认展示行数。仅当 input_type 为 multiline_text 时有效。"""
    auto_resize: Union[bool, None] = None
    """当输入类型为多行文本时，输入框高度是否自适应文本高度。仅在 PC 端生效。仅当 input_type 为 multiline_text 时有效。可选值：\n
    true：输入框高度自适应输入框内的文本高度\n
    false：输入框高度固定为 rows 属性指定的高度，不随输入框中的内容变化而变化。"""
    max_rows: Union[int, None] = None
    """输入框的最大展示行数。仅当 auto_resize 为 true 时有效。注意：\n
    取值为大于等于 1 的整数。否则，小于 1 则自动取 1，不为整数则四舍五入取整。
    取值为空时不限制输入框的最大文本展示高度（默认值），但前端渲染时，输入框可展示的最大高度不超过 x 行。"""
    label: Union[InputBoxText, None] = None
    """文本标签，即对输入框的描述，用于提示用户要填写的内容。多用于表单容器中内嵌的输入框组件。"""
    label_position: Union[Literal["top", "left"], None] = None
    """文本标签的位置。可取值：\n
    top：文本标签位于输入框上方\n
    left：文本标签位于输入框左边\n
    注意：在移动端等窄屏幕场景下，文本标签将自适应固定展示在输入框上方。"""
    value: Union[str, Dict, None] = None
    """你可在交互事件中自定义回传数据，支持 string 或 object 数据类型。"""
    confirm: Union[InputBoxConfirm, None] = None
    """二次确认弹窗配置。指在用户提交时弹出二次确认弹窗提示；只有用户点击确认后，才提交输入的内容。该字段默认提供了确认和取消按钮，你只需要配置弹窗的标题与内容即可。\n
    注意：confirm 字段仅在用户点击包含提交属性的按钮时才会触发二次确认弹窗。"""
    fallback: Union[InputBoxFallback, Literal["drop"], None] = None
    """设置输入框组件的降级文案。由于输入框仅支持飞书 V6.8 及以上版本的客户端，你需选择在低于此版本的客户端上，该组件的降级展示方式：\n
    不填写该字段，使用系统默认的降级文案：“请升级至最新版本客户端，以查看内容”\n
    "drop"：填写 "drop"，在旧版本客户端上直接丢弃该输入框组件\n
    使用 text 文本对象自定义降级文案"""
