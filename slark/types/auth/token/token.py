from time import time

from slark.types._common import BaseModel


class TokenBase(BaseModel):
    access_token: str
    """访问token"""
    expires_at: int
    """过期时间，单位为秒(从1970年1月1日0时0分0秒开始计算)"""

    @property
    def is_expired(self):
        return time() > self.expires_at

    def refresh(self):
        pass


class UserAccessToken(TokenBase):
    refresh_token: str
    """刷新user_access_token时使用的 refresh_token"""
    token_type: str
    """	token 类型，固定值"""
    refresh_expires_at: int
    """refresh_token有效期，单位: 秒，一般是30天左右，需要以返回结果为准"""
    scope: str
    """用户授予app的权限全集"""


class TenantAccessToken(TokenBase):
    pass
