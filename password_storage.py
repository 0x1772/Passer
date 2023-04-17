import json

def save_password(username, password):
    """
    Save the password associated with the given username to a JSON file
    """
    # Load the existing passwords from the JSON file
    with open('passwords.json', 'r') as f:
        passwords = json.load(f)

    # Update the passwords dictionary with the new password
    passwords[username] = password

    # Save the updated passwords dictionary to the JSON file
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

def get_password(username):
    """
    Retrieve the password associated with the given username from the JSON file
    """
    # Load the existing passwords from the JSON file
    with open('passwords.json', 'r') as f:
        passwords = json.load(f)

    # Return the password associated with the given username, or None if the username is not found
    return passwords.get(username, None)
