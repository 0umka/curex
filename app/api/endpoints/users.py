from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from api.schemas.user import User
from core.security import create_jwt_token


user = APIRouter()
users_data = {}

async def get_user(username: str):
    if username in users_data:
        user_data = users_data[username]
        return User(**user_data)
    return None


@user.post('/auth/register/')
async def register(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    users_data[user_data.username] = {'login': user_data.username, 'password': user_data.password}


@user.post('/auth/login/')
async def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_data_from_db = get_user(user_data.username)
    if user_data_from_db is None or user_data.password != user_data_from_db.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    return {"access_token": create_jwt_token({"sub": user_data.username})}