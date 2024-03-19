from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    message = os.getenv('MESSAGE', 'Hello World')
    timestamp = os.getenv('TIMESTAMP', 'Tue, Mar 19, 2024  5:08:17 PM')
    return "{} ({})".format(message, timestamp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
