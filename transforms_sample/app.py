from flask import Flask
import os
import configparser

app = Flask(__name__)


@app.route('/')
def hello():
    message = os.getenv('MESSAGE', 'Hello World')
    config = configparser.ConfigParser()
    config.read('setup.cfg')
    version = config.get('metadata', 'version')
    return "{} (ver. {})".format(message, version)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
