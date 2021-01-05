from typing import List
from app.daos.account import AccountDAO
from app.models.account import Account, AccountCreate, AccountUpdate

account_dao = AccountDAO()


class AccountService:
    def create_account(self, account_create: AccountCreate) -> Account:
        return account_dao.create(account_create)

    def get_account(self, client_id: str, id: str) -> Account:
        return account_dao.get(client_id, id)

    def list_accounts(self, client_id: str) -> List[Account]:
        return account_dao.list(client_id)

    def update_account(self, client_id: str, id: str, account_update: AccountUpdate) -> Account:
        return account_dao.update(client_id, id, account_update)

    def delete_account(self, client_id: str, id: str) -> None:
        return account_dao.delete(client_id, id)