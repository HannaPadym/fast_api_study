from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from routers import task_router
from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='127.0.0.1',
                port=80)
