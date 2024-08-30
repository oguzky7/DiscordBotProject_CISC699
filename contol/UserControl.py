from DatabaseEntity import DatabaseEntity

class UserControl:
    def __init__(self):
        self.database_entity = DatabaseEntity(dbname="mydatabase", user="postgres", password="your_password")

    def get_user(self, username):
        user_data = self.database_entity.fetch_user(username)
        return user_data
