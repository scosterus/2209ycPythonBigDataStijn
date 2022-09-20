from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/anders")
def methode():
    return "<p>Iets anders neerzetten</p>"