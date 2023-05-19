from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class QuestionBase(BaseModel):
    question_id: int
    question: str
    answer: str
    creation_date: datetime

    class Config:
        orm_mode = True


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: Optional[int]


class QuestionRequest(BaseModel):
    questions_num: int = Field(default=0, le=100, ge=0)
