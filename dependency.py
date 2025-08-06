from fastapi import Depends

from repository import TaskRepository, Cache_repository
from database import get_db_session
from cache import get_redis_connection
from service import TaskService


def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)

def get_cache_tasks_repository() -> Cache_repository:
    redis_connection = get_redis_connection()
    return Cache_repository(redis_connection)

def get_task_service(
        task_repository: TaskRepository = Depends(get_tasks_repository),
        task_cache: Cache_repository = Depends(get_cache_tasks_repository)
) -> TaskService:
    return TaskService(task_repository=task_repository, task_cache=task_cache)