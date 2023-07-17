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
        self.user_context = {}  # 用于存储用户的上下文数据

        @self.bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            self.bot.reply_to(message.chat.id, data['start_message'])

        @self.bot.message_handler(commands=['yesorno'])
        def yes_or_no(message):
            choice = random.choice(data["YES_NO"])
            self.bot.send_message(message.chat.id, choice)

        @self.bot.message_handler(commands=['random'])
        def get_start_number(message):
            self.bot.send_message(message.chat.id, "请输入起始数:")
            self.bot.register_next_step_handler(message, get_end_number)

        def get_end_number(message):
            try:
                start_number = int(message.text)

                self.bot.send_message(message.chat.id, "请输入终止数:")
                self.bot.register_next_step_handler(message, lambda msg: generate_random_number(msg, start_number))

            except ValueError:
                self.bot.send_message(message.chat.id, "无效的起始数，请输入一个整数")
                self.bot.send_message(message.chat.id, "请输入起始数:")
                self.bot.register_next_step_handler(message, get_start_number)

        def generate_random_number(message, start_number):
            try:
                end_number = int(message.text)

                number = random.randint(min(start_number, end_number), max(start_number, end_number))
                self.bot.send_message(message.chat.id, f"我的选择是{number}")

            except ValueError:
                self.bot.send_message(message.chat.id, "无效的终止数，请输入一个整数")
                self.bot.send_message(message.chat.id, "请输入终止数:")
                self.bot.register_next_step_handler(message, lambda msg: generate_random_number(msg, start_number))

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
