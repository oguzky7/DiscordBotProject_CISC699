from entity.AccountEntity import AccountEntity

class AccountControl:
    def __init__(self):
        self.account_entity = AccountEntity()

    def add_account(self, username, password, webSite):
        self.account_entity.connect()
        self.account_entity.add_account(username, password, webSite)
        self.account_entity.close()

    def fetch_accounts(self):
        """Fetch all accounts and return them."""
        self.account_entity.connect()
        accounts = self.account_entity.fetch_accounts()
        
        if accounts:
            account_messages = []
            for account in accounts:
                message = f"ID: {account[0]}, Username: {account[1]}, Password: {account[2]}, Website: {account[3]}"
                print(message)  # For terminal output
                account_messages.append(message)
            self.account_entity.close()
            return account_messages
        else:
            print("No accounts found.")  # For terminal output
            self.account_entity.close()
            return ["No accounts found."]


    def delete_account(self, account_id):
        self.account_entity.connect()
        self.account_entity.delete_account(account_id)
        self.account_entity.reset_id_sequence()
        self.account_entity.close()
