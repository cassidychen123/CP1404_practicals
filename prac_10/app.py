from flask import Flask

app = Flask(__name__)


@app.route('/')
def name():
    return 'Zhaomin Chen'


if __name__ == '__main__':
    app.run()