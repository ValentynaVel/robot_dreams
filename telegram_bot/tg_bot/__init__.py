from flask import Flask
from telegram.ext import Updater
from .views import shopping_list_bp
from .handlers import register_handlers
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


def create_app():
    app = Flask(__name__)
    app.register_blueprint(shopping_list_bp)

    updater = Updater("TOKEN")
    dp = updater.dispatcher
    register_handlers(dp)
    updater.start_polling()

    return app

