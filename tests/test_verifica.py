import pytest

from calcola_primi.verifica import valida_positivi


def test_valida_positivi():
    with pytest.raises(ValueError):
        valida_positivi(-1)
