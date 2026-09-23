from fastapi import APIRouter
from langgraph.types import Command
from pydantic import BaseModel

from app.agent.graph import build_graph


router = APIRouter(prefix="/tickets", tags=["Tickets"])

graph = build_graph()


class TicketRequest(BaseModel):
    message: str


@router.post("")
def create_ticket(request: TicketRequest):
    thread_id = f"ticket-{id(request)}"

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = graph.invoke(
        {
            "messages": [request.message],
            "ticket_data": None,
            "validation_errors": [],
            "retry_count": 0,
            "requires_approval": False,
        },
        config,
    )

    snapshot = graph.get_state(config)

    return {
        "thread_id": thread_id,
        "status": "approval_required" if snapshot.next else "completed",
        "state": result,
    }


@router.post("/{thread_id}/approve")
def approve_ticket(thread_id: str):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = graph.invoke(
        Command(resume="approve"),
        config,
    )

    return {
        "status": "completed",
        "state": result,
    }


@router.post("/{thread_id}/reject")
def reject_ticket(thread_id: str):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = graph.invoke(
        Command(resume="reject"),
        config,
    )

    return {
        "status": "rejected",
        "state": result,
    }