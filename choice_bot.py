#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import random
import telebot
from data import data, activities, replies
from functions import RandomHandler


class ChoiceBot:
    def __init__(self, api_token):
        self.bot = telebot.TeleBot(api_token)
        self.bot.delete_webhook()
        self.user_context = {}  # 用于存储用户的上下文数据
        random_handler = RandomHandler(self.bot)

        @self.bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            self.bot.reply_to(message.chat.id, data['start_message'])

        @self.bot.message_handler(commands=['yesorno'])
        def yes_or_no(message):
            choice = random.choice(data["YES_NO"])
            self.bot.send_message(message.chat.id, choice)

        @self.bot.message_handler(commands=['random'])
        def get_start_number(message):
            random_handler.get_start_number(message)

        @self.bot.message_handler(commands=['dosth'])
        def dosth(message):
            activity = random.choice(activities)
            self.bot.send_message(message.chat.id, activity)

        @self.bot.message_handler(commands=['choose'])
        def get_option_count(message):
            self.bot.send_message(message.chat.id, "请输入选项个数:")
            self.bot.register_next_step_handler(message, get_option_inputs)

        def get_option_inputs(message):
            try:
                num = int(message.text)
                if num < 2:
                    self.bot.send_message(message.chat.id, "至少2个选项，请重新输入选项个数:")
                    self.bot.register_next_step_handler(message, get_option_inputs)
                    return

                options = {}
                options['num'] = num
                options['current_option'] = 1
                options['choices'] = {}

                self.bot.send_message(message.chat.id, f"请输入选项{options['current_option']}:")
                self.bot.register_next_step_handler(message, lambda msg: save_option_input(msg, options))

            except ValueError:
                self.bot.send_message(message.chat.id, "无效的选项个数，请输入一个整数")
                self.bot.send_message(message.chat.id, "请输入选项个数:")
                self.bot.register_next_step_handler(message, get_option_count)

        def save_option_input(message, options):
            try:
                option_num = options['current_option']
                options['choices'][option_num] = message.text

                if option_num < options['num']:
                    options['current_option'] += 1
                    self.bot.send_message(message.chat.id, f"请输入选项{options['current_option']}:")
                    self.bot.register_next_step_handler(message, lambda msg: save_option_input(msg, options))
                else:
                    choose_option(options, message)

            except ValueError:
                self.bot.send_message(message.chat.id, "无效的选项，请重新输入选项:")
                self.bot.register_next_step_handler(message, lambda msg: save_option_input(msg, options))

        def choose_option(options, message):
            option_values = list(options['choices'].values())
            random.shuffle(option_values)
            choice = random.choice(option_values)
            self.bot.send_message(message.chat.id, f"我的选择是{choice}")

        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):
            if not message.text.startswith('/'):
                reply = random.choice(replies)
                self.bot.send_message(message.chat.id, reply)

    def start(self):
        self.bot.infinity_polling()
