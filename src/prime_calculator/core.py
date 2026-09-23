from math import isqrt

from bitarray import bitarray


def sieve(n: int) -> float:
    if n < 2:
        return 0

    prime_flags = bitarray(n + 1)
    prime_flags.setall(1)
    prime_flags[:2] = 0

    for i in range(2, isqrt(n) + 1):
        if prime_flags[i]:
            prime_flags[i * i :: i] = 0

    return (prime_flags.count(1) / n) * 100
