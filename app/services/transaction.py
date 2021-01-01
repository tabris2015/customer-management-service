from typing import List
from app.daos.transaction import TransactionDAO
from app.models.transaction import Transaction, TransactionCreate, TransactionUpdate

transaction_dao = TransactionDAO()


class TransactionService:
    def create_transaction(self, transaction_create: TransactionCreate) -> Transaction:
        return transaction_dao.create(transaction_create)

    def get_transaction(self, id: str) -> Transaction:
        return transaction_dao.get(id)

    def get_transactions_by_account(self, account_id: str) -> List[Transaction]:
        return transaction_dao.get_by_account_id(account_id)

    def list_transactions(self) -> List[Transaction]:
        return transaction_dao.list()

    def update_transaction(self, id: str, transaction_update: TransactionUpdate) -> Transaction:
        return transaction_dao.update(id, transaction_update)

    def delete_transaction(self, id: str) -> None:
        return transaction_dao.delete(id)