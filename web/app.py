import flask
from markupsafe import escape

app = flask.Flask(__name__)


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == "__main__":
    app.run(debug=True, port=8000)

