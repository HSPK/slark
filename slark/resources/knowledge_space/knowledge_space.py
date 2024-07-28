from slark.resources._resources import AsyncAPIResource
from slark.types._utils import cached_property
from slark.resources.knowledge_space.nodes import Nodes


class KnowledgeSpace(AsyncAPIResource):
    @cached_property
    def nodes(self):
        return Nodes(client=self._client)
