from fastapi import APIRouter, Body, HTTPException
from fastapi import status
from app.models.user import User, UserLogin, UserIn, UserUpdateIn
from app.services.authentication import AuthenticationService


router = APIRouter()
authentication_service = AuthenticationService()


@router.post('/auth/login')
def login(user_login: UserLogin = Body(...)):
    return authentication_service.authenticate_user(user_login)


@router.post('/auth/register', response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserIn = Body(...)):
    """Register a User"""
    return authentication_service.register_user(user_in)


@router.put('/auth/update', response_model=User)
async def update_user(user_update: UserUpdateIn = Body(...)):
    """Update a Todo task"""
    try:
        user = authentication_service.update_user(user_update)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail='Value Error')


@router.delete('/auth/{id}')
async def delete_user(id: str):
    """Delete a user"""
    return authentication_service.delete_user(id)
