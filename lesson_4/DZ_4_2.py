# Задание 4.2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению
# к рублю. Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве
# примера выведите курсы доллара и евро.

import requests

def currency_rates(cur):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if cur not in response:
        return None
    currency = response[response.find('<Value>', response.find(cur)) + 7:response.find('</Value>', response.find(cur))]
    return float(f"{currency.replace(',', '.')}")
print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('QWE'))



# def currency_rates_kz(cur):
#     response = requests.get('https://www.nationalbank.kz/rss/rates_all.xml').text
#     if cur not in response:
#         return None
#     currency = response[response.find('<description>', response.find(cur)) + 13:response.find('</description>', response.find(cur))]
#     return (f"{cur} to KZT - {float(currency)}")
# print(currency_rates_kz('USD'))
# print(currency_rates_kz('EUR'))
# print(currency_rates_kz('QWE'))


