from fastapi import APIRouter, Body, HTTPException
from fastapi import status
from typing import List
from app.models.account import Account, AccountCreate, AccountUpdate, AccountIn
from app.services.account import AccountService


router = APIRouter()
account_service = AccountService()


@router.post('/', response_model=Account, status_code=status.HTTP_201_CREATED)
async def create_account(account_create: AccountIn = Body(...)):
    """Create a Account task"""
    return account_service.create_account(AccountCreate(**account_create.dict()))


@router.get('/', response_model=List[Account])
async def get_accounts(client_id: str):
    """Get all Account tasks"""
    accounts = account_service.list_accounts(client_id)
    if not accounts:
        raise HTTPException(status_code=404, detail='accounts not found')
    return accounts


@router.get('/{id}', response_model=Account)
async def get_account(id: str, client_id: str):
    """Get a particular Account by id"""
    account = account_service.get_account(client_id, id)
    if not account:
        raise HTTPException(status_code=404, detail='Account not found')
    return account


@router.put('/{id}', response_model=Account)
async def update_account(id: str, client_id: str, account_update: AccountUpdate = Body(...)):
    """Update a Account task"""
    account = account_service.get_account(client_id, id)
    if not account:
        raise HTTPException(status_code=404, detail='Account not found')
    return account_service.update_account(client_id, id, account_update)


@router.delete('/{id}', response_model=Account)
async def delete_account(id: str, client_id: str):
    """Delete a account task"""
    account = account_service.get_account(client_id, id)
    if not account:
        raise HTTPException(status_code=404, detail='account not found')
    return account_service.delete_account(client_id, id)
