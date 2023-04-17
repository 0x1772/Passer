from password import Password
from database import Database


def add_password():
    name = input("What is the name of the website or application? ")
    username = input("What is your username or email address? ")
    password = input("What is your password? ")
    p = Password(name, username, password)
    db = Database()
    db.add_password(p)


def view_password():
    name = input("What is the name of the website or application? ")
    db = Database()
    password = db.get_password(name)
    if password:
        print(f"Name: {password.name}\nUsername/Email: {password.username}\nPassword: {password.password}")
    else:
        print("Password not found")


def delete_password():
    name = input("What is the name of the website or application? ")
    db = Database()
    db.delete_password(name)


def main():
    print("Welcome to Password Manager!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new password")
        print("2. View a password")
        print("3. Delete a password")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again")


if __name__ == '__main__':
    main()
