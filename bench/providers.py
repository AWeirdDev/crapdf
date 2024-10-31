import crapdf
import pypdf


def use_crapdf(fn: str):
    return crapdf.extract(fn)


def use_crapdf_bytes(b: bytes):
    return crapdf.extract_bytes(b)


def use_pypdf(fn: str):
    reader = pypdf.PdfReader(fn)
    texts = []

    for page in reader.pages:
        texts.append(page.extract_text())

    return texts
