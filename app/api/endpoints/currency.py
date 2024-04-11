from fastapi import APIRouter, Depends
from api.schemas.currency import Currency
from core.security import get_user_from_token

cur = APIRouter()


@cur.get('/currency/exchange/')
async def currencynow(current_user: str = Depends(get_user_from_token)):
    #some api prikoli
    pass

@cur.get('/currency/list/')
async def cur_currency(curren_user: str = Depends(get_user_from_token)):
    #some currency info
    pass


