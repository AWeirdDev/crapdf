# 🦀 crapdf
Extract text from a PDF file. Uses the `lopdf` crate. Kind of crappy.

```python
from crapdf import extract, extract_bytes

# Extract from file path
texts: list[str] = extract("file.pdf")

# Extract from bytes
with open("file.pdf", "rb") as f:
    content = f.read()

texts: list[str] = extract_bytes(content)
```

## Performance

Run the benchmarks using `bench.py`. Make sure to install dev dependencies from `requirements-dev.txt`.

The overall performance is similar to [`pypdf`](https://pypi.org/project/pypdf).

***

AWeirdDev. [GitHub Repo](https://github.com/AWeirdDev/crapdf)
