from ast import Return
from genericpath import exists
from itertools import count
from sqlite3 import Cursor, connect 
from flask import Flask, render_template, request, flash, abort, current_app, make_response

from mimetypes import guess_extension
from werkzeug.utils import secure_filename
from gtts import gTTS
from flask import jsonify
import os
from playsound import playsound
from os import path
import webbrowser 
import speech_recognition as sr
import pymysql
import mysql.connector
connection=pymysql.connect(host="localhost",user="root",password="123456",database="pythondb")
cursor = connection.cursor() 


def information(username):
    user_name=username
    return username

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/Howtouse")
def Howtouse():
    return render_template("Howtouse.html")

@app.route("/loginforstudent",methods=['POST']  )
def loginforstudent():
         username=request.form.get("username")
         password=request.form.get("password")
         user=information(username)
         q=("SELECT * FROM  employee WHERE emp_name=(%s)")
         v=(username)
         cursor.execute(q,v)
         data2 = cursor.fetchall()
         q3=("SELECT count(*) FROM employee WHERE emp_name=(%s)")
         v3=(username)
         v=cursor.execute(q3,v3)
         value34=cursor.fetchone()[0]

         if (value34 == 0):
           return render_template("login.html") 
         else:
          return render_template("afterLogin.html",value2=data2)#value=data , )
             

@app.route("/afterLogin/<name>")
def afterLogin(name):
    q=("SELECT * FROM  employee WHERE emp_name=(%s)")
    v=(name)
    cursor.execute(q,v)
    data2 = cursor.fetchall()
    return render_template("afterLogin.html",value2=data2)


@app.route("/StudentSchedule/<name>")
def StudentSchedule(name):
   
   q=("SELECT * FROM  student_schedule WHERE name=(%s)")
   v=(name)
   cursor.execute(q,v)
   data2 = cursor.fetchall()
   
   return render_template("StudentSchedule.html",course=data2)

@app.route("/StudentPlan")
def StudentPlan():
    return render_template("StudentPlan.html")

@app.route("/StudentRegestration")
def StudentRegestration():
    return render_template("StudentRegestration.html")

@app.route("/Financial/<name>")
def Financial(name):
   q=("SELECT * FROM  financial WHERE name=(%s)")
   v=(name)
   cursor.execute(q,v)
   data2 = cursor.fetchall()
   return render_template("Financial.html",financial=data2)


if __name__=="__main__":
     app.run(port=9000)