# Slark

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

Read table

```python
await lark.sheets.read(url, start_row=0, rows=50, has_header=True)
```

Write table

```python
await lark.sheets.write(url, data=df, start_row=0, start_col=2)
await lark.sheets.append(url, data=df, start_row=0, start_col=2)
await lark.sheets.prepend(url, data=df, start_row=0, start_col=2)
```


Send webhook message

```python
await lark.webhook.xxxx
```