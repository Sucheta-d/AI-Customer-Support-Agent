from Backend.agents.refund_agent import refund_chain

policy = """
Refunds are allowed within 30 days of delivery.
Refunds are denied for fraudulent customers.
"""

customer = {
    "customer_id": 1,
    "name": "John",
    "fraud_flag": 0,
    "vip": 1
}

order = {
    "order_id": 1,
    "product_name": "Laptop",
    "status": "Delivered"
}

result = refund_chain.invoke(
    {
        "policy": policy,
        "customer": customer,
        "order": order
    }
)

print(result)
print(result.decision)
print(result.reason)