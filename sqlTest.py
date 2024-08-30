import psycopg2

try:
    # Connect to your postgres DB
    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    # Open a cursor to perform database operations
    cursor = connection.cursor()

    # Execute a command: this creates a new table
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(50), password VARCHAR(50));")

    # Insert a new user
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", ("kaan", "kaanPassword"))

    # Query the database and obtain data as Python objects
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    print(users)

    # Commit your changes in the database
    connection.commit()

except Exception as error:
    print(f"Error: {error}")

finally:
    # Close communication with the database
    if connection:
        cursor.close()
        connection.close()
