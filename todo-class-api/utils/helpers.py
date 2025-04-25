import os
import shutil

def serialize_todo(todo):
    return {
        "id": str(todo["_id"]),
        "task": todo["task"],
        "done": todo.get("done", False),
    }


def serialize_user(user):
    return {"id": str(user["_id"]), "email": user["email"]}


def remove_pycache(root_folder):
    for root, dirs, files in os.walk(root_folder, topdown=False):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                dir_path = os.path.join(root, dir_name)
                print(f"Removing {dir_path}")
                shutil.rmtree(dir_path)
