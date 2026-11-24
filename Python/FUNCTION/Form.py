db = {
    "user_name": "",
    "email": "",
    "password": ""
}


def signup(username, email, password):

    if db["user_name"] == username:
        return "user already exists!"

    else:
        db["user_name"] = username
        db["email"] = email
        db["password"] = password

        return "successfully registered!"


def signin(email, password):

    if db["email"] == email and db["password"] == password:
        return f"Hello {db['user_name']}"

    else:
        return "Invalid details"


menu = """
MENU:
1) PRESS 1 FOR REGISTRATION
2) PRESS 2 FOR LOGIN
"""

print(menu)

status = True

while status:

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print("Registration form")

        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        print(signup(name, email, password))

    elif choice == 2:

        print("Login form")

        email = input("Enter your email: ")
        password = input("Enter your password: ")

        print(signin(email, password))

    else:
        print("Invalid input")

    exit_choice = int(
        input("Do you want to continue? 1 = Yes / 2 = No: ")
    )

    if exit_choice == 1:
        status = True
    else:
        status = False