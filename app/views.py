# views.py
from flask import request
from flask import render_template
from app import app
import spotipy as sp

#Main page of the app.
@app.route('/')
def index():
    return render_template("index.html")

#Route that will receive the url of the user.
@app.route('/', methods=['POST'])
def url_post():
    imageURL = request.form['text']
    return render_template("image.html", imageURL=imageURL)
