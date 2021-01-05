from typing import List
from google.cloud import firestore
from app.database import db
from app.models.account import Account, AccountCreate, AccountUpdate


class AccountDAO:
    """DAO for Account model, this class implements the interface with firestore db"""
    array_name = 'accounts'
    clients_collection = 'clients'

    def get_client_ref(self, client_id: str):
        return db.collection(self.clients_collection).document(client_id)

    def create(self, account_create: AccountCreate) -> Account:
        data = account_create.dict()
        # create document inside client document
        client_ref = self.get_client_ref(data['client_id'])
        client_ref.update({self.array_name: firestore.ArrayUnion([data])})
        # the object will be the last one created
        account = client_ref.get().to_dict()['accounts'][-1]

        if account['id'] == data['id']:
            return Account(**account)

    def get(self, client_id: str, id: str) -> Account:
        client_ref = self.get_client_ref(client_id)
        accounts = client_ref.get().to_dict()['accounts']
        # search in array of accounts
        for account in accounts:
            if account['id'] == id:
                return Account(**account)

    def list(self, client_id: str) -> List[Account]:
        client_ref = self.get_client_ref(client_id)
        accounts = client_ref.get().to_dict()['accounts']
        return [Account(**account) for account in accounts]

    def update(self, client_id: str, id: str, account_update: AccountUpdate) -> Account:
        data = account_update.dict(exclude_none=True)
        client_ref = self.get_client_ref(client_id)
        accounts = client_ref.get().to_dict()['accounts']
        account_idx = -1
        for idx, account in enumerate(accounts):
            if account['id'] == id:
                account_idx = idx

        if account_idx != -1:
            for key in data:
                accounts[account_idx][key] = data[key]

        client_ref.update({self.array_name: accounts})

        return self.get(client_id, id)

    def delete(self, client_id: str, id: str) -> None:
        client_ref = self.get_client_ref(client_id)
        accounts = client_ref.get().to_dict()['accounts']
        account_idx = -1
        for idx, account in enumerate(accounts):
            if account['id'] == id:
                account_idx = idx

        if account_idx != -1:
            accounts.pop(account_idx)

        client_ref.update({self.array_name: accounts})

