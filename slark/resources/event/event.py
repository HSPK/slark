import abc
import hashlib
import json
import typing as t

from slark.resources._resources import AsyncAPIResource
from slark.types._utils import cached_property
from slark.types.event.common import EventType, LarkEvent
from slark.utils.decrypt import AESCipher


class AsyncEvent(AsyncAPIResource):
    _callback_map: t.Dict[EventType, t.Callable]

    def __init__(self, client):
        super().__init__(client)
        self._callback_map = {}

    def register(self, event_type: EventType) -> t.Callable:
        def decorator(func):
            self._callback_map[event_type] = func
            return func

        return decorator

    @staticmethod
    def _decrypt_data(encrypt_key, encrypt_data):
        if encrypt_key == "" and encrypt_data is None:
            # data haven't been encrypted
            return None
        if encrypt_key == "":
            raise Exception("ENCRYPT_KEY is necessary")
        cipher = AESCipher(encrypt_key)

        return json.loads(cipher.decrypt_string(encrypt_data))

    def _make_app(self, path: t.Union[str, None] = None):
        import fastapi

        app = fastapi.FastAPI()

        @app.post(path or "/")
        async def event_handler(data: t.Dict[str, t.Any]):
            decrypt_data = self._decrypt_data(
                self._client._encrypt_key,
                data.get("encrypt"),
            )
            callback_type = decrypt_data.get("type")
            if callback_type == "url_verification":
                return {"challenge": decrypt_data.get("challenge")}
            try:
                lark_event = LarkEvent.model_validate(decrypt_data)
            except Exception:
                raise Exception(f"Invalid event data: {decrypt_data}") from None
            event_type = lark_event.header.event_type
            callback = self._callback_map.get(event_type, None)
            return await callback(lark_event)

        return app

    def listen(
        self,
        host: str = "127.0.0.1",
        port: int = 8000,
        path: t.Union[str, None] = None,
    ):
        import uvicorn

        app = self._make_app(path)

        uvicorn.run(app, host=host, port=port)
