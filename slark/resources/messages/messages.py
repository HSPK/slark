from slark.resources._resources import AsyncAPIResource
from slark.types._utils import cached_property

from .image import AsyncImage


class AsyncMessages(AsyncAPIResource):
    @cached_property
    def image(self) -> AsyncImage:
        return AsyncImage(self._client)
