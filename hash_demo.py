"""
hash_demo.py
A beginner-friendly demo of password hashing concepts for a
cybersecurity portfolio project.
"""

import hashlib
import os

def hash_password_plain(password, algorithm="sha256"):
    """Hash a password with no salt, using the given algorithm."""
    hasher = hashlib.new(algorithm)
    hasher.update(password.encode("utf-8"))
    return hasher.hexdigest()

def hash_password_salted(password, salt=None):
    """Hash a password WITH a random salt (the safer, real-world way)."""
    if salt is None:
        salt = os.urandom(16)  # 16 random bytes, different every time
    hasher = hashlib.sha256()
    hasher.update(salt + password.encode("utf-8"))
    return salt.hex(), hasher.hexdigest()

def main():
    password = input("Enter a test password (don't use a real one!): ")

    print("\n--- Unsalted Hashes ---")
    for algo in ["md5", "sha1", "sha256"]:
        result = hash_password_plain(password, algo)
        print(f"{algo.upper():8}: {result}")

    print("\n--- Salted Hash (the secure way) ---")
    salt, salted_hash = hash_password_salted(password)
    print(f"Salt:     {salt}")
    print(f"SHA-256:  {salted_hash}")

    print("\n--- Why this matters ---")
    print("The same password ALWAYS produces the same unsalted hash,")
    print("which is why attackers use 'lookup tables' of common")
    print("password hashes to crack them instantly. Salting adds")
    print("random data so the same password produces a DIFFERENT")
    print("hash every time, defeating those lookup tables.")

if __name__ == "__main__":
    main()