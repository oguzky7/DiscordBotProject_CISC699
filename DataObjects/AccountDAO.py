import psycopg2
from utils.Config import Config
from DataObjects.AccountDTO import AccountDTO

class AccountDAO:
    def __init__(self):
        self.dbname = "postgres"
        self.user = "postgres"
        self.host = "localhost"
        self.port = "5432"
        self.password = Config.DATABASE_PASSWORD

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Database Connection Established.")
        except Exception as error:
            print(f"Error connecting to the database: {error}")
            self.connection = None
            self.cursor = None

    def add_account(self, account_dto: AccountDTO):
        """Add a new account to the database using DTO."""
        try:
            query = "INSERT INTO accounts (username, password, website) VALUES (%s, %s, %s)"
            values = (account_dto.username, account_dto.password, account_dto.website)
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"Account {account_dto.username} added successfully.")
            return True
        except Exception as error:
            print(f"Error inserting account: {error}")
            return False


    def fetch_account_by_website(self, website):
        """Fetch account credentials for a specific website."""
        try:
            query = "SELECT username, password FROM accounts WHERE LOWER(website) = LOWER(%s)"
            self.cursor.execute(query, (website,))
            return self.cursor.fetchone()
        except Exception as error:
            print(f"Error fetching account for website {website}: {error}")
            return None

    def fetch_all_accounts(self):
        """Fetch all accounts from the database."""
        try:
            query = "SELECT id, username, password, website FROM accounts"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as error:
            print(f"Error fetching accounts: {error}")
            return []
        

    def delete_account(self, account_id):
        """Delete an account by its ID."""
        try:
            self.cursor.execute("DELETE FROM accounts WHERE id = %s", (account_id,))
            self.connection.commit()
            if self.cursor.rowcount > 0:  # Check if any rows were affected
                print(f"Account with ID {account_id} deleted successfully.")
                return True
            else:
                print(f"No account found with ID {account_id}.")
                return False
        except Exception as error:
            print(f"Error deleting account: {error}")
            return False
        
    def reset_id_sequence(self):
        """Reset the ID sequence to the maximum ID."""
        try:
            reset_query = "SELECT setval('accounts_id_seq', (SELECT MAX(id) FROM accounts))"
            self.cursor.execute(reset_query)
            self.connection.commit()
            print("ID sequence reset successfully.")
        except Exception as error:
            print(f"Error resetting ID sequence: {error}")


    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
