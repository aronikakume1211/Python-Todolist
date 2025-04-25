from flasgger import swag_from
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

# http://127.0.0.1:5000/apidocs for swagger endpoint
@todo_bp.route('/todos', methods=['GET'])
@swag_from({
    'tags': ['Todos'],
    'description': 'Get all todos',
    'responses': {
        '200': {
            'description': 'List of todos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'task': {'type': 'string'},
                        'completed': {'type': 'boolean'}
                    }
                }
            }
        }
    }
})
def get_todos():
    """
    This endpoint returns a list of todos.
    ---
    """
    todos = [
        {"id": 1, "task": "Finish project", "completed": False},
        {"id": 2, "task": "Read a book", "completed": True}
    ]
    return jsonify(todos)

@todo_bp.route('/todos', methods=['POST'])
@swag_from({
    'tags': ['Todos'],
    'description': 'Create a new todo',
    'parameters': [
        {
            'name': 'task',
            'in': 'body',
            'required': True,
            'type': 'string',
            'description': 'The task description'
        }
    ],
    'responses': {
        '201': {
            'description': 'Todo created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'task': {'type': 'string'},
                    'completed': {'type': 'boolean'}
                }
            }
        }
    }
})
def create_todoo():
    """
    This endpoint creates a new todo.
    ---
    """
    new_todo = {"id": 3, "task": "Go for a walk", "completed": False}
    return jsonify(new_todo), 201

