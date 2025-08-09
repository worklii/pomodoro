from sqlalchemy.orm import Session

from schema import TaskCreateSchema
from schema.task import TaskSchema
from models import Tasks
from sqlalchemy import select, delete, update

class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_tasks(self):
        with self.session() as session:
            task: list[Tasks] = session.execute(select(Tasks)).scalars().all()
        return task

    def get_task(self, task_id: int) -> Tasks | None:
        with self.session() as session:
            task = session.execute(
                select(Tasks).where(Tasks.id == task_id)
            ).scalar_one_or_none()
        return task

    def get_user_task(self, task_id: int, user_id: int) -> Tasks | None:
        query = select(Tasks).where(Tasks.id == task_id, Tasks.user_id == user_id)
        with self.session() as session:
            task: Tasks = session.execute(query).scalar_one_or_none()
        return task

    def create_task(self, task: TaskCreateSchema, user_id: int) -> int:
        with self.session() as session:
            task_model: Tasks = Tasks(name=task.name, pomodoro_count=task.pomodoro_count, category_id=task.category_id, user_id=user_id)
            session.add(task_model)
            session.commit()
            return task_model.id

    def delete_task(self, task_id: int, user_id: int) -> None:
        with self.session() as session:
            session.execute(delete(Tasks).where(Tasks.id == task_id, Tasks.user_id == user_id))
            session.commit()

    def update_task_name(self, task_id: int, name: str):
        query = update(Tasks).where(Tasks.id == task_id).values(name=name).returning(Tasks.id)
        with self.session() as session:
            task_id : int = session.execute(query).scalar_one_or_none()
            session.commit()  # вот здесь важный вызов!
            session.flush()
            return self.get_task(task_id)




