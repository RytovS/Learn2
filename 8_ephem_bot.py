"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import ephem
import datetime
import logging
from os import set_inheritable
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL ,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME , 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print ('Вызван /start')
    update.message.reply_text('Здравствуй, человек Х')

def talk_to_me(update, context):
    text = update.message.text
    print (text)
    update.message.reply_text(text)


def screen_planet (user_text):
    planet_input = user_text.split()[1]
    day = datetime.date.today()
    print(day)
    print(planet_input)
    return planet_input

def planet_position(update, contex):  
    print(update.message.text)
    planet = screen_planet(update.message.text)
    
    planet_info = getattr(ephem, planet)
    planet_date = planet_info(datetime.date.today())
    planet_place = ephem.constellation(planet_date)
    update.message.reply_text(f'{planet} position - {planet_place}')
    


def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_position))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle
    
if __name__ == "__main__":
    main()