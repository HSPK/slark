import arrow


def datetime_now(format: str = "YYYY-MM-DD HH:mm:ss") -> str:
    return arrow.now(tz="Asia/Shanghai").format(format)
