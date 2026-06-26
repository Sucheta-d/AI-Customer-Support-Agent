from Backend.database import get_connection


def log_refund_decision(
        customer_id,
        order_id,
        decision,
        reason
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO refund_requests
        (
            customer_id,
            order_id,
            decision,
            reason
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            customer_id,
            order_id,
            decision,
            reason
        )
    )

    conn.commit()
    conn.close()

    return {
        "status": "saved"
    }