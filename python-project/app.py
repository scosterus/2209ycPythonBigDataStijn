from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql.server start
#127.0.0.1
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'skillapp'
 
#mysql = MySQL(app)

#with app.app_context():
    #cursor = mysql.connection.cursor()

#Statements
#cursor.execute("CREATE DATABSE skillapp")
#cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
#cursor.execute("CREATE TALBLE users (name VARCHAR(255), age int(3), endurance int(11), strength int(11), power int(11), speed int(11), agility int(11), nerve int(11), durability int(11), hand-eye-co int(11), analytical-appr int(11))")
#cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
#cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
#Saving the Actions performed on the DB
#mysql.connection.commit()
 
#Closing the cursor
#cursor.close()

#print("done")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/intro")
def intro():
    return render_template('intro.html')

@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@app.route("/fits")
def fits():
    return render_template('fits.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

