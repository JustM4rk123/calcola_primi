from math import isqrt

from bitarray import bitarray


def crivella(n: int) -> float:
    if n < 2:
        return 0

    primi = bitarray(n + 1)
    primi.setall(1)
    primi[:2] = 0

    for i in range(2, isqrt(n) + 1):
        if primi[i]:
            primi[i * i :: i] = 0

    return (primi.count(1) / n) * 100
