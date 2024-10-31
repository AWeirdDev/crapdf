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

## Benchmark

Run the benchmarks using `bench.py`. Make sure to install dev dependencies from `requirements-dev.txt`.

Below is a table comparing the performance of the different providers.

<table>
<thead>
<tr>
    <th>↓ Provider</th>
    <th><code>water</code></th>
    <th><code>inflation</code></th>
    <th><code>chocolate</code></th>
    <th><code>mamba</code></th>
</tr>
</thead>

<tbody>
<tr>
    <td><a href="https://pypi.org/project/pypdf/">pypdf</a></td>
    <td>804.39ms (avg)</td>
    <td>877.56ms (avg)</td>
    <td>265.41ms (avg)</td>
    <td><b>1769.91ms ≈ 1.8s (avg)</b> 🥇</td>
</tr>

<tr>
    <td>crapdf</td>
    <td>386.43ms (avg)</td>
    <td><b>421.94ms (avg)</b> 🥇</td>
    <td>111.79ms (avg)</td>
    <td>💥 panic<sup>2</sup></td>
</tr>

<tr>
    <td>crapdf (bytes, mem)<sup>1</sup></td>
    <td><b>385.93ms (avg)</b> 🥇</td>
    <td>427.71ms (avg)</td>
    <td><b>95.63ms (avg)</b> 🥇</td>
    <td>💥 panic<sup>2</sup></td>
</tr>

</tbody>

</table>

<sup>1</sup> <i>mem</i> – Usage with `extract_bytes()`.<br />
<sup>2</sup> <i>panic</i> – The `lopdf` crate failed to load the PDF document, the error was "ToUnicode CMap error: Could not parse ToUnicodeCMap: Error!" which seems to be an encoding issue. I'm unsure of the probable cause, but it looks like they're discussing it here: <b>[J-F-Liu/lopdf ● #330](https://github.com/J-F-Liu/lopdf/issues/330)</b>.


***

AWeirdDev. [GitHub Repo](https://github.com/AWeirdDev/crapdf)
