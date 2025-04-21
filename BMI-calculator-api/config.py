#!/usr/bin/python3
import os

"""
manage settings that might change diff envs without changing code
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'app', 'database.db')