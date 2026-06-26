from Backend.tools.customer_tool import fetch_customer
from Backend.tools.order_tool import fetch_order
from Backend.tools.policy_tool import fetch_policy
from Backend.tools.refund_tool import (
    log_refund_decision
)
from Backend.agents.refund_agent import refund_chain
from datetime import datetime
def load_customer(state):
    trace = state.get("trace", [])

    trace.append(
        f"[{datetime.now().strftime('%H:%M:%S')}]Loading customer {state['customer_id']}"
    )
    customer = fetch_customer(
        state["customer_id"]
    )
    trace.append(
        f"[{datetime.now().strftime('%H:%M:%S')}]Customer found: {customer['name']}"
    )

    return {
        "customer": customer,
        "trace": trace
    }

def load_order(state):

    trace = state.get("trace", [])

    trace.append(
        f"[{datetime.now().strftime('%H:%M:%S')}]Loading order {state['order_id']}"
    )

    order = fetch_order(
        state["order_id"]
    )
    trace.append(
        f"[{datetime.now().strftime('%H:%M:%S')}]Loaded order {state['order_id']}"
    )

    return {
        "order": order,
        "trace": trace
    }

def load_policy(state):

    trace = state.get("trace", [])

    trace.append(
        f"[{datetime.now().strftime('%H:%M:%S')}]Loading refund policy"
    )

    policy = fetch_policy()

    trace.append(
        f"[{datetime.now().strftime('%H:%M:%S')}]Refund policy loaded successfully"
    )

    return {
        "policy": policy,
        "trace": trace
    }


def refund_decision(state):
    trace = state.get("trace", [])

    trace.append(
        f"[{datetime.now().strftime('%H:%M:%S')}]Calling llama-3.1-8b-instant"
        )
    try:
        result = refund_chain.invoke(
            {
                "policy": state["policy"],
                "customer": state["customer"],
                "order": state["order"],
                "refund_reason": state["reason"]
            }
        )
        trace.append(
            f"[{datetime.now().strftime('%H:%M:%S')}]Decision generated: {result.decision}"
        )
            

        return {
            "decision": result.decision,
            "reason": result.reason,
            "trace": trace

        }

    except Exception as e:
        return {
            "decision": "DENIED",
            "reason": f"Agent Error: {str(e)}"
        }

def log_decision(state):

    log_refund_decision(
        customer_id=state["customer_id"],
        order_id=state["order_id"],
        decision=state["decision"],
        reason=state["reason"]
    )
    return {}