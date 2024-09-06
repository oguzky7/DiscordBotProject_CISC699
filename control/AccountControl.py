from entity.AccountEntity import AccountEntity

class AccountControl:
    def __init__(self):
        self.account_entity = AccountEntity()

    def add_user(self, username, password):
        """Handles adding a new account."""
        self.account_entity.connect()
        self.account_entity.insert_user(username, password)
        self.account_entity.close()

    def delete_user(self, user_id):
        """Handles deleting an account."""
        self.account_entity.connect()
        self.account_entity.delete_user(user_id)
        self.account_entity.close()

    def fetch_users(self):
        """Handles fetching all accounts."""
        self.account_entity.connect()
        users = self.account_entity.fetch_users()
        self.account_entity.close()
        return users
