from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello guy, This is an example of flask App that ar deployed using github actions. '


