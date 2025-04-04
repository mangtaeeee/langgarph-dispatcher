# 🧠 corp-assistant

이 프로젝트는 **LangGraph + Qdrant + OpenAI** 기반으로 사내 온보딩을 자동화하는 AI 비서입니다.  
**온보딩 퀴즈 채점**, **사내 문서 요약**, **개인 맞춤 소개**를 하나의 흐름으로 구성하고  
**LangGraph Studio**를 통해 시각화 및 실행할 수 있도록 설계되었습니다.


---

## 📌 주요 기능

### 1. 회사/서비스 이해
- **입력**: 사용자의 프로필 정보
- **처리**: 회사 소개 문서, 제품 정보 등을 기반으로 요약 및 개인화
- **출력**: 직무 맞춤형 설명 제공

### 2. 온보딩 퀴즈 평가
- **입력**: 사용자의 퀴즈 답변
- **처리**: 사내 정보 기반 퀴즈 생성 → LLM 채점 → 피드백
- **출력**: 점수, 강점, 보완할 점

### 3. 사내 규정 안내
- **입력**: 프로필 + 질문
- **처리**: 문서 요약 + RAG 기반 Q&A
- **출력**: 요약된 직무 맞춤형 규정 설명

---

## ▶️ 실행 방법

### Poetry 기반 로컬 실행

```bash
PYTHONPATH=src poetry run python src/corp_assistant/run_quiz.py

입력 예시

{
  "input": {
    "profile": "신입 백엔드 개발자입니다.",
    "question": "온보딩 퀴즈 풀고 싶어요.",
    "answer": "1. HTTP는 보안이 없고 HTTPS는 보안됨\n2. REST는 자원 중심\n3. merge는 병합, rebase는 기록 재작성"
  }
}



⸻

🧪 LangGraph Studio 사용법
	•	graphstudio.json 파일을 기반으로 Studio에서 불러올 수 있습니다.
	•	입력은 State 탭에 아래와 같이 작성:

{
  "input": {
    "profile": "신입 백엔드 개발자입니다.",
    "question": "온보딩 퀴즈 풀고 싶어요.",
    "answer": "..."
  }
}

❗ 정답 입력이 없을 경우 Studio에서는 ValueError를 통해 안내합니다.

⸻

🧱 구성 파일 구조

파일 경로	설명
graph.py	LangGraph StateGraph 정의
dispatcher.py	목적 분류 LLM 노드
quiz_feedback.py	퀴즈 수행 및 피드백 노드
summary_guide.py	사내 문서 요약 + Q&A 노드
personalized_intro.py	개인화된 회사 설명 노드
rag.py	Qdrant 연결 및 벡터스토어 설정
run_quiz.py	로컬 실행용 엔트리포인트
graphstudio.json	LangGraph Studio 실행 설정


⸻

## 🧱 아키텍처

```mermaid
graph TD
  Start[Start (__start__)] -->|input| Dispatcher
  Dispatcher -->|task_type: quiz_feedback| QuizFeedback
  Dispatcher -->|task_type: summary_guide| SummaryGuide
  Dispatcher -->|task_type: personalized_intro| PersonalizedIntro
  QuizFeedback --> End
  SummaryGuide --> End
  PersonalizedIntro --> End


⸻

✅ 개발 상태
	•	LangGraph 기반 흐름 구성
	•	Qdrant 벡터스토어 연동
	•	LangGraph Studio 시각화 및 실행 확인
	•	입력 기반 분기 처리
	•	고도화된 피드백 및 퀴즈 재도전 기능 추가 예정

⸻
