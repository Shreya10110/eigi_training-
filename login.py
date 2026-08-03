users_db = {}
#in this section user will do sign up and if user already exist 
#in user database it will give message already exist
def signup():
    print("\n--- USER SIGNUP ---")
    username = input("Enter a new username: ").strip()
    if username in users_db:
        print(f" Error: Username '{username}' already exists! Please choose another or login.")
        return
    password = input("Enter a password: ").strip()
    email = input("Enter your email: ").strip()
    users_db[username] = {
        "password": password,
        "email": email
    }
    print(f" Success: Account created successfully for '{username}'!")
#this is only for user who already did sign up process
def login():
    """Authenticates an existing user."""
    print("\n--- USER LOGIN ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users_db and users_db[username]["password"] == password:
        print(f" Welcome back, {username}! Login successful.")
    else:
        print(" Error: Invalid username or password.")
def reset_password():
    """Resets password for an existing account."""
    print("\n--- RESET PASSWORD ---")
    username = input("Enter your username: ").strip()
    if username not in users_db:
        print(f"Error: No account found with username '{username}'.")
        return
    #here simply checking for new password and old password
    old_password = input("Enter your current password: ").strip()
    if users_db[username]["password"] == old_password:
        new_password = input("Enter your new password: ").strip()
        users_db[username]["password"] = new_password
        print(" Success: Password updated successfully!")
    else:
        print(" Error: Incorrect current password.")

def list_all_users():
    print("\n--- ALL REGISTERED USERS ---")
    usernames_list = list(users_db.keys())
    if len(usernames_list) == 0:
        print("No users registered yet.")
        return
    print(f"Total Users: {len(usernames_list)}")
    for count, username in enumerate(usernames_list, start=1):
        user_email = users_db[username]["email"]
        print(f"{count}. Username: {username} | Email: {user_email}")


def main():
    while True:
        print("\n==============================")
        print("    USER MANAGEMENT SYSTEM    ")
        print("==============================")
        print("1. User Signup")
        print("2. User Login")
        print("3. Reset Password")
        print("4. List All Users")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            reset_password()
        elif choice == "4":
            list_all_users()
        elif choice == "5":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid input! Please enter a option between 1 and 5.")


#if __name__ == "__main__":
   # main()




