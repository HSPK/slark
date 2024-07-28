from typing import Literal

import httpx
from loguru import logger

from slark import resources
from slark._constants import DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT
from slark.client._client import AsyncAPIClient
from slark.types.auth import TokenBase
import re

CredentailTypes = Literal["tenant", "user"]


class AsyncLark(AsyncAPIClient):
    auth: resources.AsyncAuth
    webhook: resources.AsyncWebhook
    knowledge_space: resources.KnowledgeSpace
    spreadsheets: resources.AsyncSpreadsheets

    _app_id: str | None
    _app_secret: str | None
    _webhook_url: str | None
    _token: TokenBase | None
    _token_type: CredentailTypes

    def __init__(
        self,
        *,
        app_id: str | None = None,
        app_secret: str | None = None,
        webhook: str | None = None,
        base_url: str | httpx.URL = "https://open.feishu.cn/open-apis/",
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: httpx.Timeout = DEFAULT_TIMEOUT,
        proxies: httpx._types.ProxyTypes | None = None,
        token_type: CredentailTypes = "tenant",
    ):
        self._app_id = app_id
        self._app_secret = app_secret
        self._webhook_url = webhook
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
        self.spreadsheets = resources.AsyncSpreadsheets(self)

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

    async def get_spreadsheet_token_and_sheet_id(self, url: str):
        if "/sheets/" in url:
            spreadsheet_token, sheet_id = re.findall(
                r"\/sheets\/([^\/\?]+)(?:\?sheet=([^\/]+))?", url
            )[0]
        elif "/wiki/" in url:
            wiki_token, sheet_id = re.findall(
                r"\/wiki\/([^\/\?]+)(?:\?sheet=([^\/]+))?", url
            )[0]
            node_info = (
                await self.knowledge_space.nodes.get_node_info(wiki_token)
            ).data.node
            if node_info.obj_type != "sheet":
                raise ValueError("The node is not a sheet")
            spreadsheet_token = node_info.obj_token
        assert spreadsheet_token, "Sheet token is not found"
        if not sheet_id:
            sheets_info = await self.spreadsheets.worksheet.get_all_worksheets_info(
                spreadsheet_token
            )
            sheet_id = sheets_info.data.sheets[0].sheet_id
        return {
            "spreadsheet_token": spreadsheet_token,
            "sheet_id": sheet_id,
        }
