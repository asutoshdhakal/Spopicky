# views.py
from flask import request
from flask import render_template
from app import app
import spotipy as sp
import httplib
import urllib
import json

#Main page of the app.
@app.route('/')
def index():
    return render_template("index.html")

#Route that will receive the url of the user.
@app.route('/results', methods=['POST'])
def url_post():
    imageURL = request.form['text']
    searchQuery = vision_words(imageURL) #pass in url into method that will return list of words
    return render_template("image.html", imageURL=imageURL, searchQuery=searchQuery)


#Method that will send image.html the words received from
#Microsoft vision api.
def vision_words(url):
    headers = {
        'Content-type': 'application/json',
    }

    params = urllib.urlencode({
        'subscription-key': 'ad55657c192544d2891a892a9430e703',
        'visualFeatures': 'All',
    })
    try:
        image_url = "http://www.martin-thoma.de/bilder/Martin_Thoma_web_thumb.jpg"
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/describe?%s" % params,"{'Url': '%s'}" % url, headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    text = data['description']['captions']
    return text[0]['text']
