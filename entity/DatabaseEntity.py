import psycopg2

class DatabaseEntity:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,  # Make sure this is the correct password
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

    def fetch_user(self, username):
        query = "SELECT username, password FROM users WHERE username = %s;"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()
