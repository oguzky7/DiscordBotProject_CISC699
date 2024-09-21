from DataObjects.AccountDAO import AccountDAO

class AccountControl:
    def __init__(self):
        self.account_dao = AccountDAO()  # DAO for database operations

    def receive_command(self, command_data, *args):
        """Handle all account-related commands and process business logic."""
        print("Data received from boundary:", command_data)

        if command_data == "fetch_all_accounts":
            return self.fetch_all_accounts()
        
        elif command_data == "fetch_account_by_website":
            website = args[0] if args else None
            return self.fetch_account_by_website(website)
        
        elif command_data == "add_account":
            username, password, website = args if args else (None, None, None)
            return self.add_account(username, password, website)
        
        elif command_data == "delete_account":
            account_id = args[0] if args else None
            return self.delete_account(account_id)
        
        else:
            result = "Invalid command."
            print(result)
            return result

    def add_account(self, username: str, password: str, website: str):
        """Add a new account to the database."""
        self.account_dao.connect()  # Establish database connection
        result = self.account_dao.add_account(username, password, website)  # Call DAO to add account
        self.account_dao.close()  # Close the connection
        
        # Prepare the result and print it
        result_message = f"Account for {website} added successfully." if result else f"Failed to add account for {website}."
        print(result_message)
        return result_message

    def delete_account(self, account_id: int):
        """Delete an account by ID."""
        self.account_dao.connect()  # Establish database connection
        result = self.account_dao.delete_account(account_id)
        self.account_dao.reset_id_sequence()  # Reset the ID sequence
        self.account_dao.close()  # Close the connection
        
        # Prepare the result and print it
        result_message = f"Account with ID {account_id} deleted successfully." if result else f"Failed to delete account with ID {account_id}."
        print(result_message)
        return result_message

    def fetch_all_accounts(self):
        """Fetch all accounts using the DAO."""
        self.account_dao.connect()  # Establish database connection
        try:
            accounts = self.account_dao.fetch_all_accounts()
        except Exception as e:
            return "Error fetching accounts."
        self.account_dao.close()  # Close the connection

        # Prepare the result and print it
        if accounts:
            account_list = "\n".join([f"ID: {acc[0]}, Username: {acc[1]}, Password: {acc[2]}, Website: {acc[3]}" for acc in accounts])
            result_message = f"Accounts:\n{account_list}"
        else:
            result_message = "No accounts found."
        
        print(result_message)
        return result_message

    def fetch_account_by_website(self, website: str):
        """Fetch an account by website."""
        self.account_dao.connect()  # Establish database connection
        account = self.account_dao.fetch_account_by_website(website)  # Fetch the account details from the DAO
        self.account_dao.close()  # Close the connection

        # Check if the account exists and return the raw data
        if account:
            print(f"Account found for {website}: Username: {account[0]}, Password: {account[1]}")
            return account  # Return the raw account tuple (username, password)
        else:
            print(f"No account found for {website}.")
            return None  # Return None if no account was found

