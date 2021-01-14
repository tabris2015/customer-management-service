from typing import List
from app.database import db
from app.models.user import User, UserCreate, UserUpdate


class UserDAO:
    """DAO for User model, this class implements the interface with firestore db"""
    collection_name = 'users'

    def __init__(self):
        self.collection_ref = db.collection(self.collection_name)

    def create(self, user_create: UserCreate) -> User:
        data = user_create.dict(exclude={'id'})
        doc_ref = self.collection_ref.document(user_create.id)
        doc_ref.set(data)
        doc = doc_ref.get()
        if doc.exists:
            user = User(id=doc.id, **doc.to_dict())
            return user

    def get(self, id: str) -> User:
        doc_ref = self.collection_ref.document(id)
        doc = doc_ref.get()
        if doc.exists:
            return User(id=doc.id, **doc.to_dict())

    def list(self) -> List[User]:
        users = []
        for doc in self.collection_ref.stream():
            user = User(id=doc.id, **doc.to_dict())
            users.append(user)
        return users

    def update(self, id: str, user_update: UserUpdate) -> User:
        data = user_update.dict(exclude_none=True)
        doc_ref = self.collection_ref.document(id)
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: str) -> None:
        self.collection_ref.document(id).delete()
