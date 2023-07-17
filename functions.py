import random


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
            self.bot.send_message(message.chat.id, "无效的起始数，请输入一个整数")
            self.bot.send_message(message.chat.id, "请输入起始数:")
            self.bot.register_next_step_handler(message, self.get_start_number)

    def generate_random_number(self, message, start_number):
        try:
            end_number = int(message.text)

            number = random.randint(min(start_number, end_number), max(start_number, end_number))
            self.bot.send_message(message.chat.id, f"我的选择是{number}")

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
        self.bot.send_message(message.chat.id, f"我的选择是{choice}")
