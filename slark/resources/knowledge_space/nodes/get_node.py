from slark.tools._request import get
from slark.tools.api_route import API_ROUTE as route
from slark.types.exceptions import errors as err
from slark.types.knowledge_space.nodes.request import GetNodeQuery
from slark.types.knowledge_space.nodes.response import GetNodeResponse


async def get_node_info(query: GetNodeQuery):
    res = await get(route.knowledge_space.nodes.get_node, params=query.model_dump())
    try:
        node_info = GetNodeResponse.model_validate_json(res.text)
    except Exception as e:
        raise err.BadResponseError(
            f"Can't validate get node response: {e}", context={"res": res.json()}
        ) from None
    return node_info
