from pydantic import BaseModel


class RefundRequest(BaseModel):
    customer_id: int
    order_id: int
    reason: str