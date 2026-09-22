from langgraph.types import Command, interrupt

from app.agent.state import AgentState


def approval_node(state: AgentState):
    ticket = state["ticket_data"]

    decision = interrupt({
        "type": "human_approval_required",
        "message": "A high-risk action requires approval.",
        "customer_id": ticket.customer_id,
        "action": ticket.requested_action.value,
        "summary": ticket.summary,
    })

    if decision == "approve":
        return {}

    return {
        "messages": state["messages"] + [
            "The requested action was rejected by the manager."
        ],
        "requires_approval": False,
    }

