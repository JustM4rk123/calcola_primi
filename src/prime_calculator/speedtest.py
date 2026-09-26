import time

from prime_calculator.core import sieve

BENCHMARKS = {
    10: 40.0,
    100: 25.0,
    1_000: 16.8,
    10_000: 12.3,
    100_000: 9.6,
    1_000_000: 7.8,
    10_000_000: 6.7,
    100_000_000: 5.8,
    1_000_000_000: 5.0,
}


def speedtest():
    for n, expected in BENCHMARKS.items():
        start = time.perf_counter()
        result = sieve(n)
        assert abs(result - expected) < 1e-1
        elapsed = time.perf_counter() - start

        print(f"{n:>13,} -> {result:>9.6f} %, elapsed time: {elapsed:>11.6f} seconds")


if __name__ == "__main__":
    speedtest()
