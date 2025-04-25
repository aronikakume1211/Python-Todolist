from flask import Blueprint, request, jsonify
from services.todo_service import ToDoService
from db import db_instance

todo_bp = Blueprint("todos", __name__)
todo_service = ToDoService(db_instance.get_collection("todos"))


@todo_bp.route("/todos", methods=["GET"])
def get_all_todos():
    return jsonify(todo_service.get_all())


@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.json
    return jsonify(todo_service.create(data)), 201


@todo_bp.route("/todos/<id>", methods=["PATCH"])
def update_todo(id):
    data = request.json
    updated = todo_service.update(id, data)
    if updated:
        return jsonify(updated)
    return jsonify({"Error": "Todo not found"}), 404


@todo_bp.route("/todos/<id>", methods=["DELETE"])
def delete_todo(id):
    deleted = todo_service.delete(id)
    if deleted:
        return jsonify({"message": "Todo deleted"})
    return jsonify({"error": "Todo not found"}), 404
