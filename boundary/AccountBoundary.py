from control.AccountControl import AccountControl

class AccountBoundary:
    def __init__(self):
        self.account_control = AccountControl()

    def display_users(self):
        """Displays all accounts."""
        users = self.account_control.fetch_users()
        if users:
            for user in users:
                print(f"ID: {user[0]}, Username: {user[1]}")
        else:
            print("No users found.")

    def add_new_user(self, username, password):
        """Collects input for adding a new account."""
        self.account_control.add_user(username, password)
        print(f"User {username} added successfully.")

    def delete_existing_user(self, user_id):
        """Collects input for deleting an account."""
        self.account_control.delete_user(user_id)
