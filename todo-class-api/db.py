from pymongo import MongoClient


class DB:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="todo_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, name):
        return self.db[name]


# Instantiate once and reuse
db_instance = DB()
