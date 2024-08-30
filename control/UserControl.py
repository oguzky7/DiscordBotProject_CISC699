from entity.DatabaseEntity import DatabaseEntity
from Config import Config

class UserControl:
    def __init__(self):
        self.database_entity = DatabaseEntity(dbname="postgres", user="postgres", password=Config.SQL_Password)

    def get_user(self, username):
        user_data = self.database_entity.fetch_user(username)
        return user_data
