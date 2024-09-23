import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from control.AccountControl import AccountControl  # Import the control layer directly

def test_fetch_accounts():
    account_control = AccountControl()  # Use AccountControl instead of AccountBoundary
    
    # Fetching all accounts
    accounts = account_control.fetch_all_accounts()
    
    if accounts:
        for account in accounts:
            if isinstance(account, tuple) and len(account) == 4:
                print(f"ID: {account[0]}, Username: {account[1]}, Password: {account[2]}, Website: {account[3]}")
    else:
        print("No accounts found.")

def test_fetch_account_by_website(website):
    account_control = AccountControl()  # Use AccountControl instead of AccountBoundary
    
    # Fetch the account by website directly
    account = account_control.fetch_account_by_website(website)
    
    if account:
        # Check if the account is a valid tuple with the correct length
        if isinstance(account, tuple) and len(account) == 2:
            username, password = account  # Unpack the returned tuple
            print(f"Website: {website}, Username: {username}, Password: {password}")
        else:
            print(f"Unexpected data format for account: {account}")
    else:
        print(f"No account found for website: {website}")

if __name__ == "__main__":
    test_fetch_accounts()  # Test fetching all accounts
    test_fetch_account_by_website("ebay")  # Test fetching account for a specific website
