#!usr/bin/python3
import sqlite3
from datetime import datetime
from config import DATABASE


class BMIModel:
    @staticmethod
    def get_db_connection():
        con = sqlite3.connect(DATABASE) # reps connection to the db file
        con.row_factory = sqlite3.Row # dict results instead of tuple, access columns by name
        return con

    @staticmethod
    def init_db():
        with open('app/schemas/schema.sql') as f:
            schema = f.read()

        con = BMIModel.get_db_connection()
        con.executescript(schema)
        con.close()

    @staticmethod
    def save_calculation(height, weight, unit_type, bmi, category):
        con = BMIModel.get_db_connection()
        con.execute(
            'INSERT INTO bmi_records (height, weight, unit_type, bmi, category, created_at) '
            'VALUES (?, ?, ?, ?, ?, ?)',
            (height, weight, unit_type, bmi, category, datetime.now())
        )
        con.commit()
        con.close()

    @staticmethod
    def get_history():
        con = BMIModel.get_db_connection()
        records = con.execute(
            'SELECT * FROM bmi_records ORDER BY created_at DESC'
        ).fetchall()
        con.close()
        return records