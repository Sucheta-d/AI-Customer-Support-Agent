import sqlite3
import pandas as pd
import traceback
from pathlib import Path
print("Database initialization started...")


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "ecommerce.db"


try:
    # Connect to SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ==========================
    # Create Customers Table
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (                 
        customer_id INTEGER PRIMARY KEY,
        name NOT NULL,
        email TEXT,
        loyalty_level TEXT,
        total_orders INTEGER,
        vip INTEGER,
        account_status TEXT,
        signup_date TEXT,
        last_order_date TEXT,
        fraud_flag INTEGER
    )
    """)

    # ==========================
    # Create Orders Table
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product TEXT,
        category TEXT,
        price REAL,
        purchase_date TEXT,
        delivered INTEGER,
        packaging_available INTEGER,
        delivery_status_note TEXT,
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
    )
    """)

    # ==========================
    # Create Refund Policy Table
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS refund_policy (
        id INTEGER PRIMARY KEY,
        policy_text TEXT
    )
    """)

    # ==========================
    # Create Refund Requests Table
    # (for logging agent decisions)
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS refund_requests (
        refund_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        order_id INTEGER,
        decision TEXT,
        reason TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id)
            REFERENCES customers(customer_id),
        FOREIGN KEY (order_id)
            REFERENCES orders(order_id)
    )
    """)

    # ==========================
    # Clear existing data
    # ==========================
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM customers")
    cursor.execute("DELETE FROM refund_policy")

    # ==========================
    # Load CSV files
    # ==========================
    customers_df = pd.read_csv("../Data/customers.csv", sep=",")
    print(customers_df.columns)
    orders_df = pd.read_csv("../Data/orders.csv", sep=",")

    # Insert data
    customers_df.to_sql(
        "customers",
        conn,
        if_exists="append",
        index=False
    )

    orders_df.to_sql(
        "orders",
        conn,
        if_exists="append",
        index=False
    )

    # ==========================
    # Load refund policy
    # ==========================
    with open("../Data/refund_policy.txt", "r", encoding="utf-8") as f:
        policy_text = f.read()

    cursor.execute(
        """
        INSERT INTO refund_policy (id, policy_text)
        VALUES (?, ?)
        """,
        (1, policy_text)
    )

    # Save changes
    conn.commit()

    print("Database initialized successfully!")

    # ==========================
    # Verification
    # ==========================
    customer_count = cursor.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()[0]

    order_count = cursor.execute(
        "SELECT COUNT(*) FROM orders"
    ).fetchone()[0]

    print(f"Customers inserted: {customer_count}")
    print(f"Orders inserted: {order_count}")

except Exception as e:
    print("Error:", e)
    traceback.print_exc()

finally:
    conn.close()
    print("Database connection closed.")