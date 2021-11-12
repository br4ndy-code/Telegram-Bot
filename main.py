import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Settings')
    btn2 = types.KeyboardButton('Help')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Welcome!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        if message.text == 'Settings':
            bot.send_message(message.chat.id, 'There will be settings!')
        elif message.text == 'Help':
            bot.send_message(message.chat.id, 'This bot was developed just for fun by br4ndy-code!')
        else:
            bot.send.message(message.chat.id, 'Sorry, I didn\'t understand you :(')


bot.polling(none_stop=True)
