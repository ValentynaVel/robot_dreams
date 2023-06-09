import json
from pprint import pprint
import requests
from .services import WeatherService, WeatherServiceException
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

TG_BASE_URL = 'https://api.telegram.org/bot'


class User:
    def __init__(self, first_name, id, is_bot, language_code, username):
        self.first_name = first_name
        self.id = id
        self.is_bot = is_bot
        self.username = username


class TelegramHandler:
    user = None

    def send_markup_message(self, text, markup):
        data = {
            'chat_id': self.user.id,
            'text': text,
            'reply_markup': markup
        }
        requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)

    def send_message(self, text):
        data = {
            'chat_id': self.user.id,
            'text': text
        }
        requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)


class MessageHandler(TelegramHandler):

    def __init__(self, data):
        self.user = User(**data.get('from'))
        self.text = data.get('text')

    def handle(self):
        match self.text.split():
            case 'weather', city:
                try:
                    geo_data = WeatherService.get_geo_data(city)
                except WeatherServiceException as wse:
                    self.send_message(str(wse))
                else:
                    buttons = []
                    pprint(geo_data)
                    for item in geo_data:
                        test_button = {
                            'text': f'{item.get("name")} - {item.get("country")} - {item.get("country_code")}',
                            'callback_data': json.dumps(
                                {'lat': item.get('latitude'), 'lon': item.get('longitude')}
                            )
                        }
                        buttons.append([test_button])
                    markup = {
                        'inline_keyboard': buttons
                    }
                    self.send_markup_message('Select option', markup)


class CallbackHandler(TelegramHandler):

    def __init__(self, data):
        self.user = User(**data.get('from'))
        self.callback_data = json.loads(data.get('data'))

    def handle(self):
        try:
            weather = WeatherService.get_current_weather_by_geo_data(**self.callback_data)
        except WeatherServiceException as wse:
            self.send_message(str(wse))
        else:
            self.send_message(json.dumps(weather))








