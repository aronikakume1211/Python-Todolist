from flask import Flask
from flasgger import Swagger
from controllers.todo_controller import todo_bp
from controllers.auth_controller import auth_bp
from utils.helpers import remove_pycache 
from dotenv import load_dotenv

app = Flask(__name__)

#Loads .env into environment variables
load_dotenv() 

# ✅ Customized Swagger configuration
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Todo API",
        "description": "A simple Todo API with Flask",
        "version": "1.0.0"
    },
    "host": "localhost:5000",  # Change to your production host when deploying
    "schemes": ["http"]
})


# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(todo_bp)

if __name__ == "__main__":
    remove_pycache('./') 
    app.run(debug=True)
