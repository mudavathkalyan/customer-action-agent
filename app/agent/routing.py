from app.agent.state import AgentState


def validation_router(state: AgentState) -> str:
    if not state["validation_errors"]:
        return "valid"

    if state["retry_count"] < 3:
        return "retry"

    return "failed"