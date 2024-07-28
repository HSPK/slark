class LarkException(Exception):
    def __init__(self, code: int, msg: str, context: dict | None = None):
        self.code = code
        self.msg = msg
        self.context = context

    def __repr__(self) -> str:
        return f"{self.code}: {self.msg}"

    __str__ = __repr__
