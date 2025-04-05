from slark.resources._resources import APIResource, AsyncAPIResource
from slark.resources.knowledge_space.nodes import AsyncNodes, Nodes
from slark.types._utils import cached_property


class AsyncKnowledgeSpace(AsyncAPIResource):
    @cached_property
    def nodes(self):
        return AsyncNodes(client=self._client)


class KnowledgeSpace(APIResource):
    @cached_property
    def nodes(self):
        return Nodes(client=self._client)
