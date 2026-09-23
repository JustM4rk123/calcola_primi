def validate_non_negative(n: int) -> int:
    if n < 0:
        raise ValueError
    return n
