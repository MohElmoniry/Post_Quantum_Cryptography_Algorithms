import hashlib
import numpy as np
from scipy.spatial.distance import pdist
import time
import random
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

def generate_message_digest(message):
    """
    Generates a message digest for the Rainbow Protocol.

    Args:
        message (bytes): The message to be signed.

    Returns:
        int: The message digest.
    """
    message_digest = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')
    return message_digest

def generate_random_lattice_points(d, q):
    """
    Generates a set of random lattice points for the Rainbow Protocol.

    Args:
        d (int): The dimension of the lattice.
        q (int): The number of lattice points.

    Returns:
        numpy.ndarray: The set of lattice points.
    """
    points = np.random.normal(size=(q, d))
    points = points / np.linalg.norm(points, axis=1, keepdims=True)
    points = points * (q * np.sqrt(2))**d
    points = points.astype(int) % q
    return points

def generate_signature(p, q, s, message):
    """
    Generates a signature for the Rainbow Protocol.

    Args:
        p (int): The prime modulus of the elliptic curve.
        q (int): The number of lattice points.
        s (int): The secret key.
        message (bytes): The message to be signed.

    Returns:
        numpy.ndarray: The signature.
    """
    message_digest = generate_message_digest(message)
    d = 2  # Fixed dimension of the lattice
    lattice_points = generate_random_lattice_points(d, q)

    lambda_matrix = np.zeros((d, q))
    for i in range(q):
        lambda_matrix[:, i] = np.array([message_digest, lattice_points[i]])

    v = np.linalg.inv(lambda_matrix)
    u = np.dot(v, s)

    return u


def main():
    # Generate a prime modulus for the elliptic curve
    p = 17921

    # Generate a public key and secret key
    s = generate_secret_key(p)
    public_key = generate_public_key(p, s)

    # Sign a message
    message = b"Hello, world!"
    signature = generate_signature(p, 1024, s, message)

    # Verify the signature
    #is_valid = verify_signature(p, 1024, public_key, signature, message)

    # Check the correctness of the signature
    #if is_valid:
     #   print("Signature verification successful!")
    #else:
     #   print("Signature verification failed!")

    # Measure the time required for signature generation and verification
    start_time = time.time()
    signature = generate_signature(p, 1024, s, message)
    elapsed_time_for_generation = time.time() - start_time

    #
    print("Time taken for signature generation:", elapsed_time_for_generation, "seconds")
   # print("Time taken for signature verification:", elapsed_time_for_verification, "seconds")

if __name__ == "__main__":
    main()