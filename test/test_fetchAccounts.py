import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from control.AccountControl import AccountControl

def test_fetch_accounts():
    account_control = AccountControl()
    
    # Fetching all accounts
    account_control.fetch_accounts()

if __name__ == "__main__":
    test_fetch_accounts()
