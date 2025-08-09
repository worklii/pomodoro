from pydantic import BaseModel, Field, model_validator
from typing import Optional


class TaskSchema(BaseModel):
    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int
    user_id: int

    class Config:
        from_attributes = True

    @model_validator(mode='after')
    def check_name_or_pomodoro_count_is_not_none(self):
        if self.pomodoro_count is None and self.name is None:
            raise ValueError('pomodoro_count or name are required')
        return self

class TaskCreateSchema(BaseModel):
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int