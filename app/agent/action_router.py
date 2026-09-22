from app.agent.state import AgentState


def action_router(state: AgentState) -> str:
    if state["requires_approval"]:
        return "approval"

    return "execute"