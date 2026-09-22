from langgraph.graph import END, START, StateGraph

from app.agent.action_router import action_router
from app.agent.routing import validation_router
from app.agent.state import AgentState

from app.agent.nodes.extraction import extraction_node
from app.agent.nodes.validation import validation_node
from app.agent.nodes.risk import risk_node
from app.agent.nodes.execution import execution_node


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("extract", extraction_node)
    graph.add_node("validate", validation_node)
    graph.add_node("risk_check", risk_node)
    graph.add_node("execute", execution_node)

    graph.add_edge(START, "extract")

    graph.add_edge("extract", "validate")

    graph.add_conditional_edges("validate",validation_router,{
            "valid": "risk_check",
            "retry": "extract",
            "failed": END,
        },
    )

    graph.add_conditional_edges("risk_check",action_router,{
            "execute": "execute",
            "approval": END,
        },
    )

    graph.add_edge("execute", END)

    return graph.compile()