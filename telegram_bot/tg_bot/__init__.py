from flask import Flask
from telegram.ext import Updater
from .views import shopping_list_bp
from .handlers import register_handlers


def create_app():
    app = Flask(__name__)
    app.register_blueprint(shopping_list_bp)

    updater = Updater("TELEGRAM_BOT_TOKEN")
    dp = updater.dispatcher
    register_handlers(dp)
    updater.start_polling()

    return app

