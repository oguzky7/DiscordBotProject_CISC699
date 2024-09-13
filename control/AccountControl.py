from DataObjects.AccountDAO import AccountDAO

class AccountControl:
    def __init__(self):
        self.account_dao = AccountDAO()  # DAO for database operations

    def add_account(self, username: str, password: str, website: str):
        """Add a new account to the database."""
        self.account_dao.connect()  # Establish database connection
        result = self.account_dao.add_account(username, password, website)  # Call DAO to add account
        self.account_dao.close()  # Close the connection
        return result

    def delete_account(self, account_id: int):
        """Delete an account by ID."""
        self.account_dao.connect()  # Establish database connection
        result = self.account_dao.delete_account(account_id)
        self.account_dao.reset_id_sequence()  # Reset the ID sequence
        self.account_dao.close()  # Close the connection
        return result

    def fetch_all_accounts(self):
        """Fetch all accounts using the DAO."""
        self.account_dao.connect()  # Establish database connection
        accounts = self.account_dao.fetch_all_accounts()  # Fetch accounts from DAO
        self.account_dao.close()  # Close the connection
        return accounts if accounts else None

    def fetch_account_by_website(self, website: str):
        """Fetch an account by website."""
        self.account_dao.connect()  # Establish database connection
        account = self.account_dao.fetch_account_by_website(website)
        self.account_dao.close()  # Close the connection
        return account if account else None
