# 🧠 corp-assistant

**corp-assistant**는 LangGraph, Qdrant, OpenAI 기반으로 구축된 **사내 온보딩 AI 비서**입니다.  
온보딩 퀴즈 평가, 사내 문서 요약, 개인화된 서비스 소개를 하나의 흐름으로 구성하며,  
**LangGraph Studio**를 통해 구조를 시각화하고 직접 실행할 수 있도록 설계되었습니다.

---

## ✨ 주요 기능

### 🔹 1. 회사/서비스 이해
- **입력**: 사용자 프로필 정보
- **처리**: 회사 소개, 제품 정보, 핵심 가치 등을 바탕으로 직무에 맞게 요약
- **출력**: 개인화된 설명 (개발자/비개발자 구분)

### 🔹 2. 온보딩 퀴즈 평가
- **입력**: 퀴즈 정답
- **처리**: 사내 문서 기반 퀴즈 생성 → LLM 채점 → 상세 피드백 생성
- **출력**: 점수, 강점, 보완할 점 등

### 🔹 3. 사내 규정 안내
- **입력**: 사용자 프로필 + 질문
- **처리**: 긴 규정 문서 요약 및 RAG 기반 Q&A 처리
- **출력**: 직무 맞춤형 규정 설명

---

## ▶️ 실행 방법

### 🧪 로컬 실행 (Poetry)

```bash
PYTHONPATH=src poetry run python src/corp_assistant/run_quiz.py

입력 예시:

{
  "input": {
    "profile": "신입 백엔드 개발자입니다.",
    "question": "온보딩 퀴즈 풀고 싶어요.",
    "answer": "1. HTTP는 보안이 없고 HTTPS는 보안됨\n2. REST는 자원 중심\n3. merge는 병합, rebase는 기록 재작성"
  }
}



⸻

🧱 LangGraph Studio 실행
	1.	graphstudio.json 파일을 기반으로 Studio에서 프로젝트를 불러옵니다.
	2.	Start 노드의 State 탭에 아래 형식으로 입력하세요:

{
  "input": {
    "profile": "신입 백엔드 개발자입니다.",
    "question": "온보딩 퀴즈 풀고 싶어요.",
    "answer": "..."
  }
}

⚠️ 정답(answer) 미입력 시, Studio 환경에서는 ValueError를 통해 안내됩니다.

⸻

📁 파일 구성

파일명	설명
graph.py	LangGraph 플로우 정의
dispatcher.py	사용자의 요청 목적을 분류하는 LLM 노드
quiz_feedback.py	퀴즈 문제 노출, 정답 입력, LLM 채점 및 피드백 생성
summary_guide.py	사내 문서 요약 및 Q&A 처리
personalized_intro.py	직무별 개인화된 회사/서비스 소개 생성
rag.py	Qdrant 기반 RAG 구성 및 벡터스토어 연결
run_quiz.py	로컬 실행을 위한 엔트리포인트
graphstudio.json	LangGraph Studio용 설정 파일



⸻

🧭 흐름도 (Flow)

graph TD
  Start[__start__] -->|input| Dispatcher
  Dispatcher -->|quiz_feedback| QuizFeedback
  Dispatcher -->|summary_guide| SummaryGuide
  Dispatcher -->|personalized_intro| PersonalizedIntro
  QuizFeedback --> End
  SummaryGuide --> End
  PersonalizedIntro --> End



⸻

🚧 개발 상태
	•	✅ LangGraph 기반 흐름 구성
	•	✅ Qdrant 벡터스토어 연동 및 다중 컬렉션 지원
	•	✅ LangGraph Studio 시각화 및 실행 테스트 완료
	•	✅ 입력 기반 분기 처리 완비
	•	⏳ 고도화된 피드백 및 퀴즈 재도전 기능 개발 예정

⸻

📌 GitHub 업로드 시 참고
	•	루트에 README.md, graphstudio.json 포함
	•	.env 없이도 실행 가능하게 host.docker.internal 자동 분기 처리

⸻



