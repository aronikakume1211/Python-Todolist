from flask import Flask
from controllers.todo_controller import todo_bp
from controllers.auth_controller import auth_bp
from utils.helpers import remove_pycache 
from dotenv import load_dotenv

load_dotenv() #Loads .env into environment variables
app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(todo_bp)


# def remove_pycache(root_folder):
#     for root, dirs, files in os.walk(root_folder, topdown=False):
#         for dir_name in dirs:
#             if dir_name == '__pycache__':
#                 dir_path = os.path.join(root, dir_name)
#                 print(f'Removing {dir_path}')
#                 shutil.rmtree(dir_path)

if __name__ == "__main__":
    remove_pycache('./') 
    app.run(debug=True)
