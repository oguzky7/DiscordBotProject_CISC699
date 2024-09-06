import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from control.AccountControl import AccountControl

def test_add_account():
    account_control = AccountControl()
    
    # Adding a new account
    account_control.add_account("newUser", "newPassword123")

if __name__ == "__main__":
    test_add_account()
