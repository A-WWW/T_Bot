import random
import telebot

bot = telebot.TeleBot('2096753098:AAHXLw3HYe_saVzuHPmLqZxq6UORn7xcTBs')
from telebot import types

first = ["Тебе сегодня и сам чёрт не брат", "Сапер ошибается только раз",
         "Будь осторожен, когда видишь врага и очень осторожен, когда его не видишь.",
         "Неплохой день, но будь внимателен"]
second = ["Тебе сегодня и сам чёрт не брат", "Сапер ошибается только раз",
          "Будь осторожен, когда видишь врага и очень осторожен, когда его не видишь.",
          "Неплохой день, но будь внимателен"]
third = ["Тебе сегодня и сам чёрт не брат", "Сапер ошибается только раз",
         "Будь осторожен, когда видишь врага и очень осторожен, когда его не видишь.",
         "Неплохой день, но будь внимателен"]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Для счастья нужен еще и случай. Аристотель.")
        keyboard = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Первый бросок удачи', callback_data='chance')
        keyboard.add(key_first)
        key_second = types.InlineKeyboardButton(text='Второй бросок удачи', callback_data='chance')
        keyboard.add(key_second)
        key_third = types.InlineKeyboardButton(text='Третий бросок удачи', callback_data='chance')
        keyboard.add(key_third)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text= 'Статистика и случай определят момент, но иногда они на вашей стороне, Бот выдает предсказания на основе генератора случайных чисел, очень хороших 25%, просто хороших 25%, осторожных 25%, очень внимательных 25%, три попытки как вариант предскажут твою карму на сегодня или на сейчас', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "chance":
        msg = random.choice(first)
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
