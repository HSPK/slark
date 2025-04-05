from typing import Dict, Union

from slark.types.exceptions._base import LarkException


class LarkStatusCode:
    SUCCESS = 0
    REQUIRE_AUTHENTICATION = 10001
    RESOURCE_NOT_FOUND = 131005
    BAD_REQUEST = 10400
    INVALID_ACCESS_TOKEN = 20005
    PASSTIME_ACCESS_TOKEN = 20006
    INTERNAL_ERROR = 40003
    BAD_RESPONSE = 10002
    APITimeout = 10003
    APIConnectionError = 10004


class AuthenticationRequiredException(LarkException):
    def __init__(self, msg: str = "Require Authentication", context: Union[Dict, None] = None):
        super().__init__(LarkStatusCode.REQUIRE_AUTHENTICATION, msg, context)


class HttpStatusError(LarkException):
    def __init__(self, code: int, msg: str, context: Union[Dict, None] = None):
        super().__init__(code, msg, context)


class BadResponseError(LarkException):
    def __init__(self, msg: str = "Bad Response", context: Union[Dict, None] = None):
        super().__init__(LarkStatusCode.BAD_RESPONSE, msg, context)


class APITimeoutError(LarkException):
    def __init__(self, msg: str = "Timeout", context: Union[Dict, None] = None):
        super().__init__(LarkStatusCode.APITimeout, msg, context)


class APIConnectionError(LarkException):
    def __init__(self, msg: str = "API Connection Error", context: Union[Dict, None] = None):
        super().__init__(LarkStatusCode.APIConnectionError, msg, context)
