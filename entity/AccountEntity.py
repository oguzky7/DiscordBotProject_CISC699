import psycopg2
from Config import Config

class AccountEntity:
    def __init__(self):
        # Static connection details
        self.dbname = "postgres"
        self.user = "postgres"
        self.host = "localhost"
        self.port = "5432"
        self.password = Config.DATABASE_PASSWORD  # Sensitive info from Config.py
    
    def connect(self):
        try:
            # Establish the connection using psycopg2
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as error:
            print(f"Error connecting to the database: {error}")
            self.connection = None
            self.cursor = None
    
    def clear_users_table(self):
        """Clear the users table."""
        try:
            if self.cursor:
                self.cursor.execute("DELETE FROM users;")
                self.connection.commit()
                print("Users table cleared.")
        except Exception as error:
            print(f"Error clearing users table: {error}")
    
    def insert_user(self, username, password):
        """Insert a new user into the users table."""
        try:
            if self.cursor:
                self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                self.connection.commit()
                print(f"User {username} added successfully.")
        except Exception as error:
            print(f"Error inserting user: {error}")
    
    def add_default_accounts(self):
        """Insert default accounts like EBAY and BESTBUY credentials from Config."""
        self.insert_user(Config.EBAY_USERNAME, Config.EBAY_PASSWORD)
        self.insert_user(Config.BESTBUY_USERNAME, Config.BESTBUY_PASSWORD)
    
    def fetch_users(self):
        """Fetch all users from the users table."""
        try:
            if self.cursor:
                self.cursor.execute("SELECT * FROM users;")
                users = self.cursor.fetchall()
                print(users)
                return users
        except Exception as error:
            print(f"Error fetching users: {error}")
            return None
    
    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed.")
