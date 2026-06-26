# backend/database.py

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
DB_PATH = BASE_DIR /"Database"/"ecommerce.db"
print(DB_PATH)

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn