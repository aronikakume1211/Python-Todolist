from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

class DB:
    def __init__(self, uri=MONGO_URI, db_name="todo_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        print("✅ Database connection successfully")

    def get_collection(self, name):
        return self.db[name]


# Instantiate once and reuse
db_instance = DB()
