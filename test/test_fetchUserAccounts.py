import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.AccountEntity import AccountEntity

def fetch_User_Accounts():
    account_entity = AccountEntity()
    
    account_entity.connect()

    account_entity.fetch_users()

    account_entity.close()

if __name__ == "__main__":
    fetch_User_Accounts()
