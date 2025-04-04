# src/corp_assistant/dispatcher.py
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", """다음 사용자의 입력을 보고 요청의 목적을 분류하세요:
1. 사내 문서 요약 및 Q&A → 'summary_guide'
2. 개인화된 설명 → 'personalized_intro'
3. 사내 퀴즈 생성 및 피드백 → 'quiz_feedback'
반드시 위의 키워드 중 하나만 출력하세요.
"""),
    ("human", "{profile}\n{question}")
])

def dispatcher_node(state: dict) -> dict:
    user_input = state["input"]
    response = llm(prompt.format_messages(
        profile=user_input["profile"],
        question=user_input["question"]
    ))
    task_type = response.content.strip()
    return {"task_type": task_type, "input_data": user_input}