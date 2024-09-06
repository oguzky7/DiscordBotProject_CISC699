import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from boundary.AccountBoundary import AccountBoundary

def test_add_user_account():
    account_boundary = AccountBoundary()
    account_boundary.add_new_user("newUser", "newPassword123")

if __name__ == "__main__":
    test_add_user_account()
