from typing import Any, Union

import httpx
from requests_toolbelt import MultipartEncoder
from typing_extensions import Literal

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.messages.image.response import UploadImageResponse


class AsyncImage(AsyncAPIResource):
    async def upload(
        self,
        image: Any,
        image_type: Literal["message", "avatar"] = "message",
        timeout: Union[httpx.Timeout, None] = None,
    ) -> UploadImageResponse:
        """上传图片

        Args:
            image_type (str): 图片类型\
                示例值："message"\
                可选值有：\
                    message：用于发送消息\
                    avatar：用于设置头像\
            
            image (Any): 图片内容。传值方式可以参考请求体示例。\
                注意：\
                上传的图片大小不能超过 10 MB，也不能上传大小为 0 的图片。\
                分辨率限制：\
                GIF 图片分辨率不能超过 2000 x 2000，其他图片分辨率不能超过 12000 x 12000。\
                用于设置头像的图片分辨率不能超过 4096 x 4096。\
                示例值：二进制文件\
                
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            UploadImageResponse: 返回值
        """
        m = MultipartEncoder(
            fields={
                "image_type": image_type,
                "image": ("image", image),
            }
        )
        return await self._post(
            API_PATH.image.upload,
            cast_to=UploadImageResponse,
            options={
                "content": m.read(),
                "timeout": timeout,
                "headers": {
                    "Content-Type": m.content_type,
                },
            },
        )
