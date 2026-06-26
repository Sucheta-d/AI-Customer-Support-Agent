from fastapi import APIRouter, HTTPException
from Backend.services.customer_service import get_customer

router = APIRouter()


@router.get("/customer/{customer_id}")
def fetch_customer(customer_id: int):

    customer = get_customer(customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer