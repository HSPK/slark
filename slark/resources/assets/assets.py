import re
from typing import Union

import anyio
import httpx
from httpx import Response
from pydantic import BaseModel

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH


class DownloadFileInfo(BaseModel):
    filepath: str
    filename: str
    filetype: str


class AsyncAssets(AsyncAPIResource):
    async def download(
        self,
        file_token: str,
        *,
        save_dir: str,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> DownloadFileInfo:
        response = await self._get(
            API_PATH.assets.download.format(file_token=file_token),
            options={
                "timeout": timeout,
                "raw_response": True,
            },
            cast_to=Response,
        )
        mime_type = response.headers["Content-Type"]
        filename = re.findall(r'filename="(.+)"', response.headers["Content-Disposition"])[0]
        filename = f"{file_token}_{filename}"
        path = anyio.Path(save_dir) / filename
        await path.parent.mkdir(parents=True, exist_ok=True)
        f = await anyio.open_file(path, "wb")
        await f.write(response.content)
        await f.aclose()
        return DownloadFileInfo(
            filepath=path.as_posix(),
            filename=filename,
            filetype=mime_type,
        )
