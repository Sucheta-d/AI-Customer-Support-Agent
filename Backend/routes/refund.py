from fastapi import APIRouter
from Backend.schemas.refund_schema import RefundRequest
from Backend.graphs.refund_graph import refund_graph

router = APIRouter()

@router.get("/refund/logs")
def get_refund_logs():
    from Backend.database import get_connection
    import pandas as pd

    conn = get_connection()

    query = """
    SELECT *
    FROM refund_requests
    ORDER BY timestamp DESC
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df.to_dict(orient="records")

@router.post("/refund")
def create_refund(request: RefundRequest):

    result = refund_graph.invoke(
        {
            "customer_id": request.customer_id,
            "order_id": request.order_id,
            "reason": request.reason,
            "trace": []
        }
    )

    return {
        "customer_id": request.customer_id,
        "order_id": request.order_id,
        "decision": result["decision"],
        "reason": result["reason"],
        "trace": result["trace"]
    }