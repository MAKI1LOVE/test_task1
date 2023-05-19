from sqlalchemy import Column, Integer, String, DateTime

from db.base import Base


class Questions(Base):
    question_id = Column(Integer, index=True, unique=True)
    question = Column(String)
    answer = Column(String)
    creation_date = Column(DateTime)
