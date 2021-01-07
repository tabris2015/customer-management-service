from typing import List
from app.daos.account import AccountDAO
from app.models.account import Account, AccountCreate, AccountUpdate
from app.models.client import Client

account_dao = AccountDAO()


class AccountService:
    def create_account(self, account_create: AccountCreate) -> Account:
        return account_dao.create(account_create)

    def get_account(self, client: Client, id: str) -> Account:
        return account_dao.get(client.id, id)

    def list_accounts(self, client: Client) -> List[Account]:
        return account_dao.list(client.id)

    def update_account(self, client: Client, id: str, account_update: AccountUpdate) -> Account:
        return account_dao.update(client.id, id, account_update)

    def delete_account(self, client: Client, id: str) -> None:
        return account_dao.delete(client.id, id)