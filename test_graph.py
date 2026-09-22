from app.agent.graph import build_graph


graph = build_graph()

result = graph.invoke(
    {
        "messages": [
            """
            My customer ID is CUST-1001.
            I was charged twice for my order.
            Please refund the duplicate payment.
            """
        ],
        "ticket_data": None,
        "validation_errors": [],
        "retry_count": 0,
        "requires_approval": False,
    }
)

print("\nFINAL STATE")
print(result)