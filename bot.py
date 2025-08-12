import telebot
from dotenv import load_dotenv
import os
import re
from compare import compare


load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def command_start_handler(message) -> None:
    bot.send_message(message.chat.id,
                     'Belarusian Consultant поможет белорусский абитуриентам выбрать ВУЗ мечты, взвесив все за и против.\n'
                     '/start - запустить бота\n'
                     '/compare "ВУЗ" "ВУЗ" - сравнить 2 ВУЗа (Введите полное официальное название)')


@bot.message_handler(commands=['compare']) 
def command_compare_handler(message) -> None:
    matches = re.findall(r'"([^"]+)"', message.text)

    if len(matches) != 2:
        bot.send_message(message.chat.id,
                         'Пожалуйста, введите два вуза в формате:\n/compare "Первый ВУЗ" "Второй ВУЗ"')
        return None
    
    answer = compare(matches)

    bot.send_message(message.chat.id, answer)


bot.infinity_polling()