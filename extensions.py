## Вспомоательный файл файла app.py
# Фай содержит классы коверторва и исключений.
# Экспортируем необходимые библиотеки и данные файлов, которые требуются для работы.
import json
import requests
from config import keys
from config import app_id

# Конвертируем с усетом правильности запроса.
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = quote
            #quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')
        try:
            base_ticker = base
            #base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        # Держатель контента не дает данные по конвертации бесплатно.
        # Считаю сам, сохраняя формат задания.
        l = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={app_id}&symbols={quote_ticker}")
        r = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={app_id}&symbols={base_ticker}")

        cont_l = json.loads(l.content)['rates'][quote_ticker]
        cont_r = json.loads(r.content)['rates'][base_ticker]

        if int(cont_l) == 0:
            raise APIException(f'Нет данных по валюте - {quote_ticker}.')
            total_base = 0
        else:
            total_base = amount * int(cont_r) / int(cont_l)

        return total_base

# Исключения.
class APIException(Exception):
    pass