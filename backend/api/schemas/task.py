from pydantic import BaseModel


class TaskBase(BaseModel):
    task_id: str
    title: str
    domain: str
    week_number: int
    difficulty: str


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    class Config:
        from_attributes = True