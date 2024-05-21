from fastapi import FastAPI
from app.api.endpoints import currency, users
import uvicorn

app = FastAPI()

app.include_router(currency.cur)
app.include_router(users.user)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)