from fastapi import APIRouter, Body, HTTPException
from fastapi import status
from typing import List
from app.models.client import Client, ClientCreate, ClientUpdate, ClientIn
from app.models.account import Account, AccountIn, AccountCreate, AccountUpdate
from app.services.client import ClientService
from app.services.account import AccountService


router = APIRouter()
client_service = ClientService()
account_service = AccountService()


@router.post('/clients/', response_model=Client, status_code=status.HTTP_201_CREATED)
async def create_client(client_data: ClientIn = Body(...)):
    """Create a Client task"""
    return client_service.create_client(ClientCreate(**client_data.dict()))


@router.get('/clients/', response_model=List[Client])
async def get_clients():
    """Get all Client tasks"""
    clients = client_service.list_clients()
    if not clients:
        raise HTTPException(status_code=404, detail='clients not found')
    return clients


@router.get('/clients/{id}', response_model=Client)
async def get_client(id: str):
    """Get a particular Client by id"""
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='Client not found')
    return client


@router.put('/clients/{id}', response_model=Client)
async def update_client(id: str, client_update: ClientUpdate = Body(...)):
    """Update a Client task"""
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='Client not found')
    return client_service.update_client(id, client_update)


@router.delete('/clients/{id}', response_model=Client)
async def delete_client(id: str):
    """Delete a client task"""
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='client not found')
    return client_service.delete_client(id)


@router.post('/clients/{id}/accounts', response_model=Account, status_code=status.HTTP_201_CREATED)
async def create_client_account(account_data: AccountIn):
    client = client_service.get_client(account_data.client_id)
    if not client:
        raise HTTPException(status_code=404, detail='client not found')
    return account_service.create_account(AccountCreate(**account_data.dict()))


@router.get('/clients/{id}/accounts', response_model=List[Account])
async def get_client_accounts(id: str):
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='client not found')
    accounts = account_service.list_accounts(client)
    if not accounts:
        raise HTTPException(status_code=404, detail='accounts not found for this client')
    return accounts


@router.get('/clients/{id}/accounts/{account_id}', response_model=Account)
async def get_client_account(id: str, account_id: str):
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='client not found')
    account = account_service.get_account(client, account_id)
    if not account:
        raise HTTPException(status_code=404, detail='account not found')
    return account


@router.put('/clients/{id}/accounts/{account_id}', response_model=Account)
async def update_client_account(id: str, account_id: str, account_update: AccountUpdate = Body(...)):
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='Client not found')
    account = account_service.get_account(client, account_id)
    if not account:
        raise HTTPException(status_code=404, detail='Account not found')
    return account_service.update_account(client, account_id, account_update)