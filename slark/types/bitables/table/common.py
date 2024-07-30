import enum
from typing import List, Union

from typing_extensions import Literal

from slark.types._common import BaseModel, field_validator


class TableFieldPropertyOption(BaseModel):
    name: Union[str, None] = None
    """选项名

    示例值："红色"""

    id: Union[str, None] = None
    """选项 ID，创建时不允许指定 ID

    示例值："optKl35lnG"""

    color: Union[int, None] = None
    """选项颜色

    示例值：0

    数据校验规则：

    取值范围：0 ～ 54"""

    @field_validator("name")
    def validate_color(cls, v: int):
        if v < 0 or v > 54:
            raise ValueError("color should be 0-54")
        return v


class TableFieldPropertyAutoSerialOption(BaseModel):
    type: Literal["system_number", "fixed_text", "created_time"]
    """自动编号的可选规则项类型

    示例值："created_time"

    可选值有：

    system_number：自增数字位,value范围1-9
    fixed_text：固定字符，最大长度：20
    created_time：创建时间，支持格式 "yyyyMMdd"、"yyyyMM"、"yyyy"、"MMdd"、"MM"、"dd"""
    value: str
    """与自动编号的可选规则项类型相对应的取值

    示例值：'yyyyMMdd'"""


class TableFieldPropertyAllowedEditModes(BaseModel):
    manual: Union[bool, None] = None
    """是否允许手动录入

    示例值：true"""

    scan: Union[bool, None] = None
    """是否允许移动端录入

    示例值：true"""


class TableFieldPropertyRating(BaseModel):
    symbol: Union[str, None] = None
    """评分字段的符号展示

    示例值：'star'"""


class TableFieldPropertyLocation(BaseModel):
    input_type: Literal["only_mobile", "not_limit"]
    """地理位置输入限制

    示例值："not_limit"

    可选值有：

    only_mobile：只允许移动端上传
    not_limit：无限制"""


class TableFieldPropertyAutoSerial(BaseModel):
    type: str
    options: List[TableFieldPropertyAutoSerialOption]


class TableFieldProperty(BaseModel):
    options: Union[List[TableFieldPropertyOption], None] = None
    """单选、多选字段的选项信息"""

    formatter: Union[str, None] = None
    """数字、公式字段的显示格式

    示例值：'0'"""

    date_formatter: Union[str, None] = None
    """日期、创建时间、最后更新时间字段的显示格式

    示例值：'日期格式'"""

    auto_fill: Union[bool, None] = None
    """日期字段中新纪录自动填写创建时间

    示例值：false"""

    multiple: Union[bool, None] = None
    """人员字段中允许添加多个成员，单向关联、双向关联中允许添加多个记录

    示例值：false"""

    table_id: Union[str, None] = None
    """单向关联、双向关联字段中关联的数据表的id

    示例值：'tblsRc9GRRXKqhvW'"""

    table_name: Union[str, None] = None
    """单向关联、双向关联字段中关联的数据表的名字

    示例值：""table2""" ""

    back_field_name: Union[str, None] = None
    """双向关联字段中关联的数据表中对应的双向关联字段的名字

    示例值：""table1-双向关联""" ""

    auto_serial: Union[TableFieldPropertyAutoSerial, None] = None
    """自动编号类型"""

    location: Union[TableFieldPropertyLocation, None] = None
    """地理位置输入方式"""

    formula_expression: Union[str, None] = None
    """公式字段的表达式

    示例值：'bitable::$table[tblNj92WQBAasdEf].$field[fldMV60rYs]*2'"""

    allowed_edit_modes: Union[TableFieldPropertyAllowedEditModes, None] = None
    """字段支持的编辑模式"""

    min: Union[int, float, None] = None
    """进度、评分等字段的数据范围最小值

    示例值：0"""

    max: Union[int, float, None] = None
    """进度、评分等字段的数据范围最大值

    示例值：10"""

    range_customize: Union[bool, None] = None
    """进度等字段是否支持自定义范围

    示例值：true"""

    currency_code: Union[str, None] = None
    """货币币种

    示例值：'CNY'"""

    rating: Union[TableFieldPropertyRating, None] = None
    """评分字段的相关设置"""


