from pydantic import BaseModel
from typing import Literal

class UserInput(BaseModel):
    profile: str
    question: str

class DispatcherOutput(BaseModel):
    task_type: Literal["summary_guide", "personalized_intro", "quiz_feedback"]
    input_data: UserInput
