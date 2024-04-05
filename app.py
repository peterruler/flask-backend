from flask import Flask, Response, request, jsonify
from io import BytesIO
import base64
from flask_cors import CORS, cross_origin
import os
import sys
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'

@app.route("/image", methods=['GET', 'POST'])
def image():
    if(request.method == "POST"):
        bytesOfImage = request.get_data()
        with open('image.jpeg', 'wb') as out:
            out.write(bytesOfImage)
        return "Image read"


@app.route("/video", methods=['GET', 'POST'])
def video():
    if(request.method == "POST"):
        bytesOfVideo = request.get_data()
        with open('video.mp4', 'wb') as out:
            out.write(bytesOfVideo)
        return "Video read"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=4000)