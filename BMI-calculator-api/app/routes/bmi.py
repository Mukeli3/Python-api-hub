#!/usr/bin/python3
from flask import Blueprint, request, jsonify
from app.models.bmi_model import BMIModel
import math

bmi = Blueprint('bmi', __name__)

@bmi.route('/calculate', methods=['POST'])
def calculate_bmi():
    if request.json:
        data = request.json
    else:
        data = request.args

    height = float(data['height'])
    weight = float(data['weight'])
    unit_type = data.get('unit_type', 'metric')

    if unit_type == 'metric':
        bmi = weight / (height / 100) ** 2
    else:
        bmi = (weight / (height ** 2)) * 703

    # category
    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    BMIModel.save_calculation(height, weight, unit_type, round(bmi, 2), category)

    return jsonify({
        'bmi': round(bmi, 2),
        'category': category,
        'message': 'Calculation saved!'
    })