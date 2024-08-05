import enum
from typing import List, Union

import pydantic
from typing_extensions import Literal


class BlockType(enum.Enum):
    """Block 类型

    可选值有：

    1：页面 Block

    2：文本 Block

    3：标题 1 Block

    4：标题 2 Block

    5：标题 3 Block

    6：标题 4 Block

    7：标题 5 Block

    8：标题 6 Block

    9：标题 7 Block

    10：标题 8 Block

    11：标题 9 Block

    12：无序列表 Block

    13：有序列表 Block

    14：代码块 Block

    15：引用 Block

    17：待办事项 Block

    18：多维表格 Block

    19：高亮块 Block

    20：会话卡片 Block

    21：流程图 & UML Block

    22：分割线 Block

    23：文件 Block

    24：分栏 Block

    25：分栏列 Block

    26：内嵌网页 Block

    27：图片 Block

    28：开放平台小组件 Block

    29：思维笔记 Block

    30：电子表格 Block

    31：表格 Block。了解如何在文档中插入表格，参考文档常见问题-如何插入表格并往单元格填充内容。

    32：表格单元格 Block

    33：视图 Block

    34：引用容器 Block

    35：任务 Block

    36：OKR Block

    37：OKR Objective Block

    38：OKR Key Result Block

    39：OKR 进展 Block

    40：文档小组件 Block

    41：Jira 问题 Block

    42：Wiki 子目录 Block

    43：画板 Block

    44：议程 Block

    45：议程项 Block

    46：议程项标题 Block

    47：议程项内容 Block

    48：链接预览 Block

    999：未支持 Block"""

    PAGE = 1
    TEXT = 2
    TITLE1 = 3
    TITLE2 = 4
    TITLE3 = 5
    TITLE4 = 6
    TITLE5 = 7
    TITLE6 = 8
    TITLE7 = 9
    TITLE8 = 10
    TITLE9 = 11
    UNORDERED_LIST = 12
    ORDERED_LIST = 13
    CODE_BLOCK = 14
    QUOTE = 15
    TODO = 17
    MULTI_DIMENSION_TABLE = 18
    HIGHLIGHT = 19
    CONVERSATION_CARD = 20
    FLOWCHART_UML = 21
    SEPARATOR = 22
    FILE = 23
    COLUMN = 24
    COLUMN_ITEM = 25
    EMBEDDED_WEBPAGE = 26
    IMAGE = 27
    OPEN_PLATFORM_WIDGET = 28
    MIND_MAP = 29
    SPREADSHEET = 30
    TABLE = 31
    TABLE_CELL = 32
    VIEW = 33
    REFERENCE_CONTAINER = 34
    TASK = 35
    OKR = 36
    OKR_OBJECTIVE = 37
    OKR_KEY_RESULT = 38
    OKR_PROGRESS = 39
    DOCUMENT_WIDGET = 40
    JIRA_ISSUE = 41
    WIKI_SUBDIRECTORY = 42
    CANVAS = 43
    AGENDA = 44
    AGENDA_ITEM = 45
    AGENDA_ITEM_TITLE = 46
    AGENDA_ITEM_CONTENT = 47
    LINK_PREVIEW = 48
    UNSUPPORTED = 999


