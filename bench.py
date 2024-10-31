import time
from typing import Any, Callable, ParamSpec

from bench import download, providers


P = ParamSpec("P")


def measure(
    name: str, call: Callable[P, Any], *args: P.args, **kwargs: P.kwargs
) -> float:
    s = time.perf_counter()
    call(*args, **kwargs)
    e = time.perf_counter()

    print(f"{name}: {(e - s) * 1000:.2f}ms")
    return e - s


print("Benchmarking...\n\n")

files = [
    (
        "water.pdf",
        "https://www.epa.gov/sites/default/files/2015-10/documents/ace3_drinking_water.pdf",
    ),
    (
        "inflation.pdf",
        "https://www.europarl.europa.eu/RegData/etudes/BRIE/2022/729352/EPRS_BRI(2022)729352_EN.pdf",
    ),
    (
        "chocolate.pdf",
        "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/10E9BE79E5DEFD360C5CD46B92E07414/S0007114507795296a.pdf/cocoa-and-health-a-decade-of-research.pdf",
    ),
    ("mamba.pdf", "https://arxiv.org/pdf/2312.00752"),
]

for name, url in files:
    print("Using", name, "\x1b[2mfrom", url, "\x1b[22m")

    bench_a = []
    bench_b = []
    bench_c = []

    for i in range(3):
        print("** attempt", i + 1, "**")

        fn, content = download.get_large_pdf("files/" + name, url)

        try:
            bench_a.append(measure("crapdf", providers.use_crapdf, fn))

            bench_b.append(
                measure("crapdf (bytes, mem)", providers.use_crapdf_bytes, content)
            )

        except Exception as err:
            print("\x1b[1;31mcrapdf failed:", err, "\x1b[0m")

        try:
            bench_c.append(measure("pypdf", providers.use_pypdf, fn))

        except Exception as err:
            print("\x1b[1;31mpypdf failed:", err, "\x1b[0m")

        print()

    print("\x1b[1mResults\x1b[0m")
    print(
        "  \x1b[1;34mcrapdf:\x1b[0m",
        sum(bench_a) / (len(bench_a) or 1) * 1000,
        "ms (avg)",
    )
    print(
        "  \x1b[1;34mcrapdf (bytes, mem):\x1b[0m",
        sum(bench_b) / (len(bench_b) or 1) * 1000,
        "ms",
    )
    print("  \x1b[1;34mpypdf:\x1b[0m", sum(bench_c) / (len(bench_c) or 1) * 1000, "ms")
    print("\n")
