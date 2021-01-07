from typing import List
from app.daos.client import ClientDAO
from app.models.client import Client, ClientCreate, ClientUpdate
from app.models.account import Account, AccountCreate, AccountUpdate
from app.services.account import AccountService
from app.daos.account import AccountDAO

client_dao = ClientDAO()
account_dao = AccountDAO()
account_service = AccountService()


class ClientService:
    def create_client(self, client_create: ClientCreate) -> Client:
        return client_dao.create(client_create)

    def get_client(self, id: str) -> Client:
        return client_dao.get(id)

    def list_clients(self) -> List[Client]:
        return client_dao.list()

    def update_client(self, id: str, client_update: ClientUpdate) -> Client:
        return client_dao.update(id, client_update)

    def delete_client(self, id: str) -> None:
        return client_dao.delete(id)

    def list_accounts(self, id: str) -> List[Account]:
        client = self.get_client(id)
        return client.accounts

    def get_account(self, id: str, account_id: str):
        client = self.get_client(id)
        for account in client.accounts:
            if account.id == account_id:
                return account

    def create_account(self, account_create: AccountCreate):
        return account_service.create_account(account_create)

    def update_account(self, account_update: AccountUpdate):
        return account_dao.update(account_update.client_id, account_update.id, account_update)
