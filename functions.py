import random
import re

from data import replies, sleeps, activities_short_term, activities_long_term, greetings, sad, angry, anxious, lonely, \
    disappointed, activities_sleep
import datetime
import pytz


class RandomHandler:
    def __init__(self, bot):
        self.bot = bot

    def get_start_number(self, message):
        self.bot.send_message(message.chat.id, "请输入起始数:")
        self.bot.register_next_step_handler(message, self.get_end_number)

    def get_end_number(self, message):
        try:
            start_number = int(message.text)

            self.bot.send_message(message.chat.id, "请输入终止数:")
            self.bot.register_next_step_handler(message, lambda msg: self.generate_random_number(msg, start_number))

        except ValueError:
            self.bot.send_message(message.chat.id, "无效的起始数，请输入一个整数。")
            self.get_start_number(message)

    def generate_random_number(self, message, start_number):
        try:
            end_number = int(message.text)

            number = random.randint(min(start_number, end_number), max(start_number, end_number))
            self.bot.send_message(message.chat.id, f"我的选择是【 {number} 】✨")

        except ValueError:
            self.bot.send_message(message.chat.id, "无效的终止数，请输入一个整数")
            self.bot.send_message(message.chat.id, "请输入终止数:")
            self.bot.register_next_step_handler(message, lambda msg: self.generate_random_number(msg, start_number))


class ChooseHandler:
    def __init__(self, bot):
        self.bot = bot
        self.options = {}

    def get_option_count(self, message):
        self.bot.send_message(message.chat.id, "请输入选项个数:")
        self.bot.register_next_step_handler(message, self.get_option_inputs)

    def get_option_inputs(self, message):
        try:
            num = int(message.text)
            if num < 2:
                self.bot.send_message(message.chat.id, "至少2个选项，请重新输入选项个数:")
                self.bot.register_next_step_handler(message, self.get_option_inputs)
                return

            self.options['num'] = num
            self.options['current_option'] = 1
            self.options['choices'] = {}

            self.bot.send_message(message.chat.id, f"请输入选项{self.options['current_option']}:")
            self.bot.register_next_step_handler(message, self.save_option_input)

        except ValueError:
            self.bot.send_message(message.chat.id, "无效的选项个数，请输入一个整数")
            self.bot.send_message(message.chat.id, "请输入选项个数:")
            self.bot.register_next_step_handler(message, self.get_option_count)

    def save_option_input(self, message):
        if message.text.startswith('/'):
            # 用户输入了其他命令，停止执行当前代码
            return

        try:
            option_num = self.options['current_option']
            self.options['choices'][option_num] = message.text

            if option_num < self.options['num']:
                self.options['current_option'] += 1
                self.bot.send_message(message.chat.id, f"请输入选项{self.options['current_option']}:")
                self.bot.register_next_step_handler(message, self.save_option_input)
            else:
                self.choose_option(message)

        except ValueError:
            self.bot.send_message(message.chat.id, "无效的选项，请重新输入选项:")
            self.bot.register_next_step_handler(message, self.save_option_input)

    def choose_option(self, message):
        option_values = list(self.options['choices'].values())
        random.shuffle(option_values)
        choice = random.choice(option_values)
        self.bot.send_message(message.chat.id, f"我的选择是【 {choice} 】✨")


def handle_text(message, bot):
    pattern_greet = re.compile(r"hello|hi|你好|hey|你是")
    pattern_sad = re.compile(r"😭|伤心|难受|难过|😮‍💨|哎|唉|难受|死|失望|悲伤|沮丧|痛苦|心碎|郁闷|💔|😤|心碎|痛苦|伤心|失恋|痛心|失望|悲伤")
    pattern_angry = re.compile(r"😡|生气|愤怒|气愤|发火|火大|气死|吵架")
    pattern_anxious = re.compile(r"😰|焦虑|紧张|担心|忧虑|不安|烦躁|害怕|😫|压力|累|疲|倦|疲劳|憔悴|心力交瘁|😟|困扰")
    pattern_lonely = re.compile(r"😔|孤单|寂寞|无聊|孤独|空虚|陪")
    pattern_disappointed = re.compile(r"失望|沮丧|郁闷|可惜|😤|挫折|失意|无奈|无力|懊悔|泄气")
    if not message.text.startswith('/'):
        if pattern_greet.search(message.text):
            greeting = random.choice(greetings)
            bot.send_message(message.chat.id, greeting)
        elif is_within_time_range():
            sleep = random.choice(sleeps)
            bot.send_message(message.chat.id, sleep)
        elif pattern_sad.search(message.text):
            sad_random = random.choice(sad)
            bot.send_message(message.chat.id, sad_random)
        elif pattern_angry.search(message.text):
            angry_random = random.choice(angry)
            bot.send_message(message.chat.id, angry_random)
        elif pattern_anxious.search(message.text):
            anxious_random = random.choice(anxious)
            bot.send_message(message.chat.id, anxious_random)
        elif pattern_lonely.search(message.text):
            lonely_random = random.choice(lonely)
            bot.send_message(message.chat.id, lonely_random)
        elif pattern_disappointed.search(message.text):
            disappointed_random = random.choice(disappointed)
            bot.send_message(message.chat.id, disappointed_random)
        elif message.text.endswith('？') | message.text.endswith('?'):
            reply = random.choice(replies)
            bot.send_message(message.chat.id, reply)
        else:
            pass


def is_within_time_range():
    local_time = datetime.datetime.now()
    local_tz = pytz.timezone('Asia/Shanghai')  # 设置本地时区
    beijing_time = local_time.astimezone(local_tz)
    hour = beijing_time.hour
    return hour >= 23 or hour < 5


def get_options_keyboard(types):
    keyboard = types.InlineKeyboardMarkup()

    short_time_btn = types.InlineKeyboardButton(text='短时间', callback_data='short')
    long_time_btn = types.InlineKeyboardButton(text='长时间', callback_data='long')

    keyboard.add(short_time_btn, long_time_btn)

    return keyboard


def short_term(message, self):
    activity = random.choice(activities_short_term)
    self.bot.send_message(message.chat.id, activity)


def long_term(message, self):
    activity = random.choice(activities_long_term)
    self.bot.send_message(message.chat.id, activity)


def sleep_activity(message, bot):
    activity = random.choice(activities_sleep)
    bot.send_message(message.chat.id, activity)
