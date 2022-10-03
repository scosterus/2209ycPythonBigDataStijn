from flask import Flask
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "bigdata-database.mysql.database.azure.com",
    port = "3306",
    user = "bigData",
    password = "qwer1234QWER!@#$",
    database = "skillapp"
    )

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE skillapp")
# mycursor.execute("CREATE TABLE users (ID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), age int(3), endurance int(11), strength int(11), power int(11), speed int(11), flexibilty int(11), agility int(11), nerve int(11), durability int(11), hand_eye_co int(11), analytical_appr int(11))")

# db.commit()

print("Done!")


@app.route("/")
def index():
    return "hallo"

@app.route("/intro/<vnaam>/<age>")
def intro(vnaam,age):
    mycursor.execute("INSERT INTO users (name, age) VALUES ('%s', '%s')" % (vnaam, age))
    db.commit()
    mycursor.execute("SELECT MAX(ID) FROM users")
    id = mycursor.fetchone()[0]
    print(id, vnaam, age, "added")
    return id

@app.route("/quiz/<speed>/<id>")
def quiz(speed, id):
    mycursor.execute("UPDATE users SET speed = '%s' WHERE ID = '%s'" % (speed, id))
    db.commit()
    print(speed, "added")
    return "beantwoord speed"

@app.route("/fits")
def fits():
    return 'fits.html'

@app.route("/home")
def home():
    return 'home.html'
