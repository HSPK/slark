# Slark

[![PyPI version](https://badge.fury.io/py/slark.svg)](https://badge.fury.io/py/slark)

Simple LARK(Feishu) SDK

# Usage

```
pip install slark
```

```python
from slark import AsyncLark

lark = AsyncLark(
    app_id=xxx, app_secret=xxx, webhook=xxx
)
```

## Spreadsheets

Read table

```python
await lark.sheets.read(
    url: str,
    *,
    start_row: int = 0,
    start_col: int = 0,
    rows: Union[int, None] = None,
    cols: Union[int, None] = None,
    has_header: bool = True,
    dropna: bool = True,
    valueRenderOption: Union[
        Literal["ToString", "Formula", "FormattedValue", "UnformattedValue"], None
    ] = None,
    dateTimeRenderOption: Union[Literal["FormattedString"], None] = None,
    user_id_type: Union[Literal["open_id", "union_id"], None] = None,
    return_raw: bool = False,
    timeout: Union[httpx.Timeout, None] = None,
)
    """从电子表格读取数据，该接口返回数据的最大限制为 10 MB。该接口不支持获取跨表引用和数组公式的计算结果。

    Args:
        url (str): 电子表格的 URL 链接
        start_row (int, optional): 起始行数. Defaults to 0.
        start_col (int, optional): 起始列数. Defaults to 0.
        rows (Union[int, None], optional): 读取行数. Defaults to None.
        cols (Union[int, None], optional): 读取列数. Defaults to None.
        has_header (bool, optional): 是否包括标题. Defaults to True.
        dropna (bool, optional): 是否去除全为空的行/列. Defaults to True.
        valueRenderOption (Literal[ &quot;ToString&quot;, &quot;Formula&quot;, &quot;FormattedValue&quot;, &quot;UnformattedValue&quot; ], None, optional): \
            指定单元格数据的格式。可选值如下所示。\
            当参数缺省时，默认不进行公式计算，返回公式本身，且单元格为数值格式。\
            ToString：返回纯文本的值（数值类型除外）。\
            Formula：单元格中含有公式时，返回公式本身。\
            FormattedValue：计算并格式化单元格。\
            UnformattedValue：计算但不对单元格进行格式化. Defaults to None.
        dateTimeRenderOption (Literal[&quot;FormattedString&quot;], None, optional):\
            指定数据类型为日期、时间、或时间日期的单元格数据的格式。\
            若不传值，默认返回浮点数值，整数部分为自 1899 年 12 月 30 日以来的天数；\
            小数部分为该时间占 24 小时的份额。\
            例如：若时间为 1900 年 1 月 1 日中午 12 点，则默认返回 2.5。\
            其中，2 表示 1900 年 1 月 1 日为 1899 年12 月 30 日之后的 2 天；\
            0.5 表示 12 点占 24 小时的二分之一，即 12/24=0.5。\
            可选值为 FormattedString，此时接口将计算并对日期、时间、或时间日期类型的数据格式化并返回格式化后的字符串，但不会对数字进行格式化。. Defaults to None.
        user_id_type (Literal[&quot;open_id&quot;, &quot;union_id&quot;], None, optional):\
            当单元格中包含@用户等涉及用户信息的元素时，该参数可指定返回的用户 ID 类型。\
            默认为 lark_id，建议选择 open_id 或 union_id. Defaults to None.
        timeout (Union[httpx.Timeout, None], optional): _description_. Defaults to None.

    Returns:
        Union[pd.DataFrame, List[List[CellTypes]]]: 读取的数据，\
            如果 return_raw 为 True 则返回 List[List[CellTypes]]，否则返回 pd.DataFrame
    """
```

Write table

```python
await lark.sheets.write(url, data=df, start_row=0, start_col=2)
await lark.sheets.append(url, data=df, start_row=0, start_col=2)
await lark.sheets.prepend(url, data=df, start_row=0, start_col=2)
```

## Webhook

Send webhook message

```python
await lark.webhook.post_error_card(
    self,
    msg: str,
    traceback: str,
    title,
    subtitle: Union[str, None] = None,
    timeout: Union[httpx.Timeout, None] = None,
)

await lark.webhook.post_success_card(
    self,
    msg: str,
    title,
    subtitle: Union[str, None] = None,
    timeout: Union[httpx.Timeout, None] = None,
)
```

## Bitables

1. Read
   
```python
await lark.bitables.read(
    url: str,
    *,
    rows: Union[int, None] = None,
    field_names: Union[List[str], None] = None,
    return_raw: bool = False,
    timezone: Union[str, None] = "Asia/Shanghai",
    timeout: Union[httpx.Timeout, None] = None,
)
    """从多维表格中读取数据

    Args:
        url (str): 多维表格分享链接
        rows (Union[int, None], optional): 读取的行数. Defaults to None.
        field_names (Union[List[str], None], optional): 读取的列名. Defaults to None.
        raw (bool, optional): 是否返回原始数据. Defaults to False.
        timezone (Union[str, None], optional): 时区，仅在raw=False时有效. Defaults to "Asia/Shanghai".

    Returns:
        Union[dict, pd.DataFrame]: 当raw=True时返回原始数据，否则返回DataFrame\
            返回的 dataframe 的 index 为对应记录的 record id
    """
```

2. Append

```python
await lark.bitables.append(
    url: str,
    *,
    data: pd.DataFrame,
    timezone: Union[str, None] = "Asia/Shanghai",
    timeout: Union[httpx.Timeout, None] = None,
)
    """向多维表格中追加数据

    Args:
        url (str): 多维表格分享链接
        data (pd.DataFrame): 要追加的数据
        timezone (Union[str, None], optional): 时区. Defaults to "Asia/Shanghai".
        timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

    Returns:
        List[RecordResponseData]: 追加的数据
    """
```

3. Update

```python
await lark.bitables.update(
    url: str,
    *,
    data: pd.DataFrame,
    timezone: Union[str, None] = "Asia/Shanghai",
    timeout: Union[httpx.Timeout, None] = None,
)
    """更新多维表格中的数据

    Args:
        url (str): 多维表格分享链接
        data (pd.DataFrame): 要更新的数据，index 为更新记录的 record id
        timezone (Union[str, None], optional): 时区. Defaults to "Asia/Shanghai".
        timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

    Returns:
        List[RecordResponseData]: 更新的数据
    """
```

4. Delete

```python
await lark.bitables.delete(
    url: str, *, record_ids: List[str], timeout: Union[httpx.Timeout, None] = None
)
    """删除多维表格中的数据

    Args:
        url (str): 多维表格分享链接
        record_ids (List[str]): 要删除的记录ID
        timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.
    """
```

## Document

1. Read to Markdown

```python
await lark.docs.read_markdown(
    url: str,
    *,
    assets_path: str = "./assets/",
    timeout: Union[httpx.Timeout, None] = None,
)
    """从文档中读取 markdown 内容

    Args:
        url (str): 文档分享链接。
        assets_path (str, optional): 保存图片的目录. Defaults to "./assets/".
        timeout (Union[httpx.Timeout, None], optional): 超时时间. Defaults to None.

    Returns:
        str: markdown 内容
    """
```

### 目前支持的文档元素：

1. 文本，格式包括超链接、粗体、斜体、下划线、删除线，不支持字体颜色、背景颜色
2. 标题，支持 1-9 级标题
3. 有序列表
4. 无序列表
5. 代码块
6. 引用
7. 公式
8. 待办事项，支持勾选和未勾选状态，不支持用户
9. 高亮块
10. 分割线
11. 图片
12. 表格
13. 画板（导出为图片）

暂不支持的元素：
1. 指定@用户
2. 评论
3. 文件
4. 多维表格
5. 群聊卡片
6. 链接卡片（官方不支持）
7. 分栏布局
8. iframe
9. 三方应用
10. 任务
11. OKR
12. Jira问题
13. 议程

