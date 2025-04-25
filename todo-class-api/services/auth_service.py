from flask_bcrypt import Bcrypt
from bson import ObjectId
from utils.jwt_manager import generate_token
from utils.helpers import serialize_user

bcrypt = Bcrypt()


class AuthService:
    def __init__(self, user_collection):
        self.users = user_collection

    def register(self, data):
        if self.users.find_one({"email": data["email"]}):
            return None, "Email already exists"

        hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
        user = {"email": data["email"], "password": hashed_pw}
        result = self.users.insert_one(user)
        user["_id"] = result.inserted_id
        return serialize_user(user), None

    def login(self, data):
        user = self.users.find_one({"email": data["email"]})
        if user and bcrypt.check_password_hash(user["password"], data["password"]):
            token = generate_token(user["_id"])
            return token, None
        return None, "Invalid credentials"
