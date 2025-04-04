from langgraph.graph import StateGraph

builder = StateGraph(dict)

def determine_branch(state: dict) -> str:
    return "quiz_feedback"

builder.add_node("dispatcher", lambda x: x)
builder.add_node("quiz_feedback", lambda x: x)

builder.add_conditional_edges(
    source="dispatcher",
    path=determine_branch,  # ✅ 핵심
    path_map={"quiz_feedback": "quiz_feedback"}
)

print("✅ 분기 로직 정상 등록됨!")