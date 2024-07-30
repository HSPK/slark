from slark.types._common import BaseModel


class GetTenantAccessTokenParams(BaseModel):
    app_id: str
    """应用唯一标识，创建应用后获得。有关app_id 的详细介绍。
    请参考通用参数介绍 https://open.feishu.cn/document/server-docs/api-call-guide/terminology"""
    app_secret: str
    """应用秘钥，创建应用后获得。有关 app_secret 的详细介绍，请参考通用参数介绍"""
