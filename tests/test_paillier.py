import random

from swartz import paillier

ITERATIONS = 100
kp = paillier.generate_keypair(128)


def test_encrypt_decrypt():
    for m in random.sample(range(2 ** 63 - 1), ITERATIONS):
        c = kp.encrypt(m)
        assert kp.decrypt(c) == m


def test_encrypt_no_repeat():
    m = random.randrange(2 ** 63 - 1)
    c = kp.encrypt(m)
    for _ in range(ITERATIONS):
        assert c != kp.encrypt(m)


def test_homomorphic_addition():
    c, total = 1, 0
    for m in random.sample(range(2 ** 63 - 1), ITERATIONS):
        c = (c * kp.encrypt(m)) % (kp.n ** 2)
        total += m
        assert kp.decrypt(c) == total


def test_homomorphic_multiplication():
    c, total = kp.encrypt(1), 1
    for α in random.sample(range(2 ** 63 - 1), ITERATIONS):
        c = pow(c, α, kp.n ** 2)
        total *= α
        assert kp.decrypt(c) == total % kp.n
