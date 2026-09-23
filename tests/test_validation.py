import pytest

from prime_calculator.validation import validate_non_negative


def test_validate_non_negative():
    with pytest.raises(ValueError):
        validate_non_negative(-1)
