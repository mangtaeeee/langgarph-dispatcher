# src/corp_assistant/load_quiz.py

from dotenv import load_dotenv
import os
from corp_assistant.rag import get_vectorstore_by_collection

# ✅ OpenAI API 키 로드
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

quiz_text = """
[신입 개발자 온보딩 퀴즈]

Q1. HTTP와 HTTPS의 차이를 간단히 설명하시오.
Q2. REST API의 주요 특징을 2가지 이상 서술하시오.
Q3. Git에서 merge와 rebase의 차이를 설명하시오.
"""

if __name__ == "__main__":
    vectorstore = get_vectorstore_by_collection("quiz-corp")
    vectorstore.add_texts([quiz_text])
    print("✅ 'quiz-corp' 컬렉션에 퀴즈 데이터 삽입 완료")