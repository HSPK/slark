import re
from urllib.parse import unquote


def extract_filename(disposition: str):
    match = re.search(r"filename\*=([^;]+)", disposition)
    if match:
        try:
            enc_quoted = match.group(1).strip().strip('"')
            enc, quoted = enc_quoted.split("''")
            return unquote(quoted, encoding=enc)
        except Exception:
            return "Unkown"
    else:
        return "Unknown"