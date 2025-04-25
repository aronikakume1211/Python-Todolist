from flask import Blueprint, request, jsonify
from bson import ObjectId
from db import todos
from utils.helpers import serialize_todo

todo_bp = Blueprint("todos", __name__)

@todo_bp.route("/todos", methods=["GET"])
def get_all_todos():
    return jsonify([serialize_todo(todo) for todo in todos.find()])

@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.json
    new_todo = {"task": data["task"], "done": False}
    result = todos.insert_one(new_todo)
    new_todo["_id"] = result.inserted_id
    return jsonify(serialize_todo(new_todo)), 201

@todo_bp.route("/todos/<id>", methods=["PATCH"])
def update_todo(id):
    data = request.json
    updated = todos.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": {"done": data["done"]}},
        return_document=True
    )
    if updated:
        return jsonify(serialize_todo(updated))
    return jsonify({"error": "Todo not found"}), 404

@todo_bp.route("/todos/<id>", methods=["DELETE"])
def delete_todo(id):
    result = todos.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "Todo deleted"})
    return jsonify({"error": "Todo not found"}), 404
