from Backend.services.customer_service import get_customer


def fetch_customer(customer_id: int):
    return get_customer(customer_id)