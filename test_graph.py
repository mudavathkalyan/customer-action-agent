from app.agent.graph import build_graph

# My customer ID is CUST-1001.
# I was charged  for my subscription.
# may i know the next subscription amount.

graph = build_graph()

config = {
    "configurable": {
        "thread_id": "ticket-1001"
    }
}

graph.invoke(
    {
        "messages": [
            """
            My customer ID is CUST-1001.
            I was charged twice for my subscription.
            Please refund the duplicate charge.
            """
        ],
        "ticket_data": None,
        "validation_errors": [],
        "retry_count": 0,
        "requires_approval": False,
    },
    config,
)

snapshot = graph.get_state(config)

print("\nCURRENT STATE:")
print(snapshot.values)

print("\nNEXT:")
print(snapshot.next)