class TableFieldDescription(BaseModel):
    disable_sync: Union[bool, None] = None
    """是否禁止同步，如果为true，表示禁止同步该描述内容到表单的问题描述

    示例值：true

    默认值：true"""

    text: Union[str, None] = None
    """字段描述内容，支持换行\n

    示例值："请按 name_id 格式填写\n例如：“Alice_20202020”"""


class FieldType(enum.Enum):
    TEXT = 1
    NUMBER = 2
    SINGLE_SELECT = 3
    MULTI_SELECT = 4
    DATE = 5
    CHECKBOX = 7
    USER = 11
    PHONE = 13
    URL = 15
    ATTACHMENT = 17
    SINGLE_LINK = 18
    FORMULA = 20
    DUPLEX_LINK = 21
    LOCATION = 22
    GROUP_CHAT = 23
    CREATED_TIME = 1001
    MODIFIED_TIME = 1002
    CREATED_USER = 1003
    MODIFIED_USER = 1004
    AUTO_NUMBER = 1005


class TableField(BaseModel):
    field_name: str
    """字段名,示例值："文本"""

    type: FieldType
    """可选值有：

    1：多行文本
    2：数字
    3：单选
    4：多选
    5：日期
    7：复选框
    11：人员
    13：电话号码
    15：超链接
    17：附件
    18：单向关联
    20：公式
    21：双向关联
    22：地理位置
    23：群组
    1001：创建时间
    1002：最后更新时间
    1003：创建人
    1004：修改人
    1005：自动编号"""

    ui_type: Union[
        Literal[
            "Text",
            "Barcode",
            "Number",
            "Progress",
            "Currency",
            "Rating",
            "SingleSelect",
            "MultiSelect",
            "DateTime",
            "Checkbox",
            "User",
            "GroupChat",
            "Phone",
            "Url",
            "Attachment",
            "SingleLink",
            "Formula",
            "DuplexLink",
            "Location",
            "CreatedTime",
            "ModifiedTime",
            "CreatedUser",
            "ModifiedUser",
            "AutoNumber",
        ],
        None,
    ] = None
    """字段在界面上的展示类型，例如进度字段是数字的一种展示形态

    示例值："Progress"

    可选值有：

    Text：多行文本
    Barcode：条码
    Number：数字
    Progress：进度
    Currency：货币
    Rating：评分
    SingleSelect：单选
    MultiSelect：多选
    DateTime：日期
    Checkbox：复选框
    User：人员
    GroupChat：群组
    Phone：电话号码
    Url：超链接
    Attachment：附件
    SingleLink：单向关联
    Formula：公式
    DuplexLink：双向关联
    Location：地理位置
    CreatedTime：创建时间
    ModifiedTime：最后更新时间
    CreatedUser：创建人
    ModifiedUser：修改人
    AutoNumber：自动编号"""

    property: Union[TableFieldProperty, None] = None
    description: Union[TableFieldDescription, None] = None


class TableData(BaseModel):
    name: Union[str, None] = None
    """数据表名称

    请注意：

    名称中的首尾空格将会被去除。
    示例值："table1"

    数据校验规则：

    长度范围：1 字符 ～ 100 字符"""
    default_view_name: Union[str, None] = None
    """默认表格视图的名称，不填则默认为 表格。

    请注意：

    名称中的首尾空格将会被去除。
    名称中不允许包含 [ ] 两个字符"""

    fields: Union[List[TableField]] = None
    """数据表的初始字段。

    请注意：

    如果 default_view_name 字段和 fields 字段都不填写，将会创建一个仅包含索引列的空数据表。

    如果指定了 fields 字段，将会创建一个包含初始字段的数据表且默认第一个字段为索引列。

    数据校验规则：

    长度范围：1 ～ 300"""

    @field_validator("name")
    def validate_name(cls, v: str):
        v = v.strip()
        if not v or len(v) > 100:
            raise ValueError("name length should be 1-100")
        return v

    @field_validator("default_view_name")
    def validate_default_view_name(cls, v: str):
        v = v.strip()
        if "[" in v or "]" in v:
            raise ValueError("default_view_name should not contain [ or ]")
        return v

    @field_validator("fields")
    def validate_fields(cls, v: List[TableField]):
        if v is not None and len(v) > 300:
            raise ValueError("fields length should be 1-300")
        return v
