import os
from os.path import exists
from choice_bot import ChoiceBot
from dotenv import load_dotenv

api_token = None
if exists(".env"):
    load_dotenv('.env')
    api_token = os.getenv('API_TOKEN')

if not api_token:
    api_token = os.environ.get('API_TOKEN')
if __name__ == '__main__':
    bot = ChoiceBot(api_token)
    bot.start()
