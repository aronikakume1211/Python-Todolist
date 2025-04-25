from flask import Blueprint, request, jsonify
from services.todo_service import ToDoService
from db import db_instance
from utils.jwt_manager import token_required

todo_bp = Blueprint("todos", __name__, url_prefix="/api/v1")
todo_service = ToDoService(db_instance.get_collection("todos"))


@todo_bp.route("/todos", methods=["GET"])
@token_required
def get_all_todos():
    return jsonify(todo_service.get_all(request.user_id))


@todo_bp.route("/todos", methods=["POST"])
@token_required
def create_todo():
    data = request.json
    return jsonify(todo_service.create(data, request.user_id)), 201


@todo_bp.route("/todos/<id>", methods=["PATCH"])
@token_required
def update_todo(id):
    data = request.json
    updated = todo_service.update(id, data, request.user_id)
    if updated:
        return jsonify(updated)
    return jsonify({"Error": "Todo not found"}), 404


@todo_bp.route("/todos/<id>", methods=["DELETE"])
@token_required
def delete_todo(id):
    deleted = todo_service.delete(id, request.user_id)
    if deleted:
        return jsonify({"message": "Todo deleted"})
    return jsonify({"error": "Todo not found"}), 404
