from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # The following settings are required
    base_url: str = "https://open.feishu.cn/open-apis/"
    access_token: str
