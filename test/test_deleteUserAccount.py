import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.AccountEntity import AccountEntity

def test_delete_user_account():
    account_entity = AccountEntity()
    
    # Connect to the database
    account_entity.connect()

    # Delete user with ID 4
    account_entity.delete_user(4)

    # Close the database connection
    account_entity.close()

if __name__ == "__main__":
    test_delete_user_account()
