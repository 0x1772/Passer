from password_generator import generate_password
from password_storage import save_password, get_password
from encryption import encrypt, decrypt

def show_menu():
    print("Password Manager")
    print("1. Generate new password")
    print("2. Store password")
    print("3. Retrieve password")
    print("4. Exit")

def generate_password_menu():
    password_length = int(input("Enter password length: "))
    password = generate_password(password_length)
    print(f"Generated password: {password}")
    return password

def store_password_menu():
    service_name = input("Enter service name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    encrypted_password = encrypt(password)
    save_password(service_name, username, encrypted_password)
    print("Password saved successfully!")

def retrieve_password_menu():
    service_name = input("Enter service name: ")
    username = input("Enter username: ")
    encrypted_password = get_password(service_name, username)
    if encrypted_password:
        password = decrypt(encrypted_password)
        print(f"Retrieved password: {password}")
    else:
        print("Password not found!")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        generate_password_menu()
    elif choice == "2":
        store_password_menu()
    elif choice == "3":
        retrieve_password_menu()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
