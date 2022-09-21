from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/quiz")
def index_quiz():
    return render_template('index_quiz.html')
