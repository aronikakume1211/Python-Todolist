Todo List API (Flask + MongoDB + JWT + Swagger)

This is a modular, OOP-based REST API for managing Todo tasks, built using Flask and MongoDB.
It supports user authentication with JWT and includes Swagger UI for API documentation.

-----------------------------------------
Installation & Setup
-----------------------------------------

1. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate        (Linux/macOS)
   venv\Scripts\activate.bat       (Windows)

2. Install dependencies:
   pip install -r requirements.txt

3. Create a .env file in the root directory with the following content:
   SECRET_KEY=your_secret_key
   MONGO_URI=mongodb://localhost:27017/todo_db

4. Run the application:
   python app.py

-----------------------------------------
API Documentation
-----------------------------------------

Swagger UI is available at:
http://localhost:5000/apidocs

-----------------------------------------
Project Structure
-----------------------------------------

app.py                     - Application entry point
config.py                  - Configuration and environment setup
models/                    - MongoDB models (e.g. Todo, User)
controllers/               - Route handlers using Blueprints
utils/                     - Utility functions (e.g. JWT handling)
.env                       - Environment variables (do not commit)
requirements.txt           - Python dependencies
README.txt                 - Project info and instructions

-----------------------------------------
Developer Notes
-----------------------------------------

To remove all __pycache__ folders:
- Run: python remove_pycache.py

To add new routes, create a function in a controller and register it with the appropriate Blueprint.
Use @swag_from or docstrings to describe endpoints in Swagger UI.

-----------------------------------------
Author
-----------------------------------------

Built by Mebratu Kumera
