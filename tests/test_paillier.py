import random

from swartz import paillier

kp = paillier.generate_keypair(128)


def test_encrypt_decrypt():
    m = random.randrange(1, 1e10)
    x = kp.encrypt(m)
    assert kp.decrypt(x) == m


def test_encrypt_no_repeat():
    m = random.randrange(1, 1e10)
    assert kp.encrypt(m) != kp.encrypt(m)


def test_homomorphic_addition():
    m1 = random.randrange(1, 1e10)
    m2 = random.randrange(1, 1e10)
    c = kp.encrypt(m1) * kp.encrypt(m2)
    assert kp.decrypt(c) == m1 + m2


def test_homomorphic_multiplication():
    m1 = random.randrange(1, 1e10)
    m2 = random.randrange(1, 1e10)
    c = pow(kp.encrypt(m1), m2, kp.n ** 2)
    assert kp.decrypt(c) == m1 * m2
