import os
from typing import Union

import httpx
from loguru import logger

from slark import resources
from slark._constants import DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT
from slark.client._client import AsyncAPIClient
from slark.types.auth import CredentailTypes, TokenBase


class AsyncLark(AsyncAPIClient):
    auth: resources.AsyncAuth
    webhook: resources.AsyncWebhook
    knowledge_space: resources.KnowledgeSpace
    sheets: resources.AsyncSpreadsheets
    bitables: resources.AsyncBiTable
    docs: resources.AsyncDocuments
    board: resources.AsyncBoard
    assets: resources.AsyncAssets
    messages: resources.AsyncMessages

    _app_id: Union[str, None]
    _app_secret: Union[str, None]
    _webhook_url: Union[str, None]
    _token: Union[TokenBase, None]
    _token_type: CredentailTypes

    def __init__(
        self,
        *,
        app_id: Union[str, None] = None,
        app_secret: Union[str, None] = None,
        webhook: Union[str, None] = None,
        verification_token: Union[str, None] = None,
        encrypt_key: Union[str, None] = None,
        base_url: Union[str, httpx.URL] = "https://open.feishu.cn/open-apis/",
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: httpx.Timeout = DEFAULT_TIMEOUT,
        proxies: Union[httpx._types.ProxyTypes, None] = None,
        token_type: CredentailTypes = "tenant",
    ):
        self._app_id = app_id or os.getenv("APP_ID", None)
        self._app_secret = app_secret or os.getenv("APP_SECRET", None)
        self._webhook_url = webhook or os.getenv("WEBHOOK_URL", None)
        self._verification_token = verification_token or os.getenv("VERIFICATION_TOKEN", None)
        self._encrypt_key = encrypt_key or os.getenv("ENCRYPT_KEY", None)
        self._token = None
        self._token_type = token_type

        super().__init__(
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            proxies=proxies,
        )

        self.auth = resources.AsyncAuth(self)
        self.webhook = resources.AsyncWebhook(self)
        self.knowledge_space = resources.KnowledgeSpace(self)
        self.sheets = resources.AsyncSpreadsheets(self)
        self.bitables = resources.AsyncBiTable(self)
        self.docs = resources.AsyncDocuments(self)
        self.board = resources.AsyncBoard(self)
        self.assets = resources.AsyncAssets(self)
        self.messages = resources.AsyncMessages(self)

    @property
    def app_credentials(self) -> dict:
        if self._app_id is None or self._app_secret is None:
            raise ValueError("App credentials are not set")
        return {
            "app_id": self._app_id,
            "app_secret": self._app_secret,
        }

    async def get_auth_headers(self) -> dict:
        if self._token is None or self._token.is_expired:
            if self._token_type == "tenant":
                logger.debug("Refreshing tenant access token")
                self._token = await self.auth.token.get_tenant_access_token()
            else:
                raise NotImplementedError(f"{self._token_type} token is not supported")
        return {
            "Authorization": f"Bearer {self._token.access_token}",
        }
