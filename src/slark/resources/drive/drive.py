import re
from typing import Union

import httpx
from pydantic import BaseModel

from slark.resources._resources import APIResource, AsyncAPIResource
from slark.resources.drive.file import AsyncFile, File
from slark.types._utils import cached_property


class FileInfo(BaseModel):
    file_token: str


class AsyncDrive(AsyncAPIResource):
    @cached_property
    def file(self):
        return AsyncFile(client=self._client)

    async def get_file_info(self, url: str) -> FileInfo:
        if "/file/" in url:
            file_token = re.findall(r"\/file\/([^\/\?]+)", url)[0]
        else:
            raise ValueError("The url is not a file url")
        return FileInfo(file_token=file_token)

    async def download_file(
        self,
        url: str,
        *,
        save_dir: str,
        range: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        info = await self.get_file_info(url)
        return await self.file.download(
            info.file_token, save_dir=save_dir, range=range, timeout=timeout
        )


class Drive(APIResource):
    @cached_property
    def file(self):
        return File(client=self._client)

    def get_file_info(self, url: str) -> FileInfo:
        if "/file/" in url:
            file_token = re.findall(r"\/file\/([^\/\?]+)", url)[0]
        else:
            raise ValueError("The url is not a file url")
        return FileInfo(file_token=file_token)

    def download_file(
        self,
        url: str,
        *,
        save_dir: str,
        range: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        info = self.get_file_info(url)
        return self.file.download(info.file_token, save_dir=save_dir, range=range, timeout=timeout)
