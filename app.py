from flask import Flask, request

from middleware import middleware

app = Flask(__name__)
app.wsgi_app = middleware(app.wsgi_app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    # using
    user = request.environ['user']
    return "Hi %s" % user['name']


@app.route("/")
def count_simulations():
    return "<p>Hello, World!</p>"


@app.route("/")
def state():
    return "<p>Hello, World!</p>"


@app.route("/")
def listing():
    return "<p>Hello, World!</p>"


@app.route("/")
def fixtures_id():
    return "<p>Hello, World!</p>"


@app.route("/")
def fixtures_info():
    return "<p>Hello, World!</p>"


@app.route("/")
def graph():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)
