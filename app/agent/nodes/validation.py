from app.agent.state import AgentState


def validation_node(state: AgentState) -> dict:
    ticket = state["ticket_data"]

    errors = []

    if ticket is None:
        errors.append("Ticket data was not extracted.")

    else:
        if not ticket.customer_id.strip():
            errors.append("customer_id cannot be empty.")

        if not ticket.summary.strip():
            errors.append("summary cannot be empty.")

    return {
        "validation_errors": errors
    }