import os
from typing import Tuple

import httpx


def get_large_pdf(file: str, url: str) -> Tuple[str, bytes]:
    if os.path.exists(file):
        with open(file, "rb") as f:
            content = f.read()

    else:
        content = httpx.get(url).content

        with open(file, "wb") as f:
            f.write(content)

    return file, content
