from slark.resources._resources import AsyncAPIResource
from slark.types._utils import cached_property

from .data import AsyncData
from .table import AsyncTable
from .worksheet import AsyncWorksheet


class AsyncSpreadsheets(AsyncAPIResource):
    @cached_property
    def table(self):
        return AsyncTable(client=self._client)

    @cached_property
    def worksheet(self):
        return AsyncWorksheet(client=self._client)

    @cached_property
    def data(self):
        return AsyncData(client=self._client)
