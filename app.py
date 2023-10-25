## Это Бот "Magic" он умеет конвертировать не большой, но актуальный,
# на мой взгляд, список валют.
# Экспортируем необходимые библиотеки и данные файлов, которые требуются для работы бота.
import telebot
from config import keys, TOKEN
from extensions import APIException, CryptoConverter

# Активируем бота.
bot = telebot.TeleBot(TOKEN)

# Обрабатываются сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работату введи команду боту в следующем формате:\n <имя валюты>'
            '  <в какую валюту перевести>   <количество переводимой валюты> '
            '\n Пример: USD RUB 2 \n Показать список всех доступных валют: /values')
    bot.reply_to(message, text)

# Обрабатывается команда '/values'.
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:' # Список приотовил в ручную на основании бесплатноо запроса API.
    for key,value in keys.items(): # Список в файле config.py
        valuta = key+"-"+value
        text ="\n".join((text, valuta))
    bot.reply_to(message, text)

# Обрабатывается запрос по конвертации валют.
@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise APIException('Недопустимое количество параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка.\n{e}')
    else:
        text = f'Цена {amount} {keys[quote]} в {keys[base]} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
