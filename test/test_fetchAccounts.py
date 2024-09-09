import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from control.AccountControl import AccountControl

def test_fetch_accounts():
    account_control = AccountControl()
    
    # Fetching all accounts
    account_control.fetch_accounts()

def test_fetch_account_by_website(website):
    account_control = AccountControl()
    
    # Fetch the account by website directly
    account = account_control.fetch_account_by_website(website)
    
    if account:
        username, password = account  # Unpack the returned tuple
        print(f"Website: {website}, Username: {username}, Password: {password}")
    else:
        print(f"No account found for website: {website}")    

if __name__ == "__main__":
    test_fetch_accounts()
    test_fetch_account_by_website("ebay")
