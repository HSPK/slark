from typing import List, Union

from slark.types._common import BaseModel

from .common import TableData


class CreateTableBody(BaseModel):
    table: TableData


class BatchCreateTableData(BaseModel):
    name: str


class BatchCreateTableBody(BaseModel):
    tables: List[BatchCreateTableData]


class BatchCreateTableParams(BaseModel):
    user_id_type: Union[str, None] = None


class BatchDeleteTableBody(BaseModel):
    table_ids: List[str]
    """待删除的数据表的id [table_id 参数说明]，当前一次操作最多支持50个数据表(/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/bitable/notification#735fe883)

    示例值：["tbl1TkhyTWDkSoZ3"]"""


class UpdateTableBody(BaseModel):
    name: str
    r"""	
    数据表的新名称。

    请注意：

    名称中的首尾空格将会被去除。

    如果名称为空或和旧名称相同，接口仍然会返回成功，但是名称不会被更改。

    示例值："数据表的新名称"

    数据校验规则：

    长度范围：1 字符 ～ 100 字符
    正则校验：^[^\[\]\:\\\/\?\*]+$"""


class ListTableParams(BaseModel):
    page_token: Union[str, None] = None
    """分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果

    示例值：tblsRc9GRRXKqhvW"""
    page_size: Union[int, None] = None
    """分页大小

    示例值：10

    默认值：20

    数据校验规则：

    最大值：100"""
