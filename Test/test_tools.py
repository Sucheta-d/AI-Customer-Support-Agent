from Backend.tools.customer_tool import fetch_customer
from Backend.tools.order_tool import fetch_order
from Backend.tools.policy_tool import fetch_policy

print(fetch_customer(1))
print(fetch_order(1))
print(fetch_policy()[:200])