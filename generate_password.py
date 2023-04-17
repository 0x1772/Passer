import string
import random

def generate_password(length):
    """
    Generate a random password with the given length
    """
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    return password
