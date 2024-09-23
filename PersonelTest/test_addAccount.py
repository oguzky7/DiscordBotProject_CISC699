import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from control.AccountControl import AccountControl

def test_add_account(username, password, website):
    account_control = AccountControl()
    
    # Adding a new account
    result = account_control.add_account(username, password, website)
    if result:
        print(f"Account for {website} added successfully.")
    else:
        print(f"Failed to add account for {website}.")

if __name__ == "__main__":
    test_add_account("newUser", "newPassword123", "newWebsite")  # Change values to test