class TextStyleAlign(enum.Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3


class CodeBlockLanguage(enum.Enum):
    """代码块的语言类型。仅支持对 Code 块进行修改
    可选值有：

    1：PlainText

    2：ABAP

    3：Ada

    4：Apache

    5：Apex

    6：Assembly Language

    7：Bash

    8：CSharp

    9：C++

    10：C

    11：COBOL

    12：CSS

    13：CoffeeScript

    14：D

    15：Dart

    16：Delphi

    17：Django

    18：Dockerfile

    19：Erlang

    20：Fortran

    21：FoxPro

    22：Go

    23：Groovy

    24：HTML

    25：HTMLBars

    26：HTTP

    27：Haskell

    28：JSON

    29：Java

    30：JavaScript

    31：Julia

    32：Kotlin

    33：LateX

    34：Lisp

    35：Logo

    36：Lua

    37：MATLAB

    38：Makefile

    39：Markdown

    40：Nginx

    41：Objective-C

    42：OpenEdgeABL

    43：PHP

    44：Perl

    45：PostScript

    46：Power Shell

    47：Prolog

    48：ProtoBuf

    49：Python

    50：R

    51：RPG

    52：Ruby

    53：Rust

    54：SAS

    55：SCSS

    56：SQL

    57：Scala

    58：Scheme

    59：Scratch

    60：Shell

    61：Swift

    62：Thrift

    63：TypeScript

    64：VBScript

    65：Visual Basic

    66：XML

    67：YAML

    68：CMake

    69：Diff

    70：Gherkin

    71：GraphQL

    72：OpenGL Shading Language

    73：Properties

    74：Solidity

    75：TOML"""

    PLAIN_TEXT = 1
    ABAP = 2
    ADA = 3
    APACHE = 4
    APEX = 5
    ASSEMBLY_LANGUAGE = 6
    BASH = 7
    CSHARP = 8
    CPLUSPLUS = 9
    C = 10
    COBOL = 11
    CSS = 12
    COFFEESCRIPT = 13
    D = 14
    DART = 15
    DELPHI = 16
    DJANGO = 17
    DOCKERFILE = 18
    ERLANG = 19
    FORTRAN = 20
    FOXPRO = 21
    GO = 22
    GROOVY = 23
    HTML = 24
    HTMLBARS = 25
    HTTP = 26
    HASKELL = 27
    JSON = 28
    JAVA = 29
    JAVASCRIPT = 30
    JULIA = 31
    KOTLIN = 32
    LATEX = 33
    LISP = 34
    LOGO = 35
    LUA = 36
    MATLAB = 37
    MAKEFILE = 38
    MARKDOWN = 39
    NGINX = 40
    OBJECTIVE_C = 41
    OPENEDGEABL = 42
    PHP = 43
    PERL = 44
    POSTSCRIPT = 45
    POWER_SHELL = 46
    PROLOG = 47
    PROTOBUF = 48
    PYTHON = 49
    R = 50
    RPG = 51
    RUBY = 52
    RUST = 53
    SAS = 54
    SCSS = 55
    SQL = 56
    SCALA = 57
    SCHEME = 58
    SCRATCH = 59
    SHELL = 60
    SWIFT = 61
    THRIFT = 62
    TYPESCRIPT = 63
    VBSCRIPT = 64
    VISUAL_BASIC = 65
    XML = 66
    YAML = 67
    CMAKE = 68
    DIFF = 69
    GHERKIN = 70
    GRAPHQL = 71
    OPENGL_SHADING_LANGUAGE = 72
    PROPERTIES = 73
    SOLIDITY = 74
    TOML = 75


class TextBackgroundColor(enum.Enum):
    """块的背景色

    可选值有：

    LightGrayBackground：浅灰色

    LightRedBackground：浅红色

    LightOrangeBackground：浅橙色

    LightYellowBackground：浅黄色

    LightGreenBackground：浅绿色

    LightBlueBackground：浅蓝色

    LightPurpleBackground：浅紫色

    PaleGrayBackground：淡灰色

    DarkGrayBackground：深灰色

    DarkRedBackground：深红色

    DarkOrangeBackground：深橙色

    DarkYellowBackground：深黄色

    DarkGreenBackground：深绿色

    DarkBlueBackground：深蓝色

    DarkPurpleBackground：深紫色

    """

    LIGHT_GRAY = "LightGrayBackground"
    LIGHT_RED = "LightRedBackground"
    LIGHT_ORANGE = "LightOrangeBackground"
    LIGHT_YELLOW = "LightYellowBackground"
    LIGHT_GREEN = "LightGreenBackground"
    LIGHT_BLUE = "LightBlueBackground"
    LIGHT_PURPLE = "LightPurpleBackground"
    PALE_GRAY = "PaleGrayBackground"
    DARK_GRAY = "DarkGrayBackground"
    DARK_RED = "DarkRedBackground"
    DARK_ORANGE = "DarkOrangeBackground"
    DARK_YELLOW = "DarkYellowBackground"
    DARK_GREEN = "DarkGreenBackground"
    DARK_BLUE = "DarkBlueBackground"
    DARK_PURPLE = "DarkPurpleBackground"


class TextElementBackgroundColor(enum.Enum):
    """背景色

    可选值有：

    1：浅粉红色

    2：浅橙色

    3：浅黄色

    4：浅绿色

    5：浅蓝色

    6：浅紫色

    7：浅灰色

    8：暗粉红色

    9：暗橙色

    10：暗黄色

    11：暗绿色

    12：暗蓝色

    13：暗紫色

    14：暗灰色

    15：暗银灰色"""

    LIGHT_PINK = 1
    LIGHT_ORANGE = 2
    LIGHT_YELLOW = 3
    LIGHT_GREEN = 4
    LIGHT_BLUE = 5
    LIGHT_PURPLE = 6
    LIGHT_GRAY = 7
    DARK_PINK = 8
    DARK_ORANGE = 9
    DARK_YELLOW = 10
    DARK_GREEN = 11
    DARK_BLUE = 12
    DARK_PURPLE = 13
    DARK_GRAY = 14
    DARK_SILVER_GRAY = 15


class TextElementTextColor(enum.Enum):
    """
    字体颜色

    可选值有：

    1：粉红色

    2：橙色

    3：黄色

    4：绿色

    5：蓝色

    6：紫色

    7：灰色"""

    PINK = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5
    PURPLE = 6
    GRAY = 7


class BorderColor(enum.Enum):
    """
    边框色

    可选值有：

    1：红色

    2：橙色

    3：黄色

    4：绿色

    5：蓝色

    6：紫色

    7：灰色"""

    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5
    PURPLE = 6
    GRAY = 7


class TextIndentationLevel(enum.Enum):
    NO_INDENT = "NoIndent"
    ONE_LEVEL_INDENT = "OneLevelIndent"


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict()


class TextStyle(BaseModel):
    align: Union[TextStyleAlign, None] = None
    """对齐方式"""
    done: Union[bool, None] = None
    """todo 的完成状态。支持对 Todo 块进行修改"""
    folded: Union[bool, None] = None
    """文本的折叠状态。支持对 Heading1~9、和有子块的 Text、Ordered、Bullet 和 Todo 块进行修改"""
    language: Union[CodeBlockLanguage, None] = None
    """代码块的语言类型。仅支持对 Code 块进行修改"""
    wrap: Union[bool, None] = None
    """代码块是否自动换行。支持对 Code 块进行修改"""
    background_color: Union[TextBackgroundColor, None] = None
    """块的背景色"""
    indentation_level: Union[TextIndentationLevel, None] = None
    """首行缩进级别"""


class DocType(enum.Enum):
    """云文档类型

    可选值有：

    1：Doc

    3：Sheet

    8：Bitable

    11：MindNote

    12：File

    15：Slide

    16：Wiki

    22：Docx"""

    DOC = 1
    SHEET = 3
    BITABLE = 8
    MINDNOTE = 11
    FILE = 12
    SLIDE = 15
    WIKI = 16
    DOCX = 22


class DiagramType(enum.Enum):
    FLOWCHART = 1
    UML = 2


class ViewType(enum.Enum):
    CARD = 1
    PREVIEW = 2


class IframeType(enum.Enum):
    """
    iframe 类型

    可选值有：

    1：哔哩哔哩

    2：西瓜视频

    3：优酷

    4：Airtable

    5：百度地图"""

    BILIBILI = 1
    XIGUA_VIDEO = 2
    YOUKU = 3
    AIRTABLE = 4
    BAIDU_MAP = 5


class TextElementLink(BaseModel):
    url: str


class TextElementStyle(BaseModel):
    bold: Union[bool, None] = None
    """加粗"""
    italic: Union[bool, None] = None
    """斜体"""
    strikethrough: Union[bool, None] = None
    """删除线"""
    underline: Union[bool, None] = None
    """下划线"""
    inline_code: Union[bool, None] = None
    """行内代码"""
    backgroud_color: Union[TextElementBackgroundColor, None] = None
    """背景色"""
    text_color: Union[TextElementTextColor, None] = None
    """字体颜色"""
    link: Union[TextElementLink, None] = None
    """链接"""
    comment_ids: Union[List[str], None] = None
    """评论 ID 列表"""


class TextRun(BaseModel):
    content: str
    """文本内容"""
    text_element_style: Union[TextElementStyle, None] = None
    """文本样式"""


class MentionUser(BaseModel):
    user_id: str
    """用户 OpenID"""
    text_element_style: Union[TextElementStyle, None] = None
    """文本样式"""


class MentionDoc(BaseModel):
    token: str
    """文档 Token"""
    obj_type: Union[DocType, None] = None
    """云文档类型"""
    url: str
    """云文档链接（需要 url_encode)"""
    title: str
    """文档标题，只读属性"""
    text_element_style: Union[TextElementStyle, None] = None
    """文本局部样式"""


class Reminder(BaseModel):
    create_user_id: str
    """创建者用户 ID"""
    is_notify: bool
    """是否通知"""
    is_whole_day: bool
    """是日期还是整点小时"""
    expire_time: str
    """事件发生的时间（毫秒级时间戳）"""
    notify_time: str
    """触发通知的时间（毫秒级时间戳）"""
    text_element_style: Union[TextElementStyle, None] = None
    """文本局部样式"""


class InlineFile(BaseModel):
    file_token: str
    """附件 token"""
    source_block_id: str
    """当前文档中该文件所处的 block 的 ID"""
    text_element_style: Union[TextElementStyle, None] = None
    """文本局部样式"""


class InlineBlock(BaseModel):
    block_id: str
    """关联的内联状态的 block 的 block_id"""
    text_element_style: Union[TextElementStyle, None] = None
    """文本局部样式"""


class Equation(BaseModel):
    content: str
    """符合 KaTeX 语法的公式内容，语法规则请参考：https://katex.org/docs/supported.html"""
    text_element_style: Union[TextElementStyle, None] = None


class TextElement(BaseModel):
    text_run: Union[TextRun, None] = None
    """文字。支持对 Page、Text、Heading1~9、Bullet、Ordered、Code、Quote、Todo 块进行修改"""
    mention_user: Union[MentionUser, None] = None
    """@用户。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改。"""
    mention_doc: Union[MentionDoc, None] = None
    """@文档。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改"""
    reminder: Union[Reminder, None] = None
    """日期提醒。支持对 Text、Heading1~9、Bullet、Ordered、Quote、Todo 块进行修改"""
    file: Union[InlineFile, None] = None
    """内联文件。仅支持删除或移动位置，不支持创建新的内联文件"""
    inline_block: Union[InlineBlock, None] = None
    """内联块。仅支持删除或移动位置，不支持创建新的内联块"""
    equation: Union[Equation, None] = None
    """公式"""


class Text(BaseModel):
    style: Union[TextStyle, None] = None
    """文本样式"""
    elements: Union[List[TextElement], None] = None
    """文本元素"""


class Bitable(BaseModel):
    token: str
    """多维表格 Token"""


class Callout(BaseModel):
    backgroud_color: Union[TextElementBackgroundColor, None] = None
    border_color: Union[BorderColor, None] = None
    text_color: Union[TextElementTextColor, None] = None
    emoji_id: Union[str, None] = None
    """todo"""


class ChatCard(BaseModel):
    chat_id: str
    align: Union[TextStyleAlign, None] = None


class Diagram(BaseModel):
    diagram_type: DiagramType


class Divider(BaseModel):
    pass


class File(BaseModel):
    token: str
    name: str
    view_type: ViewType


class Grid(BaseModel):
    column_size: int


class GridColumn(BaseModel):
    width_ratio: int


class IframeComponent(BaseModel):
    iframe_type: IframeType
    url: str


class Iframe(BaseModel):
    component: IframeComponent


class Image(BaseModel):
    width: int
    """图片宽度px"""
    height: int
    """图片高度px"""
    token: str
    """图片 Token"""
    align: Union[TextStyleAlign, None] = None


class ISVWidget(BaseModel):
    component_id: str
    """团队互动应用唯一ID"""
    component_type_id: str
    """团队互动应用类型，比如信息收集"blk_5f992038c64240015d280958" """


class AddOns(BaseModel):
    component_id: str
    """文档小组件 ID"""
    component_type_id: str
    """文档小组件类型，比如问答互动"blk_636a0a6657db8001c8df5488" """
    record: str
    """文档小组件内容数据，JSON 字符串"""


class MindNode(BaseModel):
    token: str
    """思维导图 Token"""


class Sheet(BaseModel):
    token: str
    """电子表格 Token"""


class TableMergeInfo(BaseModel):
    row_span: int
    """从当前行索引起被合并的连续行数"""
    col_span: int
    """从当前列索引起被合并的连续列数"""


class TableProperty(BaseModel):
    row_size: int
    """行数"""
    column_size: int
    """列数"""
    column_width: Union[List[int], None] = None
    """列宽，单位px"""
    merge_info: Union[List[TableMergeInfo]] = None
    """单元格合并信息。创建 Table 时，此属性只读，将由系统自动生成。如果需要合并单元格，可以通过更新块接口的子请求 merge_table_cells 实现"""
    header_row: Union[bool, None] = None
    """设置首行为标题行"""
    header_column: Union[bool, None] = None
    """设置首列为标题列"""


class Table(BaseModel):
    cells: List[str]
    """单元格数组，数组元素为 Table Cell Block 的 ID"""
    property: TableProperty
    """表格属性"""


class TableCell(BaseModel):
    pass


class Undefined(BaseModel):
    pass


class QuoteContainer(BaseModel):
    pass


class Task(BaseModel):
    task_id: str
    """任务 ID，查询具体任务详情见 https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/task-v2/task/get"""
    folded: bool


class OKRPeriodStatus(enum.Enum):
    DEFAULT = "default"
    NORMAL = "normal"
    INVALID = "invalid"
    HIDDEN = "hidden"


class OKRVisibleSetting(BaseModel):
    progress_fill_area_visible: bool
    """进展编辑区域是否可见"""
    progress_status_visible: bool
    """进展状态是否可见"""
    score_visible: bool
    """分数是否可见"""


class OKR(BaseModel):
    okr_id: str
    """OKR ID，获取需要插入的 OKR ID 可见"""
    period_display_status: OKRPeriodStatus
    period_name_zh: str
    """周期名 - 中文"""
    period_name_en: str
    """周期名 - 英文"""
    user_id: str
    """OKR 所属的用户 ID"""
    visible_setting: OKRVisibleSetting
    """OKR 可见性设置"""


class OKRProgressRate(BaseModel):
    mode: Literal["simple", "advanced"]
    current: Union[float, None] = None
    percent: Union[float, None] = None
    progress_status: Literal[
        "unset",
        "normal",
        "risk",
        "extended",
    ]
    start: Union[float, None] = None
    status_type: Literal["default", "custom"]
    target: Union[float, None] = None


class OKRObjective(BaseModel):
    objective_id: str
    """Objective ID"""
    confidential: bool
    """是否在 OKR 平台设置了私密权限"""
    position: int
    """是否在 OKR 平台设置了私密权限"""
    score: int
    """打分信息"""
    visible: bool
    """OKR Block 中是否展示该 Objective"""
    weight: float
    """Objective 的权重"""
    progress_rate: OKRProgressRate
    """进展信息"""
    content: Text
    """Objective 的文本内容"""


class OKRKeyResult(BaseModel):
    kr_id: str
    """Key Result 的 ID"""
    confidential: bool
    """是否在 OKR 平台设置了私密权限"""
    position: int
    """Key Result 的位置编号，对应 Block 中 KR1、KR2 的 1、2。"""
    score: int
    """打分信息"""
    visible: bool
    """OKR Block 中是否展示该 Key Result"""
    weight: float
    """Key Result 的权重"""
    progress_rate: OKRProgressRate
    """进展信息"""
    content: Text
    """Key Result 的文本内容"""


class OKRProgress(BaseModel):
    pass


class JiraIssue(BaseModel):
    id: str
    """Jira 问题 ID"""
    key: str
    """Jira 问题 key"""


class WikiCatalog(BaseModel):
    wiki_token: str
    """知识库 token"""


class Board(BaseModel):
    token: str
    """画板 Token"""
    align: Union[TextStyleAlign, None] = None
    width: Union[int, None] = None
    """宽度，单位 px；不填时自动适应文档宽度；值超出文档最大宽度时，页面渲染为文档最大宽度"""
    height: Union[int, None] = None
    """高度，单位 px；不填时自动适应内容高度；值超出文档最大高度时，页面渲染为文档最大高度"""


class Agenda(BaseModel):
    pass


class AgendaItem(BaseModel):
    pass


class AgendaItemTitleElement(BaseModel):
    text_run: Union[TextRun, None] = None
    mention_user: Union[MentionUser, None] = None
    mention_doc: Union[MentionDoc, None] = None
    reminder: Union[Reminder, None] = None
    file: Union[InlineFile, None] = None
    undefined: Union[Undefined, None] = None
    inline_block: Union[InlineBlock, None] = None
    equation: Union[Equation, None] = None


class AgendaItemContent(BaseModel):
    pass


class AgendaItemTitle(BaseModel):
    elements: List[AgendaItemTitleElement]
    align: Union[TextStyleAlign, None] = None
    agenda_item_content: AgendaItemContent


class LinkPreview(BaseModel):
    url_type: Literal["MessageLink", "Undefined"]


class BlockInfo(BaseModel):
    block_id: str
    """子块的唯一标识"""
    block_type: BlockType
    """Block 类型"""
    parent_id: Union[str, None] = None
    """子块的父块 ID"""
    children: Union[List[str], None] = None
    """子块的子块 ID 列表"""
    page: Union[Text, None] = None
    """文档的根 Block，也称页面 Block"""
    text: Union[Text, None] = None
    heading1: Union[Text, None] = None
    heading2: Union[Text, None] = None
    heading3: Union[Text, None] = None
    heading4: Union[Text, None] = None
    heading5: Union[Text, None] = None
    heading6: Union[Text, None] = None
    heading7: Union[Text, None] = None
    heading8: Union[Text, None] = None
    heading9: Union[Text, None] = None
    bullet: Union[Text, None] = None
    ordered: Union[Text, None] = None
    code: Union[Text, None] = None
    quote: Union[Text, None] = None
    equation: Union[Equation, None] = None
    todo: Union[Text, None] = None
    bitable: Union[Bitable, None] = None
    callout: Union[Callout, None] = None
    chat_card: Union[ChatCard, None] = None
    diagram: Union[Diagram, None] = None
    divider: Union[Divider, None] = None
    file: Union[File, None] = None
    grid: Union[Grid, None] = None
    grid_column: Union[GridColumn, None] = None
    iframe: Union[Iframe, None] = None
    image: Union[Image, None] = None
    isv: Union[ISVWidget, None] = None
    add_ons: Union[AddOns, None] = None
    mindnote: Union[MindNode, None] = None
    sheet: Union[Sheet, None] = None
    table: Union[Table, None] = None
    table_cell: Union[TableCell, None] = None
    view: Union[ViewType, None] = None
    undefined: Union[Undefined, None] = None
    quote_container: Union[QuoteContainer, None] = None
    task: Union[Task, None] = None
    okr: Union[OKR, None] = None
    okr_objective: Union[OKRObjective, None] = None
    okr_key_result: Union[OKRKeyResult, None] = None
    okr_progress: Union[OKRProgress, None] = None
    comment_ids: Union[List[str], None] = None
    jira_issue: Union[JiraIssue, None] = None
    wiki_catalog: Union[WikiCatalog, None] = None
    board: Union[Board, None] = None
    agenda: Union[Agenda, None] = None
    agenda_item: Union[AgendaItem, None] = None
    agenda_item_title: Union[AgendaItemTitle, None] = None
    link_preview: Union[LinkPreview, None] = None
