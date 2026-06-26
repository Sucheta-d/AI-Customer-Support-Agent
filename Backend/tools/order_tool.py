from Backend.services.order_service import get_order


def fetch_order(order_id: int):
    return get_order(order_id)