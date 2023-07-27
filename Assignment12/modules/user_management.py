from modules import file_handling

USERS_FILE = "data/users.txt"

def login():
    print("==== User Login ====")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users_data = file_handling.read_data(USERS_FILE)

    if users_data:
        users = users_data.split("\n")
        for user in users:
            user_info = user.split(",")
            if len(user_info) == 2:
                stored_username, stored_password = user_info
                if username == stored_username and password == stored_password:
                    print("Login successful.")
                    return
    print("Invalid username or password.")
def register():
    print("==== User Registration ====")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    users_data = file_handling.read_data(USERS_FILE)

    if users_data:
        users = users_data.split("\n")
        for user in users:
            stored_username = user.split(",")
            if username == stored_username:
                print("Username already exists. Please choose a different username.")
                return

    new_user_data = f"{username},{password}\n"
    file_handling.append_data(USERS_FILE, new_user_data)
    print("Registration successful. You can now login with your new credentials.")