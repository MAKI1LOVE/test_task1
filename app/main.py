import uvicorn
from fastapi import FastAPI

from db.session import init_db, close_db_connection
from routers.api import api_router
from util import init_http_session, http_session_close

app = FastAPI(title='Task1', version='1.0.0')
app.include_router(api_router, prefix='/api')


@app.on_event('startup')
async def startup():
    await init_db()
    await init_http_session()


@app.on_event('shutdown')
async def shutdown():
    await close_db_connection()
    await http_session_close()


if __name__ == '__main__':
    uvicorn.run(app, port=8080)
