from app.agent.state import AgentState
from app.services.llm import structured_llm


def extraction_node(state: AgentState) -> dict:
    message = state["messages"][-1]

    errors = state.get("validation_errors", [])

    error_context = ""

    if errors:
        error_context = f"""
        Previous extraction failed validation.

        Validation errors:
        {errors}

        Correct these problems in your new extraction.
        """

    ticket = structured_llm.invoke(
        f"""
        Extract a structured customer support ticket.

        {error_context}

        Customer message:
        {message}
        """
    )

    return {
        "ticket_data": ticket,
        "validation_errors": [],
        "retry_count": state.get("retry_count", 0) + 1,
    }