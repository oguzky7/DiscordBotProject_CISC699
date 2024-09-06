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
            print(f"Database Connection Established Successfully ")
        except Exception as error:
            print(f"Error connecting to the database: {error}")
            self.connection = None
            self.cursor = None

    def insert_user(self, username, password):
        """Insert a new user into the users table."""
        try:
            if self.cursor:
                self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                self.connection.commit()
                print(f"User {username} added successfully.")
        except Exception as error:
            print(f"Error inserting user: {error}")
    
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
    
    def delete_user(self, user_id):
        """Delete a user by ID and reset the sequence."""
        try:
            if self.cursor:
                # Delete user with the given ID
                self.cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
                rows_deleted = self.cursor.rowcount  # Get the number of rows affected by the delete
                self.connection.commit()

                if rows_deleted > 0:
                    print(f"User with ID {user_id} deleted successfully.")
                    
                    # Fetch the maximum ID from the table
                    self.cursor.execute("SELECT COALESCE(MAX(id), 0) FROM users;")
                    max_id = self.cursor.fetchone()[0]

                    # Reset the ID sequence based on the maximum ID
                    self.cursor.execute(f"ALTER SEQUENCE users_id_seq RESTART WITH {max_id + 1};")
                    self.connection.commit()
                    print(f"ID sequence reset to {max_id + 1}.")
                else:
                    print(f"User with ID {user_id} does not exist. Nothing to delete.")
                    
        except Exception as error:
            print(f"Error deleting user: {error}")

    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed.")
