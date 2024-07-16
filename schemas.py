from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: str | None = None

    def __str__(self):
        return f'{self.name} {self.description}'


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
