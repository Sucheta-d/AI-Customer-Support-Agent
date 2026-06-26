from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from Backend.graphs.state import RefundState
from Backend.graphs.nodes import *

builder = StateGraph(RefundState)

builder.add_node(
    "load_customer",
    load_customer
)

builder.add_node(
    "load_order",
    load_order
)

builder.add_node(
    "load_policy",
    load_policy
)

builder.add_node(
    "refund_decision",
    refund_decision
)

builder.add_node(
    "log_decision",
    log_decision
)

builder.add_edge(
    START,
    "load_customer"
)

builder.add_edge(
    "load_customer",
    "load_order"
)

builder.add_edge(
    "load_order",
    "load_policy"
)

builder.add_edge(
    "load_policy",
    "refund_decision"
)

builder.add_edge(
    "refund_decision",
    "log_decision"
)

builder.add_edge(
    "log_decision",
    END
)

refund_graph = builder.compile()