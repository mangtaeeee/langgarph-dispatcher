# src/corp_assistant/run_quiz.py
from corp_assistant.graph import graph

if __name__ == "__main__":
    input_data = {
        "input": {
            "profile": "신입 백엔드 개발자입니다.",
            "question": "온보딩 퀴즈 풀고 싶어요."
        }
    }
    result = graph.invoke(input_data)
    print("\n\n\n\n🎯 AI 통해서 응답온 결과:", result)