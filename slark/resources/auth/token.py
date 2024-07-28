from slark.types.auth import (
    GetTenantAccessTokenParams,
    GetTenantAccessTokenResponse,
    TenantAccessToken,
)
import httpx
from .._resources import AsyncAPIResource
from slark.resources.api_path import API_PATH
from time import time

NETWORK_DELAY_AJUSTMENT = 5


class Token(AsyncAPIResource):
    async def get_tenant_access_token(
        self, timeout: httpx.Timeout | None = None
    ) -> TenantAccessToken:
        response = await self._post(
            API_PATH.auth.get_tenant_access_token,
            cast_to=GetTenantAccessTokenResponse,
            body=GetTenantAccessTokenParams.model_validate(
                self._client.app_credentials
            ).model_dump(),
            options={"timeout": timeout, "no_auth": True},
        )
        return TenantAccessToken(
            access_token=response.tenant_access_token,
            expires_at=response.expire + int(time()) - NETWORK_DELAY_AJUSTMENT,
        )
