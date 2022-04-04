import requests

def currency_rates(cur):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if cur not in response:
        return None
    currency = response[response.find('<Value>', response.find(cur)) + 7:response.find('</Value>', response.find(cur))]
    return float(f"{currency.replace(',', '.')}")
