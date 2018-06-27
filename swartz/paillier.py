import random

from dataclasses import dataclass

from .utils import generate_prime, modular_inverse

DEFAULT_KEYSIZE = 2048


@dataclass
class PublicKey:
    n: int
    g: int

    def encrypt(self, message: int) -> int:
        n, g = self.n, self.g
        r = random.randrange(1, n)
        mod = n ** 2
        return (pow(g, message, mod) * pow(r, n, mod)) % mod


@dataclass
class KeyPair(PublicKey):
    λ: int
    µ: int

    def decrypt(self, cipher: int) -> int:
        n, λ, µ = self.n, self.λ, self.µ
        return ((pow(cipher, λ, n ** 2) - 1) // n * µ) % n

    @property
    def public_key(self) -> PublicKey:
        return PublicKey(self.n, self.g)


def generate_keypair(length: int = DEFAULT_KEYSIZE) -> KeyPair:
    p, q = generate_prime(length // 2), generate_prime(length // 2)

    n = p * q
    g = n + 1
    λ = (p - 1) * (q - 1)
    µ = modular_inverse(λ, n)
    return KeyPair(n, g, λ, µ)
