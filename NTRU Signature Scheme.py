import hashlib

import numpy as np

def generate_keypair(q, d):
    # Generate a prime number
    p = 2**(2*q + 1) - 1

    # Generate a random matrix H
    H = np.random.randint(1, p, (2*d, q))
    H = np.linalg.qr(H)[0]
    H = (H[:d, :], H[d:, :])

    # Generate a secret key vector s
    s = np.random.randint(1, p)

    return p, H, s

def hash_message(message):
    # Hash the message
    digest = hashlib.sha512(message.encode('utf-8')).digest()
    return digest

def generate_signature(p, H, s, message):
    # Generate a random vector v
    d = 2
    v = np.random.randint(1, p, (d, 1))

    # Compute the signature matrix
    A = np.dot(H[0], v) - np.dot(message, H[1], v)

    # Compute the signature
    signature = np.dot(np.linalg.inv(A), s)

    return signature

def verify_signature(p, H, public_key, signature, message):
    # Verify the signature
    u = np.dot(signature, H[1]) + np.dot(message, H[0], signature)
    v = np.dot(u, public_key) % p

    if v == 1:
        return True
    else:
        return False
