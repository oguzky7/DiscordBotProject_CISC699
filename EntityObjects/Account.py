class Account:
    """
    Represents a user account with a username and password.
    """

    def __init__(self, username, password):
        # Initialize account with username and password
        self.username = username
        self.__password = password

    def set_username(self, username):
        # Set a new username
        self.username = username

    def set_password(self, password):
        # Set a new password
        self.__password = password

    def get_username(self):
        # Return the username
        return self.username

    def info_account(self):
        # Print detailed information about the account
        print(f"Username: {self.username}")
        # Password is protected and should not be printed out directly
        print("Password: [PROTECTED]")

    def validate_account(self, username, password):
        # Validate the account credentials
        if self.username == username and self.__password == password:
            print("Login successful.")
            return True
        else:
            print("Login failed. Invalid credentials.")
            return False
