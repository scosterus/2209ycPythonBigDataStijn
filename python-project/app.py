from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    port = "8889",
    user = "root",
    password = "root",
    database = "skillapp"
    )

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE skillapp")
# mycursor.execute("CREATE TABLE users (ID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), age int(3), endurance int(11), strength int(11), power int(11), speed int(11), agility int(11), nerve int(11), durability int(11), hand_eye_co int(11), analytical_appr int(11))")

# db.commit()

print("Done!")


@app.route("/", methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route("/intro/<vnaam>/<age>")
def intro(vnaam,age):
    mycursor.execute("INSERT INTO users (name, age) VALUES ('%s', '%s')" % (vnaam, age))
    db.commit()
    print(vnaam, age, "added")
    return "data naam en leeftijd"

@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@app.route("/fits")
def fits():
    return render_template('fits.html')

@app.route("/home")
def home():
    return render_template('home.html')
