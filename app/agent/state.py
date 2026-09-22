from typing import TypedDict

from app.models.ticket import TicketData


class AgentState(TypedDict):
    messages: list
    ticket_data: TicketData | None
    validation_errors: list[str]
    retry_count: int
    requires_approval: bool