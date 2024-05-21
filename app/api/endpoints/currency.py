from fastapi import APIRouter, Depends
from app.api.schemas.currency import Currency
from app.core.security  import get_user_from_token
from app.utils.external_api import get_currency_info, get_trading_info
import httpx
import json

cur = APIRouter()

@cur.get('/currency/exchange/')
async def currencynow(current_user: str = Depends(get_user_from_token)):
    '''
    За место апи было решено просто выгрузить json с веб страницы курсов ЦБ РФ, обновляющихся ежедневно
    '''

    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    currency_list = response.json()
    return currency_list

@cur.get('/currency/list/')
async def currency_info(current_user: str = Depends(get_user_from_token)):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    currency_list = response.json()
    return currency_list


