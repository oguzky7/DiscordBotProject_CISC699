import psycopg2

def fetch_all_users():
    try:
        # Connect to your postgres DB
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",  # Replace with your actual password
            host="localhost",
            port="5432"
        )

        # Open a cursor to perform database operations
        cursor = connection.cursor()

        # Execute a command to fetch all users
        cursor.execute("SELECT * FROM users;")

        # Fetch all rows from the executed query
        users = cursor.fetchall()

        # Print out the users
        for user in users:
            print(f"ID: {user[0]}, Username: {user[1]}, Password: {user[2]}")

    except Exception as error:
        print(f"Error: {error}")

    finally:
        # Close communication with the database
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    fetch_all_users()
