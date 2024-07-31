from slark.resources._resources import AsyncAPIResource
from slark.types._utils import cached_property

from .field import AsyncField
from .meta import AsyncMeta
from .record import AsyncRecord
from .table import AsyncTable
from .view import AsyncView


class AsyncBiTable(AsyncAPIResource):
    @cached_property
    def field(self) -> AsyncField:
        return AsyncField(self._client)

    @cached_property
    def record(self) -> AsyncRecord:
        return AsyncRecord(self._client)

    @cached_property
    def view(self) -> AsyncView:
        return AsyncView(self._client)

    @cached_property
    def table(self) -> AsyncTable:
        return AsyncTable(self._client)

    @cached_property
    def meta(self) -> AsyncMeta:
        return AsyncMeta(self._client)
