from typing import Union

import httpx

from slark.resources._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from slark.types.bitables.request import UpdateBitableMetaBody
from slark.types.bitables.response import GetBitableMetaResponse, UpdateBitableMetaResponse


class AsyncMeta(AsyncAPIResource):
    async def get(
        self,
        app_token: str,
        *,
        timeout: Union[httpx.Timeout, None] = None,
    ) -> GetBitableMetaResponse:
        """获取多维表格元数据 https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/get

        Args:
            app_token (str): 多维表格的 app_token
            timeout (Union[httpx.Timeout, None], optional): Timeout. Defaults to None.

        Returns:
            GetBitableMetaResponse: 多维表格元数据
        """
        return await self._get(
            API_PATH.bitables.get_bitable_meta.format(app_token=app_token),
            cast_to=GetBitableMetaResponse,
            options={"timeout": timeout},
        )

    async def update(
        self,
        app_token: str,
        *,
        name: Union[str, None] = None,
        is_advanced: Union[bool, None] = None,
    ) -> UpdateBitableMetaResponse:
        """更新多维表格元数据 https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/update

        Args:
            app_token (str): 多维表格的 app_token
            name (Union[str, None], optional): 更新表格的名字. Defaults to None.
            is_advanced (Union[bool, None], optional): 是否开启高级权限. Defaults to None.

        Returns:
            UpdateBitableMetaResponse: 更新返回值
        """
        return await self._put(
            API_PATH.bitables.update_bitable_meta.format(app_token=app_token),
            body=UpdateBitableMetaBody(
                name=name,
                is_advanced=is_advanced,
            ).model_dump(),
            cast_to=UpdateBitableMetaResponse,
        )
