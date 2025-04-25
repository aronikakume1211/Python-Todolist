def serialize_todo(todo):
    return {
        "id": str(todo["_id"]),
        "task": todo["task"],
        "done": todo.get("done", False),
    }
