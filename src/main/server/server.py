from flask import Flask
from flask_cors import CORS
from src.main.routes.pets_routes import pet_routes_bp
from src.models.mysql.settings.connection import db_connection_handler

routes = [pet_routes_bp]

db_connection_handler.connect_to_db()

app = Flask(__name__)

CORS(app)

for i in routes:
    app.register_blueprint(i)