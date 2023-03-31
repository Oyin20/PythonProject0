import re

def check_password_strength(password):
    """
    Function to check the strength of a password.

    Password must be over 8 characters and must contain alphanumeric, upper and lowercase characters.

    Args:
        password (str): The password to be checked.
    Returns:
        int: 0 if password is weak, 1 if password is moderate and 2 if password is strong. """
 strength = 0
 if len(password) < 8:
        print("Password is w
