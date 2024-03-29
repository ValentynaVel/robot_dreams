from flask import Flask
from logging.config import dictConfig
from config import AppConfig


app = Flask(__name__)


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handler': ['wsgi']
    }
})

app.config.from_object(AppConfig)

from views import *





