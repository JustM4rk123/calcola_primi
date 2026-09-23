import argparse

from .core import sieve
from .validation import validate_non_negative


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate prime numbers up to a given number."
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        help="The number up to which prime numbers should be calculated.",
        required=False,
    )

    args = parser.parse_args()

    if args.number is not None:
        n = validate_non_negative(args.number)
    else:
        n = validate_non_negative(
            int(input("Up to which number should prime numbers be calculated? "))
        )
    prime_percentage = sieve(n)
    print(f"{prime_percentage}% of the numbers are prime")


if __name__ == "__main__":
    main()
