from typing import Union

import anyio
import httpx
import pandas as pd
from httpx import Response
from PIL import Image, ImageChops

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH


def trim(im_path: str, save_path: str):
    im = Image.open(im_path)
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        im = im.crop(bbox)
        im.save(save_path)


class AsyncBoard(AsyncAPIResource):
    async def download_as_image(
        self,
        whiteboard_id: str,
        *,
        save_dir: str,
        auto_trim: bool = True,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> pd.DataFrame:
        """下载白板为图片。
        通过此接口，可以将白板下载为图片，支持下载为 png、jpg、jpeg 格式。

        Args:
            whiteboard_id (str): 白板 ID。
            save_dir (str): 保存图片的目录。
            auto_trim (bool, optional): 是否自动裁剪图片。 Defaults to True.
            timeout (Union[httpx.Timeout, None], optional): 超时时间。 Defaults to None.

        Returns:
            str: 保存的图片路径。
        """
        response = await self._get(
            API_PATH.board.download_as_image.format(whiteboard_id=whiteboard_id),
            options={
                "timeout": timeout,
                "headers": {"Content-Type": "image/png"},
                "raw_response": True,
            },
            cast_to=Response,
        )

        save_dir_path = anyio.Path(save_dir)
        await save_dir_path.mkdir(exist_ok=True)
        file_path = save_dir_path / f"{whiteboard_id}.png"
        f = await anyio.open_file(file_path, "wb")
        await f.write(response.content)
        await f.aclose()
        if auto_trim:
            trim(file_path, file_path)
        return file_path
