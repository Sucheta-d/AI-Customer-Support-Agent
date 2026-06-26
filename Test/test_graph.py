from Backend.graphs.refund_graph import (
    refund_graph
)

result = refund_graph.invoke(
    {
        "customer_id": 1,
        "order_id": 1
    }
)

print(result)