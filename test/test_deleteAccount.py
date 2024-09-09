import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from control.AccountControl import AccountControl

def test_delete_account():
    account_control = AccountControl()
    
    account_control.delete_account(4)

if __name__ == "__main__":
    test_delete_account()
