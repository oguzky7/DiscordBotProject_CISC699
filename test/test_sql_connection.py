from entity.AccountEntity import AccountEntity

def test_sql_connection():
    account_entity = AccountEntity()
    
    # Connect to the database
    account_entity.connect()

    # Clear the table first
    account_entity.clear_users_table()

    # Insert one random user (testKaanUserName, testKaanPassword)
    account_entity.insert_user("testKaanUserName", "testKaanPassword")

    # Insert the default accounts (EBAY and BESTBUY from Config)
    account_entity.add_default_accounts()

    # Fetch and print the users
    users = account_entity.fetch_users()

    # Close the database connection
    account_entity.close()

if __name__ == "__main__":
    test_sql_connection()
