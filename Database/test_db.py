import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "ecommerce.db"
conn = sqlite3.connect(DB_PATH)

customers = pd.read_sql(
    "SELECT * FROM customers",
    conn
)

orders = pd.read_sql(
    "SELECT * FROM orders",
    conn
)

policy = pd.read_sql(
    "SELECT * FROM refund_policy",
    conn
)

print(customers.head())
print("\n")
print(orders.head())
print("\n")
print(policy.iloc[0]["policy_text"])

conn.close()