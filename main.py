from fastapi import FastAPI
from app.api.endpoints import currency, users

app = FastAPI()

app.include_router(currency.cur)
app.include_router(users.user)