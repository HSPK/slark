import re
from typing import List, Union

import httpx
import pandas as pd
from pydantic import BaseModel

from slark.resources._resources import AsyncAPIResource
from slark.types._utils import cached_property
from slark.types.bitables.record.response import RecordResponseData


class AsyncBlocks(AsyncAPIResource):
    pass