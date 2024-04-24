from fastapi import APIRouter, Depends
from api.schemas.currency import Currency
from core.security import get_user_from_token
import requests
import json
from utils.external_api import get_currency_info, get_trading_info

cur = APIRouter()


@cur.get('/currency/exchange/')
async def currencynow(current_user: str = Depends(get_user_from_token)):
    '''
    За место апи было решено просто выгрузить json с веб страницы курсов ЦБ РФ, обновляющихся ежедневно
    '''

    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    currency_list = get_trading_info(response)
    json_data = json.loads(currency_list)
    
    return json_data

@cur.get('/currency/list/')
async def currency_info(current_user: str = Depends(get_user_from_token)):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    currency_list = get_currency_info(response)
    json_data = json.loads(currency_list)
    
    return json_data



