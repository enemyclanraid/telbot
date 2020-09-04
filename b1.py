#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot('830513665:AAHyoUAo4LTUeUOR9iciTfLJ-aZpbxebv9I')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Приветттт')
    elif message.text.lower() == 'bb':
        bot.send_message(message.chat.id, 'Пока, ЛОЛ:)')

bot.polling()