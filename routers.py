from typing import Annotated
from schemas import STaskAdd, STask, STaskId
from fastapi import APIRouter, Depends
from repository import TaskRepository

task_router = APIRouter(prefix='/tasks', tags=['tasks', ])


@task_router.get('/')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {'tasks': tasks}


@task_router.post('/')
async def create_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {'response': 'ok', 'task_id': task_id}
