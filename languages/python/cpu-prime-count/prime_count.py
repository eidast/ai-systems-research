#!/usr/bin/env python3
import sys

def count_primes(limit: int) -> int:
    if limit < 2:
        return 0
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= limit:
        if sieve[p]:
            start = p * p
            step = p
            sieve[start:limit + 1:step] = b"\x00" * (((limit - start) // step) + 1)
        p += 1
    return sum(sieve)

if __name__ == "__main__":
    upper = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    print(count_primes(upper))
