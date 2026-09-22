from calcola_primi import crivella


def test_crivella():
    assert crivella(50) == 30
    assert crivella(100) == 25
    assert crivella(500) == 19
    assert crivella(1000) == 16.8


def test_crivella_per_numeri_minori_di_due():
    assert crivella(0) == 0
    assert crivella(1) == 0
