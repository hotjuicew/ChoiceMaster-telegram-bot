#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import random

import telebot

from data import data, activities, replies


class ChoiceBot:
    def __init__(self, api_token):
        self.bot = telebot.TeleBot(api_token)
        self.bot.delete_webhook()

        @self.bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            self.bot.reply_to(message.chat.id, data['start_message'])

        @self.bot.message_handler(commands=['yesorno'])
        def yes_or_no(message):
            choice = random.choice(data["YES_NO"])
            self.bot.send_message(message.chat.id, choice)

        @self.bot.message_handler(commands=['random'])
        def random_number(message):
            params = message.text.split()
            if len(params) != 3:
                self.bot.reply_to(message, "格式错误:\n/random <num1> <num2>，数字之间用空格隔开哦^o^")
                return
            a = int(params[1])
            b = int(params[2])
            number = random.randint(min(a, b), max(a, b))
            self.bot.send_message(message.chat.id, f"我的选择是{number}")

        @self.bot.message_handler(commands=['dosth'])
        def dosth(message):
            activity = random.choice(activities)
            self.bot.send_message(message.chat.id, activity)

        @self.bot.message_handler(commands=['choose'])
        def choose(message):
            options = message.text.split()[1:]
            if len(options) < 2:
                self.bot.reply_to(message, "至少2个选项,选项之间用空格隔开哦^o^")
                return
            random.shuffle(options)
            choice = options[0]
            self.bot.send_message(message.chat.id, f"我的选择是{choice}")

        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):
            if not message.text.startswith('/'):
                reply = random.choice(replies)
                self.bot.send_message(message.chat.id, reply)

    def start(self):
        self.bot.infinity_polling()
