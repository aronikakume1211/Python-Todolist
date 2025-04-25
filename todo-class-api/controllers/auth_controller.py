from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from db import db_instance

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1")
auth_service = AuthService(db_instance.get_collection("users"))


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user, error = auth_service.register(data)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(user), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token, error = auth_service.login(data)
    if error:
        return jsonify({"error": error}), 401
    return jsonify({"token": token})
