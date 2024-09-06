import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.AccountEntity import AccountEntity

def test_add_user_account():
    account_entity = AccountEntity()
    
    account_entity.connect()

    account_entity.insert_user("newUser", "newPassword123")

    account_entity.close()

if __name__ == "__main__":
    test_add_user_account()
