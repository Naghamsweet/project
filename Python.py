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





if __name__=="__main__":
     app.run(port=9000)