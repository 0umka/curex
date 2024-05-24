from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from app.api.schemas.user import User
from app.core.security import create_jwt_token
from fastapi.responses import HTMLResponse


user = APIRouter()
users_data = {
    '1': {'login': '1', 'password': '1'}
}
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_user(username: str):
    global users_data
    if username in users_data:
        user_data = users_data[username]
        return User(**user_data)
    return None

@user.get("/auth/register/")
def register_form():
    html = """
    <html>
        <body>
            <h1>Register</h1>
            <form action="/auth/register/" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br>
                <input type="submit" value="Register">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html, media_type="text/html")

@user.get("/auth/login/")
def login_form():
    html = """
    <html>
        <body>
            <h1>Login</h1>
            <form action="/auth/login/" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html, media_type="text/html")

@user.post('/auth/register/')
async def register(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    users_data[user_data.username] = {'login': user_data.username, 'password': user_data.password}
    return {"message": "User registered successfully", 'data': users_data}

@user.post('/auth/login/')
async def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await get_user(user_data.username)
    if user and user.password == user_data.password:
         access_token = await create_jwt_token({"sub": user_data.username})
         return {"access_token": access_token, "token_type": "bearer"}
    return {"error": "Неверные учетные данные"}