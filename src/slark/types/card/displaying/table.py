from typing import Dict, List, Union

from typing_extensions import Literal

from ..base import BaseElement, BaseModel
from ..color import Color


class TableHeaderStyle(BaseModel):
    text_align: Union[Literal["left", "center", "right"], None] = None
    text_size: Union[Literal["normal", "heading"], None] = None
    backgroud_style: Union[Literal["none", "grey"]] = None
    text_color: Union[Literal["default", "grey"], None] = None
    bold: Union[bool, None] = None
    lines: Union[int, None] = None


class TableColumnFormat(BaseModel):
    precision: Union[int, None] = None
    symbol: Union[str, None] = None
    seperator: Union[bool, None] = None


class TableColumn(BaseModel):
    name: str
    """自定义列的标记。用于唯一指定行数据对象数组中，需要将数据填充至这一行的具体哪个单元格中。"""
    display_name: Union[str, None] = None
    """在表头展示的列名称。不填或为空则不展示列名称。"""
    width: Union[str, None] = None
    """列宽度。可取值：\n
    auto：自适应内容宽度\n
    自定义宽度：自定义表格的列宽度，如 120px。取值范围是 [80px,600px] 的整数\n
    自定义宽度百分比：自定义列宽度占当前表格画布宽度的百分比（表格画布宽度 = 卡片宽度-卡片左右内边距），如 25%。取值范围是 [1%,100%]"""

    horizontal_align: Union[Literal["left", "center", "right"], None] = None
    """列内数据对齐方式。可选值：\n
    left：左对齐\n
    center：居中对齐\n
    right：右对齐"""

    data_type: Literal["text", "lark_md", "options", "number", "persons", "date", "markdown"] = (
        "text"
    )
    """列数据类型。可选值如下所示。了解不同类型用法，参考 data_type 字段说明一节。\n
    text：不带格式的普通文本。为 data_type 默认值。
    lark_md：支持部分 markdown 格式的文本。飞书 v7.10 及之后版本支持。详情参考普通文本-lark_md 支持的 Markdown 语法
    options：选项标签
    number：数字。默认在单元格中右对齐展示。若选择该数据类型，你可继续在 column 中添加 format 字段，设置数字的格式属性
    persons：人员列表。为用户名称+头像样式
    date：日期时间。需输入 Unix 标准毫秒级时间戳，飞书客户端将按用户本地时区展示日期时间。飞书 v7.6 及之后版本支持
    markdown：支持完整 Markdown 语法的文本内容。详情参考富文本（Markdown）组件。飞书 v7.14 及之后版本支持"""

    format: Union[TableColumnFormat, None] = None
    date_format: Union[
        Literal["YYYY/MM/DD", "YYYY/MM/DD HH:mm", "YYYY-MM-DD", "YYYY-MM-DD HH:mm"], str, None
    ] = None
    """该字段仅当 data_type 为 date 时生效。你可按需选择以下日期时间占位符，并使用任意分隔符组合。\n
    YYYY：年
    MM：月
    DD：日
    HH：小时
    mm：分钟
    ss：秒
    推荐使用以下日期格式。默认按 RFC 3339 标准格式展示日期时间。

    YYYY/MM/DD
    YYYY/MM/DD HH:mm
    YYYY-MM-DD
    YYYY-MM-DD HH:mm
    DD/MM/YYYY
    MM/DD/YYYY"""


class TableCellOption(BaseModel):
    text: str
    color: Color


TableCellType = Union[
    str,
    int,
    float,
    TableCellOption,
    List[str],
]
"""日期时间。需输入 Unix 标准毫秒级时间戳，飞书客户端将按用户本地时区展示日期时间。支持添加 date_format 字段，设置日期的格式属性。默认按 RFC 3339 标准格式展示日期时间。详情参考 date_format 字段说明。
markdown type 支持完整 Markdown 语法的文本内容。详情参考富文本（Markdown）组件。"""


class TableElement(BaseElement):
    tag: str = "table"
    page_size: Union[int, None] = None
    row_height: Union[str, Literal["low", "middle", "high"], None] = None
    header_style: Union[TableHeaderStyle, None] = None
    columns: List[TableColumn]
    rows: List[Dict[str, TableCellType]]
