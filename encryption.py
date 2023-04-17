from cryptography.fernet import Fernet

def encrypt_password(password):
    """
    Encrypt the password using a symmetric encryption algorithm
    """
    # Generate a new encryption key
    key = Fernet.generate_key()

    # Create a Fernet cipher using the encryption key
    cipher = Fernet(key)

    # Encrypt the password using the Fernet cipher
    encrypted_password = cipher.encrypt(password.encode())

    return key, encrypted_password

def decrypt_password(key, encrypted_password):
    """
    Decrypt the encrypted password using the encryption key
    """
    # Create a Fernet cipher using the encryption key
    cipher = Fernet(key)

    # Decrypt the encrypted password using the Fernet cipher
    password = cipher.decrypt(encrypted_password).decode()

    return password
