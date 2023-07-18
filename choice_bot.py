#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import random
import telebot
from telebot import types
from data import data, mindfulness
from functions import RandomHandler, ChooseHandler, handle_text, short_term, long_term, get_options_keyboard


class ChoiceBot:
    def __init__(self, api_token):
        self.bot = telebot.TeleBot(api_token)
        self.bot.delete_webhook()
        self.user_context = {}  # 用于存储用户的上下文数据
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        keyboard.add('短时间', '长时间')

        @self.bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            self.bot.send_message(message.chat.id, data['start_message'])

        @self.bot.message_handler(commands=['yesorno'])
        def yes_or_no(message):
            choice = random.choice(data["YES_NO"])
            self.bot.send_message(message.chat.id, choice)

        @self.bot.message_handler(commands=['random'])
        def get_start_number(message):
            random_handler = RandomHandler(self.bot)
            random_handler.get_start_number(message)

        @self.bot.message_handler(commands=['dosth'])
        # def do_sth(message):
        #     dosth(message, self.bot)
        def send_options(message):
            keyboard = get_options_keyboard(types)
            self.bot.send_message(message.chat.id, '- 如果你不知道未来15分钟内的时间要干什么，请选择“短时间”.\n- 如果你有一天或半天的空闲时间，请选择“长时间”',
                                  reply_markup=keyboard)

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            if call.data == 'short':
                short_term(call.message, self)
            elif call.data == 'long':
                long_term(call.message, self)

        @self.bot.message_handler(commands=['mindfulness'])
        def mind(message):
            mindfulness_chose = random.choice(mindfulness)
            self.bot.send_message(message.chat.id, mindfulness_chose)

        @self.bot.message_handler(commands=['choose'])
        def choose(message):
            choose_handler = ChooseHandler(self.bot)
            choose_handler.get_option_count(message)

        @self.bot.message_handler(content_types=['text'])
        def handle_message(message):
            handle_text(message, self.bot)

    def start(self):
        self.bot.infinity_polling()
