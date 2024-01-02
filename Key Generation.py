import random
import numpy as np
from scipy.spatial.distance import pdist


def generate_secret_key(p):
    """
    Generates a secret key for the Rainbow Protocol.

    Args:
        p (int): The prime modulus of the elliptic curve.

    Returns:
        int: The secret key.
    """
    while True:
        s = random.randrange(1, p)
        if s % 2 == 1:
            return s


def generate_public_key(p, s):
    """
    Generates a public key for the Rainbow Protocol.

    Args:
        p (int): The prime modulus of the elliptic curve.
        s (int): The secret key.

    Returns:
        list: The public key.
    """
    a = random.randrange(1, p)
    b = s * a % p
    return [a, b]
