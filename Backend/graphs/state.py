from typing import TypedDict


class RefundState(TypedDict):
    customer_id: int
    order_id: int
    reason: str

    customer: dict
    order: dict
    policy: str

    decision: str
    explanation: str

    trace: list[str]