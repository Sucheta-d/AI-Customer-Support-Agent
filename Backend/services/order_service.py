from Backend.database import get_connection

def get_order(order_id: int):
    conn = get_connection()

    order = conn.execute(
        """
        SELECT *
        FROM orders
        WHERE order_id=?
        """,
        (order_id,)
    ).fetchone()

    conn.close()

    return dict(order) if order else None