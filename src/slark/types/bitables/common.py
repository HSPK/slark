import enum
from typing import List, Union

from typing_extensions import Literal

from slark.types._common import BaseModel


class FieldType(enum.Enum):
    """https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/guide
    可选值有：

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

    TEXT = 1
    NUMBER = 2
    SINGLE_SELECT = 3
    MULTI_SELECT = 4
    DATE = 5
    CHECKBOX = 7
    PERSON = 11
    PHONE = 13
    URL = 15
    ATTACHMENT = 17
    LOOKUP = 18
    FORMULA = 20
    DUPLEX_LINK = 21
    LOCATION = 22
    GROUP_CHAT = 23
    CREATED_TIME = 1001
    MODIFIED_TIME = 1002
    CREATED_USER = 1003
    MODIFIED_USER = 1004
    AUTO_NUMBER = 1005


class UIType(enum.Enum):
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

    TEXT = "Text"
    BARCODE = "Barcode"
    NUMBER = "Number"
    PROGRESS = "Progress"
    CURRENCY = "Currency"
    RATING = "Rating"
    SINGLE_SELECT = "SingleSelect"
    MULTI_SELECT = "MultiSelect"
    DATE_TIME = "DateTime"
    CHECKBOX = "Checkbox"
    USER = "User"
    GROUP_CHAT = "GroupChat"
    PHONE = "Phone"
    URL = "Url"
    ATTACHMENT = "Attachment"
    SINGLE_LINK = "SingleLink"
    FORMULA = "Formula"
    DUPLEX_LINK = "DuplexLink"
    LOCATION = "Location"
    CREATED_TIME = "CreatedTime"
    MODIFIED_TIME = "ModifiedTime"
    CREATED_USER = "CreatedUser"
    MODIFIED_USER = "ModifiedUser"
    AUTO_NUMBER = "AutoNumber"


class FieldPropertyEditModes(BaseModel):
    manual: bool = True
    """是否允许手动录入"""
    scan: bool = True
    """是否允许移动端录入"""


class BarCodeFieldProperty(BaseModel):
    allowed_edit_modes: FieldPropertyEditModes


class NumberFieldProperty(BaseModel):
    formatter: str
    """格式，参考：formatter
    网页中数字格式	formatter
    整数	"0"
    保留1位小数	"0.0"
    保留2位小数	"0.00"
    保留3位小数	"0.000"
    保留4位小数	"0.0000"
    千分位	"1,000"
    千分位（小数点）	"1,000.00"
    百分比	"%"
    百分比（小数点）	"0.00%"
    人民币	"¥"
    人民币（小数点）	"¥0.00"
    美元	"$"
    美元（小数点）	"$0.00"
    """


class CurrencyFieldProperty(BaseModel):
    formatter: Literal["0", "0.0", "0.00", "0.000", "0.0000"]
    """"0"
    "0.0"
    "0.00"
    "0.000"
    "0.0000"
    """

    currency_code: Literal[
        "CNY",
        "USD",
        "EUR",
        "GBP",
        "AED",
        "AUD",
        "BRL",
        "CAD",
        "CHF",
        "HKD",
        "INR",
        "IDR",
        "JPY",
        "KRW",
        "MOP",
        "MXN",
        "MYR",
        "PHP",
        "PLN",
        "RUB",
        "SGD",
        "THB",
        "TRY",
        "TWD",
        "VND",
    ]
    """网页中数字格式	货币符号	货币说明
    "CNY"	¥	人民币
    "USD"	$	美元
    "EUR"	€	欧元
    "GBP"	£	英镑
    "AED"	dh	阿联酋迪拉姆
    "AUD"	$	澳大利亚元
    "BRL"	R$	巴西雷亚尔
    "CAD"	$	加拿大元
    "CHF"	CHF	瑞士法郎
    "HKD"	$	港元
    "INR"	₹	印度卢比
    "IDR"	Rp	印尼盾
    "JPY"	¥	日元
    "KRW"	"₩"	韩元
    "MOP"	MOP$	澳门元
    "MXN"	$	墨西哥比索
    "MYR"	RM	马来西亚令吉
    "PHP"	₱	菲律宾比索
    "PLN"	zł	波兰兹罗提
    "RUB"	₽	俄罗斯卢布
    "SGD"	$	新加坡元
    "THB"	฿	泰国铢
    "TRY"	₺	土耳其里拉
    "TWD"	NT$	新台币
    "VND"	₫	越南盾"""


class ProgressFieldProperty(BaseModel):
    formatter: str
    """进度的格式
    可选值：
    "0"
    "0.0"
    "0.00"
    "0%"
    "0.0%"
    "0.00%"
    """

    range_customize: bool = False
    """是否允许自定义进度条值"""
    min: Union[int, float, None] = None
    """进度的最小值, range_customizeture为true时必填"""
    max: Union[int, float, None] = None
    """进度的最大值, range_customize为true时必填"""


class RatingFieldPropertyRating(BaseModel):
    symbol: Literal[
        "star", "heart", "thumbsup", "fire", "smile", "lightning", "flower", "number"
    ] = "star"
    """评分图标
    "star"
    "heart"
    "thumbsup"
    "fire"
    "smile"
    "lightning"
    "flower"
    "number"
    """


class RatingFieldProperty(BaseModel):
    formatter: str = "0"
    rating: Union[RatingFieldPropertyRating, None] = None
    """评分设置"""
    min: Union[int, None] = None
    """评分的最小值"""
    max: Union[int, None] = None


class OptionFieldPropertyOption(BaseModel):
    id: Union[str, None] = None
    """选项id"""
    name: Union[str, None] = None
    """选项名"""
    color: Union[int, None] = None
    """选项颜色, 0~54, 从上一个选项的color开始依次递增"""


class OptionFieldProperty(BaseModel):
    options: List[OptionFieldPropertyOption]


class DateTimeFieldProperty(BaseModel):
    date_formatter: Literal[
        "yyyy/MM/dd",
        "yyyy/MM/dd HH:mm",
        "yyyy-MM-dd",
        "yyyy-MM-dd HH:mm",
        "MM-dd",
        "MM/dd/yyyy",
        "dd/MM/yyyy",
    ] = "yyyy/MM/dd"
    """日期格式，参考：日期格式date_formatter
    网页中日期格式	date_formatter
    2021/01/30	"yyyy/MM/dd"
    2021/01/30 14:00	"yyyy/MM/dd HH:mm"
    2021-01-30	"yyyy-MM-dd"
    2021-01-30 14:00	"yyyy-MM-dd HH:mm"
    01-30	"MM-dd"
    01/30/2021	"MM/dd/yyyy"
    30/01/2021	"dd/MM/yyyy"
    """
    auto_fill: bool = False
    """新纪录自动填写创建时间"""


class PersonFieldProperty(BaseModel):
    multiple: bool = True
    """允许添加多个成员"""


class LookupFieldProperty(BaseModel):
    multiple: bool = True
    """允许添加多个记录"""
    table_id: str
    """关联的数据表的id"""
    table_name: Union[str, None] = None
    """关联的数据表的名字（仅在响应体中返回）"""


class DuplexLinkFieldProperty(BaseModel):
    back_field_id: Union[str, None] = None
    """关联的数据表中双向关联字段的id（仅在响应体中返回）"""
    back_field_name: Union[str, None] = None
    """关联的数据表中双向关联字段的名字, default to: 关联的数据表名-本字段名"""
    multiple: bool = True
    """允许添加多个记录"""
    table_id: str
    """关联的数据表的id"""
    table_name: Union[str, None] = None
    """关联的数据表的名字（仅在响应体中返回）"""


class FormulaFieldProperty(BaseModel):
    formatter: Literal[
        "",
        "0",
        "0.0",
        "0.00",
        "1,000",
        "1,000.00",
        "%",
        "0.00%",
        "¥",
        "¥0.00",
        "$",
        "$0.00",
        "yyyy/MM/dd HH:mm",
        "yyyy/MM/dd",
        "yyyy-MM-dd",
        "MM-dd",
    ] = ""
    """格式参考：formatter
    网页中公式格式	formatter
    默认	""
    整数	"0"
    保留1位小数	"0.0"
    保留2位小数	"0.00"
    千分位	"1,000"
    千分位（小数点）	"1,000.00"
    百分比	"%"
    百分比（小数点）	"0.00%"
    人民币	"¥"
    人民币（小数点）	"¥0.00"
    美元	"$"
    美元（小数点）	"$0.00"
    2021/01/30 14:00	"yyyy/MM/dd HH:mm"
    2021/01/30	"yyyy/MM/dd"
    2021-01-30	"yyyy-MM-dd"
    01-30	"MM-dd"
    """

    formula_expression: str
    """格式参考：[formula](https://www.feishu.cn/hc/zh-CN/articles/360049067853-%E5%A4%9A%E7%BB%B4%E8%A1%A8%E6%A0%BC%E5%85%AC%E5%BC%8F%E5%AD%97%E6%AE%B5%E6%A6%82%E8%BF%B0)"""


class GroupFieldProperty(BaseModel):
    multiple: bool = True
    """是否允许添加多个群组"""


class CreateUpdateTimeFieldProperty(BaseModel):
    date_formatter: Literal[
        "yyyy/MM/dd",
        "yyyy/MM/dd HH:mm",
        "yyyy-MM-dd",
        "yyyy-MM-dd HH:mm",
        "MM-dd",
        "MM/dd/yyyy",
        "dd/MM/yyyy",
    ] = "yyyy/MM/dd"
    """日期格式，参考：日期格式date_formatter"""


class AutoNumberFieldPropertyAutoSerial(BaseModel):
    type: Literal["custom", "auto_increment_number"]
    """网页中编号类型	auto_serial_type
    自定义编号	"custom"
    自增数字	"auto_increment_number"
    """


class AutoNumberFieldPropertyOption(BaseModel):
    type: Literal["system_number", "fixed_text", "created_time"]
    """网页中编号类型	rule_option_type	对应的value限制
    自增数字	"system_number"	1-9
    固定字符	"fixed_text"	最大长度：20
    创建日期	"created_time"	可选值参考：created_time
    
    网页中创建日期	created_time
    20220130	"yyyyMMdd"
    202201	"yyyyMM"
    2022	"yyyy"
    0130	"MMdd"
    01	"MM"
    30	"dd"
    """
    value: str


class AutoNumberFieldProperty(BaseModel):
    auto_serial: Union[AutoNumberFieldPropertyAutoSerial, None] = None
    reformat_existing_records: bool = False
    options: List[AutoNumberFieldPropertyOption]


FieldPropertyType = Union[
    BarCodeFieldProperty,
    NumberFieldProperty,
    CurrencyFieldProperty,
    ProgressFieldProperty,
    RatingFieldProperty,
    OptionFieldProperty,
    DateTimeFieldProperty,
    PersonFieldProperty,
    LookupFieldProperty,
    DuplexLinkFieldProperty,
    FormulaFieldProperty,
    GroupFieldProperty,
    CreateUpdateTimeFieldProperty,
    AutoNumberFieldProperty,
]
