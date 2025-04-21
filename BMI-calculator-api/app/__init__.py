#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
from config import DATABASE
from app.models.bmi_model import BMIModel

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['DATABASE'] = DATABASE

    BMIModel.init_db()

    from app.routes.bmi import bmi
    from app.routes.history import history

    app.register_blueprint(bmi)
    app.register_blueprint(history)

    return app