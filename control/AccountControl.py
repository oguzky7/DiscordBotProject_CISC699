from entity.AccountEntity import AccountEntity

class AccountControl:
    def __init__(self):
        self.account_entity = AccountEntity()

    def add_account(self, username, password):
        self.account_entity.connect()
        self.account_entity.add_account(username, password)
        self.account_entity.close()

    def fetch_accounts(self):
        self.account_entity.connect()
        accounts = self.account_entity.fetch_accounts()
        if accounts:
            for account in accounts:
                print(f"ID: {account[0]}, Username: {account[1]}, Password: {account[2]}")
        else:
            print("No accounts found.")
        self.account_entity.close()

    def delete_account(self, account_id):
        self.account_entity.connect()
        self.account_entity.delete_account(account_id)
        self.account_entity.reset_id_sequence()
        self.account_entity.close()
