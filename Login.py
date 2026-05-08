# Predefined correct credentials
USERNAME = "Hamtah_jawzjani"
PASSWORD = "12345"


def login():
    # Number of allowed attempts
    attempts = 3

    # Loop until attempts finish
    while attempts > 0:

        # Get user input
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if credentials are correct
        if username == USERNAME and password == PASSWORD:
            print("Login successful! Access granted.")
            return True  # Exit function with success

        else:
            # Reduce attempts if login fails
            attempts -= 1
            print("Wrong username or password!")
            print(attempts, "attempt(s) remaining")

    # If attempts are finished
    print("Program locked due to too many failed attempts.")
    return False


# Run login system and check result
if login():
    print("Welcome, Hamtah_jawzjani!")
else:
    print("Access denied.")
