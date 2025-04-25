from bson import ObjectId
from utils.helpers import serialize_todo


class ToDoService:
    def __init__(self, collection):
        self.collection = collection

    def get_all(self):
        return [serialize_todo(t) for t in self.collection.find()]

    def create(self, data):
        new_todo = {"task": data["task"], "done": False}
        result = self.collection.insert_one(new_todo)
        new_todo["_id"] = result.inserted_id
        return serialize_todo(new_todo)

    def update(self, todo_id, data):
        updated = self.collection.find_one_and_update(
            {"_id": ObjectId(todo_id)},
            {"$set": {"done": data["done"]}},
            return_document=True,
        )
        return serialize_todo(updated) if updated else None

    def delete(self, todo_id):
        result = self.collection.delete_one({"_id": ObjectId(todo_id)})
        return result.deleted_count > 0
