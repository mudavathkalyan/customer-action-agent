from app.services.llm import structured_llm


message = """
Hi, I'm Ravi, customer ID CUST-9281.

I was charged twice for my subscription this month.
I need one of the charges refunded.

This is pretty urgent because the extra charge is causing problems.
"""


ticket = structured_llm.invoke(
    f"""
Extract the customer support ticket information
from the following message.

Customer message:
{message}
"""
)

print(ticket)
print()
print(ticket.model_dump())