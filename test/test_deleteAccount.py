import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from boundary.AccountBoundary import AccountBoundary

def test_delete_user_account():
    account_boundary = AccountBoundary()
    account_boundary.delete_existing_user(4)

if __name__ == "__main__":
    test_delete_user_account()
