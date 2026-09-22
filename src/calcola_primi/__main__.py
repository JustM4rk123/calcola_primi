from .core import crivella
from .verifica import valida_positivi


def main() -> None:
    n = valida_positivi(int(input("Fino a che numero vuoi calcolare i numeri primi? ")))
    primi = crivella(n)
    print(f"Il {primi}% dei numeri sono primi")


if __name__ == "__main__":
    main()
