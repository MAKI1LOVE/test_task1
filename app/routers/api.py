from datetime import datetime

from aiohttp import ClientSession
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud.questions import get_last_question, insert_questions
from db.session import get_session
from schemas.question import QuestionRequest, QuestionCreate
from util import get_http_session

api_router = APIRouter(tags=['/api'])
url = 'https://jservice.io/api/random?count='


@api_router.post('/question')
async def add_n_questions(q_req: QuestionRequest, session=Depends(get_session)):
    n = q_req.questions_num
    result = await get_last_question(session)
    output = result.scalar_one_or_none()
    await save_questions(session, n)

    return output


async def save_questions(session: AsyncSession, n: int):
    http_session: ClientSession = get_http_session()
    while n > 0:
        async with http_session.get(url + str(n)) as response:
            data = await response.json()

        res = await insert_questions(
            session,
            [data_to_question(q) for q in data]
        )
        n -= len(res.all())


def data_to_question(data: dict) -> QuestionCreate:
    return QuestionCreate(
        question_id=int(data['id']),
        question=data['question'],
        answer=data['answer'],
        # for python < 3.11 'data['created_at'][:-1]' :)
        creation_date=datetime.fromisoformat(data['created_at'][:-1])
    )
