from typing import Union

from typing_extensions import Literal

from slark.types._common import BaseModel

from .common import FieldDescription, FieldPropertyType


class ListFieldParams(BaseModel):
    view_id: Union[str, None] = None
    """视图 ID

    示例值："vewOVMEXPF"
    """

    text_field_as_array: Union[bool, None] = None
    """控制字段描述（多行文本格式）数据的返回格式, true 表示以数组富文本形式返回

    示例值：true"""

    page_token: Union[str, None] = None
    """分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果

    示例值："fldwJ4YrtB"
    """

    page_size: Union[int, None] = None
    """	
    分页大小

    示例值：10

    默认值：20

    数据校验规则：

    最大值：100"""


class CreateFieldBody(BaseModel):
    field_name: str
    """多维表格字段名

    请注意：

    名称中的首尾空格将会被去除。
    示例值："多行文本"
    """
    type: Literal[
        1, 2, 3, 4, 5, 7, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 1001, 1002, 1003, 1004, 1005
    ]
    """字段类型（相同字段类型用ui_type区分）：
        1：多行文本（默认值）、条码
        2：数字（默认值）、进度、货币、评分
        3：单选
        4：多选
        5：日期
        7：复选框
        11：人员
        13：电话号码
        15：超链接
        17：附件
        18：单向关联
        19：查找引用
        20：公式
        21：双向关联
        22：地理位置
        23：群组
        1001：创建时间
        1002：最后更新时间
        1003：创建人
        1004：修改人
        1005：自动编号"""
    property: Union[FieldPropertyType, None] = None
    """字段属性，因字段类型而异"""

    ui_type: Literal[
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
        "Lookup",
        "DuplexLink",
        "Location",
        "CreatedTime",
        "ModifiedTime",
        "CreatedUser",
        "ModifiedUser",
        "AutoNumber",
    ]
    """字段的ui类型 ：
    "Text"：多行文本
    "Barcode"：条码
    "Number"：数字
    "Progress"：进度
    "Currency"：货币
    "Rating"：评分
    "SingleSelect"：单选
    "MultiSelect"：多选
    "DateTime"：日期
    "Checkbox"：复选框
    "User"：人员
    "GroupChat"：群组
    "Phone"：电话号码
    "Url"：超链接
    "Attachment"：附件
    "SingleLink"：单向关联
    "Formula"：公式
    "Lookup": 查找引用
    "DuplexLink"：双向关联
    "Location"：地理位置
    "CreatedTime"：创建时间
    "ModifiedTime"：最后更新时间
    "CreatedUser"：创建人
    "ModifiedUser"：修改人
    "AutoNumber"：自动编号"""

    description: Union[FieldDescription, None] = None
    """字段描述"""


class UpdateFieldBody(CreateFieldBody):
    pass
