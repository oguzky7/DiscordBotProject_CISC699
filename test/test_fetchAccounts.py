import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from boundary.AccountBoundary import AccountBoundary

def test_fetch_user_accounts():
    account_boundary = AccountBoundary()
    account_boundary.display_users()

if __name__ == "__main__":
    test_fetch_user_accounts()
