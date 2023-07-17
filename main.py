import os
from choice_bot import ChoiceBot
from dotenv import load_dotenv

load_dotenv('.env')
api_token = os.getenv('API_TOKEN')
API_TOKEN = ''
if __name__ == '__main__':
    bot = ChoiceBot(api_token)
    bot.start()
