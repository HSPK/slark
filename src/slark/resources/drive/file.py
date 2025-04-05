import mimetypes
from typing import Union

import anyio
import httpx
from httpx import Response

from slark.resources._resources import APIResource, AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.drive.file.response import FileInfo
from slark.utils import extract_filename


class AsyncFile(AsyncAPIResource):
    async def download(
        self,
        file_token: str,
        *,
        save_dir: str,
        range: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> FileInfo:
        """下载云空间中的文件，如 PDF 文件。不包含飞书文档、电子表格以及多维表格等在线文档。该接口支持通过在请求头添加 Range 参数分片下载部分文件。
        调用此接口之前，你需确保应用已拥有文件的下载权限。否则接口将返回 403 的 HTTP 状态码。
        本接口仅支持下载云空间中的资源文件。要下载云文档中的素材（如图片、附件等），需调用下载素材接口。
        
        https://open.feishu.cn/document/server-docs/docs/drive-v1/download/download
        
        Args:
            file_token (str): 文件的 token。
            save_dir (str): 保存文件的目录。
            range (str): 在 HTTP 请求头中，通过指定 Range 来下载文件的部分内容，单位是字节（byte）。\
                该参数的格式为 Range: bytes=start-end.\\
                示例值为 Range: bytes=0-1024，表示下载第 0 个字节到第 1024 个字节之间的数据。
            timeout (Union[httpx.Timeout, None], optional): 超时时间。 Defaults to None.

        Returns:
            response: \
                Content-Type 文件的MIME，比如：application/vnd.openxmlformats-officedocument.wordprocessingml.document
                Content-Disposition: 文件名
        """
        response: Response = await self._get(
            API_PATH.drive.file.download.format(file_token=file_token),
            options={
                "timeout": timeout,
                "headers": {"Range": range} if range else {},
                "raw_response": True,
            },
            cast_to=Response,
        )
        mime_type = response.headers["Content-Type"]
        ext = mimetypes.guess_extension(mime_type)
        file_name = response.headers["Content-Disposition"]
        file_name = extract_filename(file_name)

        save_dir_path = anyio.Path(save_dir)
        await save_dir_path.mkdir(exist_ok=True)
        file_path = save_dir_path / f"{file_token}{ext}"

        f = await anyio.open_file(file_path, "wb")
        await f.write(response.content)
        await f.aclose()

        return FileInfo(
            file_path=file_path.as_posix(),
            file_token=file_token,
            file_name=file_name,
            mime_type=mime_type,
        )


class File(APIResource):
    def download(
        self,
        file_token: str,
        *,
        save_dir: str,
        range: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> FileInfo:
        """下载云空间中的文件，如 PDF 文件。不包含飞书文档、电子表格以及多维表格等在线文档。该接口支持通过在请求头添加 Range 参数分片下载部分文件。
        调用此接口之前，你需确保应用已拥有文件的下载权限。否则接口将返回 403 的 HTTP 状态码。
        本接口仅支持下载云空间中的资源文件。要下载云文档中的素材（如图片、附件等），需调用下载素材接口。
        
        https://open.feishu.cn/document/server-docs/docs/drive-v1/download/download
        
        Args:
            file_token (str): 文件的 token。
            save_dir (str): 保存文件的目录。
            range (str): 在 HTTP 请求头中，通过指定 Range 来下载文件的部分内容，单位是字节（byte）。\
                该参数的格式为 Range: bytes=start-end.\\
                示例值为 Range: bytes=0-1024，表示下载第 0 个字节到第 1024 个字节之间的数据。
            timeout (Union[httpx.Timeout, None], optional): 超时时间。 Defaults to None.

        Returns:
            response: \
                Content-Type 文件的MIME，比如：application/vnd.openxmlformats-officedocument.wordprocessingml.document
                Content-Disposition: 文件名
        """
        response: Response = self._get(
            API_PATH.drive.file.download.format(file_token=file_token),
            options={
                "timeout": timeout,
                "headers": {"Range": range} if range else {},
                "raw_response": True,
            },
            cast_to=Response,
        )
        mime_type = response.headers["Content-Type"]
        ext = mimetypes.guess_extension(mime_type)
        file_name = response.headers["Content-Disposition"]
        file_name = extract_filename(file_name)

        save_dir_path = anyio.Path(save_dir)
        save_dir_path.mkdir(exist_ok=True)
        file_path = save_dir_path / f"{file_token}{ext}"

        with anyio.open_file(file_path, "wb") as f:
            f.write(response.content)

        return FileInfo(
            file_path=file_path.as_posix(),
            file_token=file_token,
            file_name=file_name,
            mime_type=mime_type,
        )
