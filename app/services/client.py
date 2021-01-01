from typing import List
from app.daos.client import ClientDAO
from app.models.client import Client, ClientCreate, ClientUpdate

client_dao = ClientDAO()


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