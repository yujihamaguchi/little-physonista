from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    message = os.getenv('MESSAGE', 'Hello World')
    return message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
