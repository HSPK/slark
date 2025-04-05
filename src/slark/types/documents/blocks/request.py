from typing import Union

from typing_extensions import Literal

from slark.types._common import BaseModel


class GetAllBlocksParams(BaseModel):
    page_size: Union[int, None] = None
    """分页大小,默认值/最大值：500"""
    page_token: Union[str, None] = None
    """分页标记，第一次请求不填，表示从头开始遍历；\
        分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果"""
    document_revision_id: Union[int, None] = None
    """查询的文档版本，-1 表示文档最新版本。文档创建后，版本为 1。\
        若查询的版本为文档最新版本，则需要持有文档的阅读权限；若查询的版本为文档的历史版本，则需要持有文档的编辑权限。"""
    user_id_type: Union[Literal["open_id", "union_id", "user_id"], None] = None
    """用户 ID 类型。\
        示例值："open_id"。\
        可选值有：\n
        open_id：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。了解更多：如何获取 Open ID\n
        union_id：标识一个用户在某个应用开发商下的身份。\
            同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，\
            应用开发商可以把同个用户在多个应用中的身份关联起来。了解更多：如何获取 Union ID？\n
        user_id：标识一个用户在某个租户内的身份。\
            同一个用户在租户 A 和租户 B 内的 User ID 是不同的。\
            在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。\
            User ID 主要用于在不同的应用间打通用户数据。了解更多：如何获取 User ID？"""
