from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello flask deployment in docker and linux with docker "


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
