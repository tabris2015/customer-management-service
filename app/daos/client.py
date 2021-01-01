from typing import List
from app.database import db
from app.models.client import Client, ClientCreate, ClientUpdate


class ClientDAO:
    """DAO for Client model, this class implements the interface with firestore db"""
    collection_name = 'clients'

    def __init__(self):
        self.collection_ref = db.collection(self.collection_name)

    def create(self, client_create: ClientCreate) -> Client:
        data = client_create.dict()
        _, doc_ref = self.collection_ref.add(data)
        doc = doc_ref.get()
        if doc.exists:
            client = Client(id=doc.id, **doc.to_dict())
            return client

    def get(self, id: str) -> Client:
        doc_ref = self.collection_ref.document(id)
        doc = doc_ref.get()
        if doc.exists:
            return Client(id=doc.id, **doc.to_dict())

    def list(self) -> List[Client]:
        clients = []
        for doc in self.collection_ref.stream():
            client = Client(id=doc.id, **doc.to_dict())
            clients.append(client)
        return clients

    def update(self, id: str, client_update: ClientUpdate) -> Client:
        data = client_update.dict(exclude_none=True)
        print(data)
        doc_ref = self.collection_ref.document(id)
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: str) -> None:
        self.collection_ref.document(id).delete()
