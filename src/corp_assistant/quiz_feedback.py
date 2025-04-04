# src/corp_assistant/quiz_feedback.py
from langchain_openai import ChatOpenAI
from corp_assistant.rag import get_vectorstore_by_collection
import os

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, streaming=True)
def is_running_in_studio() -> bool:
    try:
        _ = input("테스트 입력: ")  # Studio에선 input 호출 시 EOFError 발생
    except EOFError:
        return True
    return False

def quiz_feedback_node(state: dict):
    is_studio = is_running_in_studio()
    print(f"🧪 실행 환경: {'LangGraph Studio 내부' if is_studio else '로컬'}")
    retriever = get_vectorstore_by_collection("quiz-corp").as_retriever()
    docs = retriever.invoke("온보딩 퀴즈")
    questions = docs[0].page_content.strip()

    print("\n📝 퀴즈:\n" + questions)

    if is_studio:
        input_data = state.get("input_data", {}) or state.get("input", {})
        user_answer = input_data.get("answer")
        if not user_answer:
            raise ValueError("답안이 없습니다. LangGraph Studio에서는 input.answer에 값을 넣어주세요.",state)
    else:
        user_answer = input("\n✍️ 답안을 입력하세요:\n")

    safe_answer = user_answer.encode("utf-8", "ignore").decode("utf-8")

    prompt = f"""
    아래는 퀴즈 문제와 사용자의 답변입니다. GPT로서 적절히 채점하고 상세하게 피드백을 주십시오.

    [문제]
    {questions}

    [답변]
    {safe_answer}

    [피드백 양식]
    점수: xx/100
    강점: ...
    보완할 점: ...
    """

    print("\n📊 채점 결과:")
    feedback_text = ""
    for chunk in llm.stream(prompt):
        print(chunk.content, end="", flush=True)
        feedback_text += chunk.content

    if not is_studio:
        print("\n\n📌 선택하세요:")
        print("1. 부족한 점 자세히 설명해줘")
        print("2. 다시 풀어볼래 (준비 중)")
        print("3. 그만하기")

        choice = input("👉 번호 입력: ").strip()

        if choice == "1":
            print("\n🔍 부족한 점 상세 설명:")
            followup_prompt = f"""
            아래는 GPT가 채점한 퀴즈 피드백입니다.
            '보완할 점' 항목을 바탕으로, 신입 개발자가 이해할 수 있도록 예시와 함께 상세하게 설명해 주세요.

            [피드백 원문]
            {feedback_text}
            """
            for chunk in llm.stream(followup_prompt):
                print(chunk.content, end="", flush=True)

        elif choice == "2":
            print("🔁 다시 풀기 기능은 현재 준비 중입니다.")
        else:
            print("👋 종료합니다.")

    return {"quiz_result": feedback_text}