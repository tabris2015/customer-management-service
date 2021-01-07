from datetime import datetime
from fastapi import APIRouter, Body, HTTPException
from fastapi import status
from typing import List
from uuid import uuid4
from app.models.transaction import Transaction, TransactionCreate, TransactionUpdate, TransactionIn
from app.services.transaction import TransactionService


router = APIRouter()
transaction_service = TransactionService()


@router.post('/transactions/', response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction_create: TransactionIn = Body(...)):
    """Create a Transaction task"""
    return transaction_service.create_transaction(TransactionCreate(**transaction_create.dict()))


@router.get('/transactions/', response_model=List[Transaction])
async def get_transactions():
    """Get all Transaction tasks"""
    transactions = transaction_service.list_transactions()
    if not transactions:
        raise HTTPException(status_code=404, detail='transactions not found')
    return transactions


@router.get('/transactions/{id}', response_model=Transaction)
async def get_transaction(id: str):
    """Get a particular Transaction by id"""
    transaction = transaction_service.get_transaction(id)
    if not transaction:
        raise HTTPException(status_code=404, detail='Transaction not found')
    return transaction


@router.put('/transactions/{id}', response_model=Transaction)
async def update_transaction(id: str, transaction_update: TransactionUpdate = Body(...)):
    """Update a Transaction task"""
    transaction = transaction_service.get_transaction(id)
    if not transaction:
        raise HTTPException(status_code=404, detail='Transaction not found')
    return transaction_service.update_transaction(id, transaction_update)


@router.delete('/transactions/{id}', response_model=Transaction)
async def delete_transaction(id: str):
    """Delete a transaction task"""
    transaction = transaction_service.get_transaction(id)
    if not transaction:
        raise HTTPException(status_code=404, detail='transaction not found')
    return transaction_service.delete_transaction(id)
