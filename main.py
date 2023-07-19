import os
from choice_bot import ChoiceBot

api_token = os.environ.get('API_TOKEN')

if __name__ == '__main__':
    bot = ChoiceBot(api_token)
    bot.start()
