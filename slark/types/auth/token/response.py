from slark.types.response import BaseResponse


class GetTenantAccessTokenResponse(BaseResponse):
    tenant_access_token: str
    """租户访问凭证"""
    expire: int
    """tenant_access_token 的过期时间，单位为秒"""
