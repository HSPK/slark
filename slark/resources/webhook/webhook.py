from typing import Union

import httpx

from slark.resources._resources import AsyncAPIResource
from slark.types.card.card import InteractiveCard
from slark.types.response import BaseResponse
from slark.utils import card_builder as builder
from slark.utils.time import datetime_now


class AsyncWebhook(AsyncAPIResource):
    async def send_card(
        self, card: InteractiveCard, timeout: Union[httpx.Timeout, None] = None
    ) -> BaseResponse:
        return await self._post(
            self._client._webhook_url,
            body={
                "msg_type": "interactive",
                "card": card.model_dump(),
            },
            cast_to=BaseResponse,
            options={"timeout": timeout, "no_auth": True},
        )

    async def post_error_card(
        self,
        msg: str,
        traceback: str,
        title,
        subtitle: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        if subtitle is None:
            subtitle = datetime_now()
        return await self.send_card(
            builder.build_error_msg_card(msg, traceback, title, subtitle),
            timeout=timeout,
        )

    async def post_success_card(
        self,
        msg: str,
        title,
        subtitle: Union[str, None] = None,
        timeout: Union[httpx.Timeout, None] = None,
    ):
        if subtitle is None:
            subtitle = datetime_now()
        return await self.send_card(
            builder.build_success_msg_card(msg, title, subtitle),
            timeout=timeout,
        )
