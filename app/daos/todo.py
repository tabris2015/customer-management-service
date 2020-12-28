from typing import List
from uuid import UUID

from app.database import db
from app.models.todo import Todo, TodoCreate, TodoUpdate


class TodoDAO:
    """DAO for Todo model, this class implements the interface with firestore db"""
    collection_name = 'todos'

    def create(self, todo_create: TodoCreate) -> Todo:
        data = todo_create.dict()
        data['id'] = str(data['id'])
        doc_ref = db.collection(self.collection_name).document(str(todo_create.id))
        doc_ref.set(data)
        return self.get(todo_create.id)

    def get(self, id: UUID) -> Todo:
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc = doc_ref.get()

        if doc.exists:
            return Todo(**doc.to_dict())

        return None

    def list(self) -> List[Todo]:
        todos_ref = db.collection(self.collection_name)
        return [Todo(**doc.get().to_dict()) for doc in todos_ref.list_documents() if doc.get().to_dict()]

    def update(self, id: UUID, todo_update: TodoUpdate) -> Todo:
        data = todo_update.dict()
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID) -> None:
        db.collection(self.collection_name).document(str(id)).delete()