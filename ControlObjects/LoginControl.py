class LoginControl:
    """
    Handles the login process for user accounts.
    """

    def __init__(self, accounts):
        # Initialize with a list of accounts and set the initial login status to False
        self.__login_status = False
        self.__accounts = accounts  # List of Account objects

    def login(self, username, password):
        """
        Attempt to log in with the provided username and password.
        If the credentials match an account, set login status to True.
        """
        for account in self.__accounts:
            if account.get_username() == username and account.get_password() == password:
                self.__login_status = True
                print(f"Login successful for user: {username}")
                return True
        print("Login failed. Invalid credentials.")
        return False

    def logout(self):
        """
        Log out the currently logged-in user.
        """
        if self.__login_status:
            self.__login_status = False
            print("User logged out successfully.")
        else:
            print("No user is currently logged in.")

    def is_logged_in(self):
        """
        Check if a user is currently logged in.
        """
        return self.__login_status
