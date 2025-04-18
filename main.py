from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello guy, This is an example of flask App.'


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/goodbye')
def goodbye():
    return 'Goodbye, World!'
