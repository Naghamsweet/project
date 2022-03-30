from ast import Return
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

@app.route("/loginforstudent" ,methods=['POST'] )
def loginforstudent():
    return render_template("afterLogin.html")

@app.route("/StudentSchedule")
def StudentSchedule():
    return render_template("StudentSchedule.html")

@app.route("/StudentPlan")
def StudentPlan():
    return render_template("StudentPlan.html")

@app.route("/StudentRegestration")
def StudentRegestration():
    return render_template("StudentRegestration.html")


if __name__=="__main__":
     app.run(port=9000)