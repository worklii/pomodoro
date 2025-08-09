from typing import Annotated
from dependency import get_tasks_repository, get_task_service, get_request_user_id
from fastapi import APIRouter, status, Depends, HTTPException

from exception import UserNotFoundException, TaskNotFound
from schema import TaskSchema, TaskCreateSchema
from repository import TaskRepository, Cache_repository
from service import TaskService

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/all", response_model=list[TaskSchema])
async def get_task(task_service: Annotated[TaskService, Depends(get_task_service)]):
    return task_service.get_tasks()

@router.post("/", response_model=TaskSchema)
async def create_task(
body: TaskCreateSchema,
task_service: Annotated[TaskService, Depends(get_task_service)],
user_id = Depends(get_request_user_id)):
    task = task_service.create_task(body, user_id)
    return task

@router.patch("/{task_id}", response_model=TaskSchema)
async def update_task(
task_id: int,
name: str,
task_service: Annotated[TaskService, Depends(get_task_service)],
user_id = Depends(get_request_user_id)):
    try:
        return task_service.update_task_name(task_id=task_id, name=name, user_id=user_id)
    except TaskNotFound as e:
        raise HTTPException(status_code=404, detail=e.detail)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int,
    task_service: Annotated[TaskService, Depends(get_task_service)],
    user_id: int = Depends(get_request_user_id)):
    try:
        task_service.delete_task(task_id=task_id, user_id=user_id)
    except TaskNotFound as e:
        raise HTTPException(status_code=404, detail=e.detail)
