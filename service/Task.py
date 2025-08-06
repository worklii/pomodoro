from dataclasses import dataclass
from repository import TaskRepository, Cache_repository
from schema.task import TaskSchema

@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: Cache_repository

    def get_tasks(self) -> list[TaskSchema]:
        if tasks := self.task_cache.get_tasks():
            return tasks
        else:
            tasks = self.task_repository.get_tasks()
            tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
            self.task_cache.set_tasks(tasks_schema)
            return tasks
