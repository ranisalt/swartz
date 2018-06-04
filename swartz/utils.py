import random
from typing import Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Calculates gcd using extended Euclidean algorithm
    >>> extended_gcd(240, 46)
    (2, -9, 47)
    """
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def modular_inverse(a: int, n: int) -> int:
    """Calculates modular inverse of a mod n, i.e x such that ax = 1 (mod n)
    >>> modular_inverse(77, 5)
    3
    >>> modular_inverse(55, 7)
    6
    """
    _, x, _ = extended_gcd(a, n)
    return x % n


def fermat(n: int, k: int = 100) -> bool:
    """Tests whether n is a probable prime with Fermat primality test
    >>> fermat(567)
    False
    >>> fermat(104789)
    True
    >>> fermat(15485943)
    False
    >>> fermat(32416190071)
    True
    """
    for _ in range(k):
        a = random.randrange(1, n)
        x = pow(a, n - 1, n)  # a^(n - 1) % n
        if x != 1:
            return False
    return True


def miller_rabin(n: int, k: int = 100) -> bool:
    """Tests whether n is a probable prime with Miller-Rabin primality test
    >>> fermat(567)
    False
    >>> fermat(104789)
    True
    >>> fermat(15485943)
    False
    >>> fermat(32416190071)
    True
    """
    if n == 2:
        return True

    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(1, n)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime(length: int) -> int:
    """Generates primes of length bits
    >>> p = generate_prime(32)
    >>> p.bit_length()
    32

    p is prime, i.e. not divisible by any numbers up to sqrt(p)
    >>> all(p % n != 0 for n in range(3, 2 ** 16, 2))
    True
    """
    while True:
        p = (2 ** (length - 1)) | random.getrandbits(length - 1) | 1
        if fermat(p) and miller_rabin(p):
            return p


if __name__ == "__main__":
    import doctest
    doctest.testmod()
