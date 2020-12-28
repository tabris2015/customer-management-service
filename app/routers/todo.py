from datetime import datetime
from fastapi import APIRouter, Body, HTTPException
from fastapi import status
from typing import List
from uuid import uuid4
from app.models.todo import Todo, TodoCreate, TodoUpdate, TodoIn
from app.services.todo import TodoService


router = APIRouter()
todo_service = TodoService()


@router.post('/', response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo_create: TodoIn = Body(...)):
    """Create a Todo task"""
    return todo_service.create_todo(TodoCreate(**todo_create.dict()))


@router.get('/', response_model=List[Todo])
async def get_todos():
    """Get all Todo tasks"""
    todos = todo_service.list_todos()
    if not todos:
        raise HTTPException(status_code=404, detail='todos not found')
    return todos


@router.get('/{id}', response_model=Todo)
async def get_todo(id: str):
    """Get a particular Todo by id"""
    todo = todo_service.get_todo(id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo


@router.put('/{id}', response_model=Todo)
async def update_todo(id: str, todo_update: TodoUpdate = Body(...)):
    """Update a Todo task"""
    todo = todo_service.get_todo(id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo_service.update_todo(id, todo_update)


@router.delete('/{id}', response_model=Todo)
async def delete_todo(id: str):
    """Delete a todo task"""
    todo = todo_service.get_todo(id)
    if not todo:
        raise HTTPException(status_code=404, detail='todo not found')
    return todo_service.delete_todo(id)
