
import psycopg2
from Config import Config

class TemporaryUpdate:
    def __init__(self):
        self.dbname = "postgres"
        self.user = "postgres"
        self.host = "localhost"
        self.port = "5432"
        self.password = Config.DATABASE_PASSWORD

    def connect(self):
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

    def update_website_names(self):
        try:
            if self.cursor:
                self.cursor.execute("UPDATE accounts SET website = LOWER(website)")
                self.connection.commit()
                print("Website names updated to lowercase.")
        except Exception as error:
            print(f"Error updating website names: {error}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database Connection closed.")

if __name__ == "__main__":
    updater = TemporaryUpdate()
    updater.connect()
    updater.update_website_names()
    updater.close()
