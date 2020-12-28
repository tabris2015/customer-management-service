from typing import List
from app.daos.todo import TodoDAO
from app.models.todo import Todo, TodoCreate, TodoUpdate

todo_dao = TodoDAO()


class TodoService:
    def create_todo(self, todo_create: TodoCreate) -> Todo:
        return todo_dao.create(todo_create)

    def get_todo(self, id: str) -> Todo:
        return todo_dao.get(id)

    def list_todos(self) -> List[Todo]:
        return todo_dao.list()

    def update_todo(self, id: str, todo_update: TodoUpdate) -> Todo:
        return todo_dao.update(id, todo_update)

    def delete_todo(self, id: str) -> None:
        return todo_dao.delete(id)