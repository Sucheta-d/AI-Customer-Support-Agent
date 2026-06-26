from Backend.database import get_connection

def get_policy():
    conn = get_connection()

    policy = conn.execute(
        """
        SELECT policy_text
        FROM refund_policy
        LIMIT 1
        """
    ).fetchone()

    conn.close()

    return policy["policy_text"]