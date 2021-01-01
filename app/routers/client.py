from fastapi import APIRouter, Body, HTTPException
from fastapi import status
from typing import List
from app.models.client import Client, ClientCreate, ClientUpdate, ClientIn
from app.services.client import ClientService


router = APIRouter()
client_service = ClientService()


@router.post('/', response_model=Client, status_code=status.HTTP_201_CREATED)
async def create_client(client_create: ClientIn = Body(...)):
    """Create a Client task"""
    print(client_create)
    return client_service.create_client(ClientCreate(**client_create.dict()))


@router.get('/', response_model=List[Client])
async def get_clients():
    """Get all Client tasks"""
    clients = client_service.list_clients()
    if not clients:
        raise HTTPException(status_code=404, detail='clients not found')
    return clients


@router.get('/{id}', response_model=Client)
async def get_client(id: str):
    """Get a particular Client by id"""
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='Client not found')
    return client


@router.put('/{id}', response_model=Client)
async def update_client(id: str, client_update: ClientUpdate = Body(...)):
    """Update a Client task"""
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='Client not found')
    return client_service.update_client(id, client_update)


@router.delete('/{id}', response_model=Client)
async def delete_client(id: str):
    """Delete a client task"""
    client = client_service.get_client(id)
    if not client:
        raise HTTPException(status_code=404, detail='client not found')
    return client_service.delete_client(id)
