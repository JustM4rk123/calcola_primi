# Calcola primi

Piccolo progetto Python che usa la **crivella di Eratostene** per calcolare la percentuale di numeri primi compresi tra `0` e un valore massimo indicato dall'utente.

## Requisiti

- Python 3.10 o superiore
- `pip`

## Installazione

Dalla cartella principale del progetto, installa le dipendenze elencate in `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
python -m pip install -e .
```

Il file `requirements.txt` contiene:

- [`bitarray`](https://pypi.org/project/bitarray/), usata per rappresentare in modo efficiente i valori primi e non primi.
- `pytest`, usato per eseguire i test automatici.

## Utilizzo

Avvia il programma come modulo Python:

```powershell
python -m calcola_primi
```

Inserisci il numero massimo quando richiesto. Per esempio:

```text
Fino a che numero vuoi calcolare i numeri primi? 100
Il 25.0% dei numeri sono primi
```

Il valore inserito deve essere un numero intero non negativo. Un valore negativo produce un `ValueError`.

## Uso come libreria

La funzione `crivella` è disponibile direttamente dal pacchetto:

```python
from calcola_primi import crivella

percentuale = crivella(100)
print(percentuale)  # 25.0
```

La funzione restituisce la percentuale di numeri primi tra `0` e `n`, inclusi gli estremi. Per valori minori di `2` restituisce `0`.

## Test

Esegui la suite con:

```powershell
pytest
```

I test verificano i risultati della crivella su valori diversi e i casi limite.

## Struttura del progetto

```text
calcola_primi/
├── pyproject.toml
├── requirements.txt
├── README.md
├── src/
│   └── calcola_primi/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core.py
│       └── verifica.py
└── tests/
	├── test_calcola_primi.py
	└── test_verifica.py
```

- `core.py`: implementa la crivella di Eratostene.
- `verifica.py`: controlla la validità del numero inserito.
- `__main__.py`: gestisce l'esecuzione da terminale.
- `tests/`: contiene i test automatici.