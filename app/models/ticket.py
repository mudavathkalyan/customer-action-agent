from enum import Enum

from pydantic import BaseModel, Field


class TicketCategory(str, Enum):
    BILLING = "billing"
    TECHNICAL = "technical"
    ACCOUNT = "account"
    GENERAL = "general"


class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class RequestedAction(str, Enum):
    ANSWER_FAQ = "answer_faq"
    CHECK_ORDER_STATUS = "check_order_status"
    ISSUE_REFUND = "issue_refund"
    DELETE_ACCOUNT = "delete_account"
    CHANGE_BILLING_DETAILS = "change_billing_details"


class TicketData(BaseModel):
    category: TicketCategory
    priority: TicketPriority
    customer_id: str = Field(min_length=1)
    requested_action: RequestedAction
    summary: str = Field(min_length=1)