from flask import Flask
from logging.config import dictConfig


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

app = Flask(__name__)


@app.route('/hello')
def hello():
    app.logger.info('This is a request to `/hello`')
    return '<h1 style="color:red">Hello, world!</h1>'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
