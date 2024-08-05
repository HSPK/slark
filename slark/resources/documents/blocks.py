from typing import Union

import httpx

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.documents.blocks.request import GetAllBlocksParams
from slark.types.documents.blocks.response import GetAllBlocksResponse


class AsyncBlocks(AsyncAPIResource):
    async def get_all(
        self,
        document_id: str,
        *,
        page_size: Union[int, None] = None,
        page_token: Union[str, None] = None,
        document_revision_id: Union[int, None] = None,
        user_id_type: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> GetAllBlocksResponse:
        """获取文档的全部 block 信息。
        应用频率限制：单个应用调用频率上限为每秒 5 次，超过该频率限制，接口将返回 HTTP 状态码 400 及错误码 99991400。当请求被限频，应用需要处理限频状态码，并使用指数退避算法或其它一些频控策略降低对 API 的调用速率。

        Args:
            document_id (str): 文档的唯一标识。
            page_size (Union[int, None], optional): 分页大小,默认值/最大值：500. Defaults to None.
            page_token (Union[str, None], optional): 分页标记，第一次请求不填，表示从头开始遍历；分页查询结果还有更多项时会同时返回新的 page_token，下次遍历可采用该 page_token 获取查询结果. Defaults to None.
            document_revision_id (Union[int, None], optional): 查询的文档版本，-1 表示文档最新版本。文档创建后，版本为 1。若查询的版本为文档最新版本，则需要持有文档的阅读权限；若查询的版本为文档的历史版本，则需要持有文档的编辑权限. Defaults to None.
            user_id_type (Union[str, None], optional): 用户 ID 类型。示例值："open_id"。可选值有：\n
                open_id：标识一个用户在某个应用中的身份。同一个用户在不同应用中的 Open ID 不同。了解更多：如何获取 Open ID\n
                union_id：标识一个用户在某个应用开发商下的身份。同一用户在同一开发商下的应用中的 Union ID 是相同的，在不同开发商下的应用中的 Union ID 是不同的。通过 Union ID，应用开发商可以
                把同个用户在多个应用中的身份关联起来。了解更多：如何获取 Union ID？\n
                user_id：标识一个用户在某个租户内的身份。同一个用户在租户 A 和租户 B 内的 User ID 是不同的。在同一个租户内，一个用户的 User ID 在所有应用（包括商店应用）中都保持一致。User ID 主要用于在不同的应用间打通用户数据。了解更多：如何获取 User ID？. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): 超时时间. Defaults to None.

        Returns:
            GetAllBlocksResponse: 返回的 block 信息。
        """
        return await self._get(
            API_PATH.documents.get_blocks.format(document_id=document_id),
            cast_to=GetAllBlocksResponse,
            options={
                "timeout": timeout,
                "params": GetAllBlocksParams(
                    page_size=page_size,
                    page_token=page_token,
                    document_revision_id=document_revision_id,
                    user_id_type=user_id_type,
                ).model_dump(),
            },
        )
