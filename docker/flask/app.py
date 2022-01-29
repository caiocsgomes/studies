from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hi there!"


app.run(host="0.0.0.0", port=8080)
