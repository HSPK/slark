from typing import List, Union

from typing_extensions import Literal

from slark.types._common import BaseModel

"""文档 https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/bitable-record-data-structure-overview"""


class MultiLineText(BaseModel):
    text: str
    type: Literal["text", "mention", "url"]
    mention_type: Union[Literal["User", "Doc", "Sheet", "Bitable", "Docx"], None] = None
    """type字段为mention，该字段有效，可选值有：User,Doc,Sheet,Bitable,Docx"""
    token: Union[str, None] = None
    """type字段为mention，该字段有效，不同mentionType该字段表示不同的含义
        mentionType	token含义
        User	用户id
        Doc	文档token
        Sheet	电子表格token
        Bitable	多维表格token
        Docx	文档token"""
    link: Union[str, None] = None
    """链接，type字段为url，该字段有效"""
    name: Union[str, None] = None
    """名称，type字段为url或mention，该字段有效"""


class User(BaseModel):
    id: str
    name: Union[str, None] = None
    """人员名字"""
    avatar_url: Union[str, None] = None
    """头像链接"""
    en_name: Union[str, None] = None
    """英文名字"""
    email: Union[str, None] = None
    """邮箱"""


class Group(BaseModel):
    name: Union[str, None] = None
    """群组名"""
    avatar_url: Union[str, None] = None
    """头像链接"""
    id: str
    """群组id"""


class HyperLink(BaseModel):
    text: str
    """文本名称"""
    link: str
    """超链接"""


class Attachment(BaseModel):
    file_token: str
    """附件token"""
    name: Union[str, None] = None
    """附件名称"""
    type: Union[str, None] = None
    """附件的 mime 类型, 如: image/png"""
    size: Union[int, None] = None
    """附件大小, 单位: 字节"""
    url: Union[str, None] = None
    """	附件url，下载请参考: 
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/attachment#22daecaf"""
    tmp_url: Union[str, None] = None
    """生成附件临时下载链接的url，需access token鉴权"""


class LinkRecord(BaseModel):
    link_record_ids: List[str]
    """包含多个recordID字符串的数组"""


class Location(BaseModel):
    location: str
    """经纬度"""
    pname: str
    """省"""
    cityname: str
    """市"""
    adname: str
    """区"""
    address: str
    """详细地址"""
    name: str
    """地名"""
    full_address: str
    """完整地址"""


class Email(BaseModel):
    link: str
    """邮箱的 URL 链接。示例值：mailto:zhangmin@bytedance.com"""
    type: str = "url"
    """固定取值 "url"。"""
    text: str
    """用户邮箱。示例值："zhangmin@bytedance.com"。"""


FormulaType = Union[
    List[int],
    List[str],
    List[float],
    List[bool],
    List[MultiLineText],
    List[User],
    List[Group],
    List[HyperLink],
    List[Attachment],
    List[LinkRecord],
    List[Location],
    List[Email],
]


class Formula(BaseModel):
    type: int
    """value数据类型（相同字段类型用ui_type区分）：
    1：多行文本、条码
    2：数字、进度、货币、评分
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
    value: List[FormulaType]


class Empty(BaseModel):
    pass


FieldValueType = Union[
    int,
    str,
    float,
    bool,
    User,
    None,
    List[str],
    List[MultiLineText],
    List[User],
    List[Group],
    HyperLink,
    List[Attachment],
    LinkRecord,
    Location,
    Formula,
    Email,
    Empty,
]
