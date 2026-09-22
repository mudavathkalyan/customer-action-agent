from app.agent.state import AgentState
from app.models.ticket import RequestedAction


HIGH_RISK_ACTIONS = {
    RequestedAction.ISSUE_REFUND,
    RequestedAction.DELETE_ACCOUNT,
    RequestedAction.CHANGE_BILLING_DETAILS,
}


def risk_node(state: AgentState) -> dict:
    ticket = state["ticket_data"]

    requires_approval = (
        ticket.requested_action in HIGH_RISK_ACTIONS
    )

    return {
        "requires_approval": requires_approval
    }