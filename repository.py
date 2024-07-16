from sqlalchemy import select

from database import session, TaskOrm
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with session() as new_session:
            task = TaskOrm(**data.model_dump())
            new_session.add(task)
            await new_session.flush()
            await new_session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with session() as new_session:
            query = select(TaskOrm)
            result = await new_session.execute(query)
            tasks = result.scalars().all()
            tasks_schemas = [STask.model_validate(task) for task in tasks]
            return tasks_schemas
