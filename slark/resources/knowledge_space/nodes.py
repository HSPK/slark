from typing import Union

import httpx

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.knowledge_space.nodes.request import GetNodeQuery, NodeTypes
from slark.types.knowledge_space.nodes.response import GetNodeResponse


class Nodes(AsyncAPIResource):
    async def get_node_info(
        self,
        token: str,
        obj_type: NodeTypes = "wiki",
        timeout: Union[httpx.Timeout, None] = None,
    ) -> GetNodeResponse:
        return await self._get(
            API_PATH.knowledge_space.nodes.get_node,
            cast_to=GetNodeResponse,
            options={
                "timeout": timeout,
                "params": GetNodeQuery(token=token, obj_type=obj_type).model_dump(),
            },
        )
