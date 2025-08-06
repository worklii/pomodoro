import json

from redis import Redis

from schema.task import TaskSchema


class Cache_repository:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_tasks(self) -> list[TaskSchema]:
        with self.redis as redis:
            task_json = redis.lrange('tasks', 0, -1)
            return [
                TaskSchema.model_validate(json.loads(task.decode('utf-8')))
                for task in task_json
            ]

    def set_tasks(self, tasks: list[TaskSchema]):
        task_json = [task.model_dump_json() for task in tasks]
        with self.redis as redis:
            self.redis.lpush('tasks', *task_json)