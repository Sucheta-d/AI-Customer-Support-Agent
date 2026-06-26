from Backend.services.customer_service import get_customer
from Backend.services.order_service import get_order
from Backend.services.policy_service import get_policy

print(get_customer(1))
print(get_order(1))
print(get_policy()[:100])