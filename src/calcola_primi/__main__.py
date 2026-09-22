import argparse

from .core import crivella
from .verifica import valida_positivi


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calcola i numeri primi fino a un certo numero."
    )
    parser.add_argument(
        "-n",
        "--numero",
        type=int,
        help="Il numero fino al quale calcolare i numeri primi.",
        required=False,
    )

    args = parser.parse_args()

    if args.numero is not None:
        n = valida_positivi(args.numero)
    else:
        n = valida_positivi(
            int(input("Fino a che numero vuoi calcolare i numeri primi? "))
        )
    primi = crivella(n)
    print(f"Il {primi}% dei numeri sono primi")


if __name__ == "__main__":
    main()
