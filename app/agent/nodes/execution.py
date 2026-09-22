from app.agent.state import AgentState


def execution_node(state: AgentState) -> dict:
    ticket = state["ticket_data"]

    action = ticket.requested_action

    print(f"\n[EXECUTION] Executing action: {action}")

    if action == "answer_faq":
        response = "FAQ answer generated for the customer."

    elif action == "check_order_status":
        response = "Order status retrieved successfully."

    elif action == "issue_refund":
        response = "Refund issued successfully."

    elif action == "delete_account":
        response = "Customer account deleted successfully."

    elif action == "change_billing_details":
        response = "Billing details updated successfully."

    else:
        response = "Unknown action."

    return {
        "messages": state["messages"] + [response]
    }