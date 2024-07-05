#!/usr/bin/env python3
"""
Defines a hash_password function to return a hashed password
"""

# Import the bcrypt module
import bcrypt
# Import the hashpw function from the bcrypt module
from bcrypt import hashpw


# Define a function to hash a password
def hash_password(password: str) -> bytes:
    """
    Returns a hashed password
    Args:
        password (str): password to be hashed
    """
    # Encode the password to bytes
    b = password.encode()
    # Generate the hashed password using bcrypt
    hashed = hashpw(b, bcrypt.gensalt())
    # Return the hashed password
    return hashed


# Define a function to check if a password is valid
def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check whether a password is valid
    Args:
        hashed_password (bytes): hashed password
        password (str): password in string
    Return:
        bool
    """
    # Check if the encoded password matches the hashed password
    return bcrypt.checkpw(password.encode(), hashed_password)
