from ..api.schemas.currency import Currency

def get_currency_info(response):
    '''
    вместо апи будет просто json с курсами ЦБ РФ
    '''
    currency_list = dict()
    for currency in response['Valute']:
        currency_list[currency] = {'code': currency, 'name': currency['name']}
    return currency_list

def get_trading_info(response) -> Currency:
    currency_list = dict()
    for currency in response['Valute']:
        currency_list[currency] = {'name': currency['name'], 'value': currency['value'] }
    return currency_list