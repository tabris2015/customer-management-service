from typing import List
from uuid import UUID

from app.database import db
from app.models.transaction import Transaction, TransactionCreate, TransactionUpdate


class TransactionDAO:
    """DAO for Transaction model, this class implements the interface with firestore db"""
    collection_name = 'transactions'

    def __init__(self, parent=None):
        self.collection_ref = db.collection(self.collection_name)

    def create(self, transaction_create: TransactionCreate) -> Transaction:
        data = transaction_create.dict()
        data['id'] = str(data['id'])
        doc_ref = self.collection_ref.document(str(transaction_create.id))
        doc_ref.set(data)
        return self.get(transaction_create.id)

    def get(self, id: UUID) -> Transaction:
        doc_ref = self.collection_ref.document(str(id))
        doc = doc_ref.get()

        if doc.exists:
            return Transaction(**doc.to_dict())

        return None

    def get_by_account_id(self, account_id: str, parent: str = None) -> List[Transaction]:
        coll_ref = self.collection_ref
        if parent:
            coll_ref = db.collection(parent + '/' + self.collection_name)

        transactions = coll_ref.where('account_id', '==', account_id).stream()
        return [Transaction(**doc.to_dict()) for doc in transactions if doc.to_dict()]

    def list(self) -> List[Transaction]:
        todos_ref = self.collection_ref
        return [Transaction(**doc.get().to_dict()) for doc in todos_ref.list_documents() if doc.get().to_dict()]

    def update(self, id: UUID, transaction_update: TransactionUpdate) -> Transaction:
        data = transaction_update.dict()
        doc_ref = self.collection_ref.document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID) -> None:
        self.collection_ref.document(str(id)).delete()