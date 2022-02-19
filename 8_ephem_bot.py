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
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, bot):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def screen_planet (update, bot):
    planet_input = str(update.message.text.split()[1]).lower().capitalize()
    day = date.today().split("-")
    print(day)
    print(planet_input)
    update.message.reply_text(planet_input)


def talk_to_me(update, bot):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def main():
    mybot = Updater("5204868119:AAFGSwZG7VTEqPJr1bFjf8H-z1mQ_6oYo2o
", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", screen_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

