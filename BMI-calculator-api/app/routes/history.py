#!/usr/bin/python3
from flask import Blueprint, jsonify
from app.models.bmi_model import BMIModel

history = Blueprint('history', __name__)

@history.route('/history', methods=['GET'])
def get_history():
    records = BMIModel.get_history()
    history_list = [dict(record) for record in records]
    return jsonify(history_list)