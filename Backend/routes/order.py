from fastapi import APIRouter, HTTPException
from Backend.services.order_service import get_order

router = APIRouter()


@router.get("/order/{order_id}")
def fetch_order(order_id: int):

    order = get_order(order_id)

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order