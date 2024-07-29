from slark.types._utils import cached_property

from .._resources import AsyncAPIResource
from .token import Token


class AsyncAuth(AsyncAPIResource):
    @cached_property
    def token(self) -> Token:
        return Token(client=self._client)
