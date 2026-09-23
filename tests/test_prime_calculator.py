from prime_calculator import sieve


def test_sieve():
    assert sieve(50) == 30
    assert sieve(100) == 25
    assert sieve(500) == 19
    assert sieve(1000) == 16.8


def test_sieve_for_numbers_below_two():
    assert sieve(0) == 0
    assert sieve(1) == 0
