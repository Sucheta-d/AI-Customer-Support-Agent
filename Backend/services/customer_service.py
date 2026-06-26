from Backend.database import get_connection

def get_customer(customer_id: int):
    conn = get_connection()

    customer = conn.execute(
        """
        SELECT *
        FROM customers
        WHERE customer_id=?
        """,
        (customer_id,)
    ).fetchone()

    conn.close()

    return dict(customer) if customer else None