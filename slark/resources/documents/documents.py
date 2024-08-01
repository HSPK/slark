import re
from typing import List, Union

import httpx
import pandas as pd
from pydantic import BaseModel
from typing_extensions import Literal

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types._utils import cached_property
from slark.types.documents.request import GetRawContentParams
from slark.types.documents.response import GetRawContentResponse

from .blocks import AsyncBlocks


class DocumentInfo(BaseModel):
    document_id: str


class AsyncDocuments(AsyncAPIResource):
    @cached_property
    def blocks(self) -> AsyncBlocks:
        return AsyncBlocks(self._client)

    async def get_raw_content(
        self,
        document_id: str,
        *,
        lang: Union[Literal[0, 1, 2], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> GetRawContentResponse:
        """获取文档的纯文本内容。
        应用频率限制：单个应用调用频率上限为每秒 5 次，超过该频率限制，\
            接口将返回 HTTP 状态码 400 及错误码 99991400。\
            当请求被限频，应用需要处理限频状态码，并使用指数退避算法或其它一些频控策略降低对 API 的调用速率。

        Args:
            document_id (str): 文档的唯一标识。
            lang (Union[Literal[0, 1, 2], None], optional): 指定返回的 MentionUser 即 @用户 的语言。可选值有：\n
                0：该用户的默认名称。如：@张敏\n
                1：该用户的英文名称。如：@Min Zhang\n
                2：暂不支持该枚举，使用时返回该用户的默认名称\n
                默认值：0. Defaults to None.
                
        Returns:
            GetRawContentResponse: 返回的文档内容。
        """
        return await self._get(
            API_PATH.documents.get_raw_content.format(document_id=document_id),
            cast_to=GetRawContentResponse,
            options={
                "timeout": timeout,
                "params": GetRawContentParams(lang=lang).model_dump(),
            },
        )

    async def get_document_info(self, url: str) -> DocumentInfo:
        """从文档分享链接中提取 document_id

        Args:
            url (str): URL of the document

        Returns:
            DocumentInfo: document_id
        """
        if "/docx/" in url:
            document_id = re.findall(r"\/docx\/([^\/\?]+)", url)[0]
        elif "/wiki/" in url:
            node_token = re.findall(r"\/wiki\/([^\/\?]+)", url)[0]
            node_info = await self._client.knowledge_space.nodes.get_node_info(node_token)
            if node_info.data.node.obj_type != "docx":
                raise ValueError(f"The node {node_info.data.node.obj_type} is not a document")
            document_id = node_info.data.node.obj_token
        else:
            raise ValueError("The url is not a document url")
        assert document_id, "Document token is not found"

        return DocumentInfo(document_id=document_id)

    async def read(
        self,
        url: str,
        *,
        lang: Union[Literal[0, 1, 2], None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> str:
        """从文档中读取纯文本内容

        Args:
            url (str): 文档分享链接
            lang (Union[Literal[0, 1, 2], None], optional): 指定返回的 MentionUser 即 @用户 的语言。可选值有：\n
                0：该用户的默认名称。如：@张敏\n
                1：该用户的英文名称。如：@Min Zhang\n
                2：暂不支持该枚举，使用时返回该用户的默认名称\n
                默认值：0. Defaults to None.
            timeout (Union[httpx.Timeout, None], optional): 超时时间. Defaults to None.

        Returns:
            str: 文档内容
        """
        document_id = (await self.get_document_info(url)).document_id
        return (await self.get_raw_content(document_id, lang=lang, timeout=timeout)).data.content
