from math import isqrt

from pytest import approx

from prime_calculator import sieve, small_sieve


def test_sieve():
    assert sieve(50) == 30.0
    assert sieve(100) == 25.0
    assert sieve(500) == 19.0
    assert sieve(1_000) == approx(16.8)


def test_sieve_for_numbers_at_or_above_chunk_size():
    assert sieve(10_000_000) == approx(6.64579)
    assert sieve(10_000_001) == approx(6.645789335421067)


def test_sieve_for_numbers_below_two():
    assert sieve(0) == 0
    assert sieve(1) == 0


def test_small_sieve():
    assert small_sieve(isqrt(100) + 1) == [2, 3, 5, 7, 11]
    assert small_sieve(isqrt(500) + 1) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert small_sieve(isqrt(1_000) + 1) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    assert small_sieve(isqrt(10_000) + 1) == [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
    ]
