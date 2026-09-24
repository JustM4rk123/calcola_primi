from math import isqrt

from bitarray import bitarray


def sieve(n: int) -> float:
    if n < 2:
        return 0

    # Only primes up to sqrt(n) are needed to mark composite values.
    primes_until_sqrt_of_n = small_sieve(isqrt(n) + 1)

    CHUNK_SIZE = 10_000_000
    current_chunk = 0
    prime_sum = 0

    while current_chunk <= n:
        # Each bit represents the number at current_chunk + its bit index.
        chunk_end = min(current_chunk + CHUNK_SIZE, n + 1)
        prime_flags = bitarray(chunk_end - current_chunk)
        prime_flags.setall(1)

        if current_chunk == 0:
            prime_flags[:2] = 0

        for prime in primes_until_sqrt_of_n:
            # Larger primes cannot introduce a new composite in this chunk.
            if prime * prime >= chunk_end:
                break

            # Start at the first multiple inside the current chunk, but never
            # before p^2 so that the prime p itself remains marked as prime.
            first_multiple = max(
                prime * prime,
                ((current_chunk + prime - 1) // prime) * prime,
            )
            if first_multiple < chunk_end:
                prime_flags[first_multiple - current_chunk :: prime] = 0

        prime_sum += prime_flags.count(1)
        current_chunk = chunk_end

    return (prime_sum / n) * 100


def small_sieve(n: int) -> list[int]:
    if n < 2:
        return []

    # Sieve the small contiguous range used to mark the larger chunks.
    prime_flags = bitarray(n + 1)
    prime_flags.setall(1)
    prime_flags[:2] = 0

    for i in range(2, isqrt(n) + 1):
        if prime_flags[i]:
            prime_flags[i * i :: i] = 0

    return [i for i in range(n+1) if prime_flags[i]]
    
