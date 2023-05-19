from sqlalchemy import select, Result, IteratorResult
from sqlalchemy.dialects.postgresql import insert as p_insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.question import Questions
from schemas.question import QuestionCreate


async def insert_questions(session: AsyncSession, questions: [QuestionCreate]) -> IteratorResult:
    stmt = p_insert(Questions).values([dict(q) for q in questions]).on_conflict_do_nothing().returning(Questions.id)
    return await session.execute(stmt)


async def get_last_question(session: AsyncSession) -> Result:
    stmt = select(Questions).order_by(Questions.id.desc()).limit(1)
    return await session.execute(stmt)


async def get_question_by_question_id(session: AsyncSession, question_id: int) -> Result:
    stmt = select(Questions).where(Questions.question_id == question_id)
    return await session.execute(stmt)
