from langgraph.graph import StateGraph
from corp_assistant.dispatcher import dispatcher_node
from corp_assistant.quiz_feedback import quiz_feedback_node
from corp_assistant.summary_guide import summary_guide_node
from corp_assistant.personalized_intro import personalized_intro_node

QUIZ = "quiz_feedback"
SUMMARY = "summary_guide"
PERSONAL = "personalized_intro"

builder = StateGraph(dict)

builder.add_node("dispatcher", dispatcher_node)
builder.add_node(QUIZ, quiz_feedback_node)
builder.add_node(SUMMARY, summary_guide_node)
builder.add_node(PERSONAL, personalized_intro_node)

builder.set_entry_point("dispatcher")

def determine_branch(state: dict) -> str:
    return state["task_type"]

builder.add_conditional_edges(
    source="dispatcher",
    path=determine_branch,
    path_map={
        QUIZ: QUIZ,
        SUMMARY: SUMMARY,
        PERSONAL: PERSONAL
    }
)

builder.set_finish_point(QUIZ)
builder.set_finish_point(SUMMARY)
builder.set_finish_point(PERSONAL)

graph = builder.compile()
import json

# LangGraph Studio에서 사용할 graphstudio.json 파일 생성
graphstudio_project = {
    "dockerfile_lines": [],
    "graphs": {
        "main": "./src/corp_assistant/graph.py:graph"  # 모듈 경로:변수명
    },
    "env": "./.env",
    "python_version": "3.11",
    "dependencies": [
        "."  # 현재 Poetry 프로젝트 기준
    ]
}
with open("langgraph.json", "w", encoding="utf-8") as f:
    json.dump(graphstudio_project, f, indent=2, ensure_ascii=False)

print("✅ LangGraph Studio용 graphstudio.json 생성 완료")