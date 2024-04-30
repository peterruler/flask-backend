from flask import Flask, Response, request, jsonify
from io import BytesIO
import base64
from flask_cors import CORS, cross_origin
import os
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json

app = Flask(__name__)
cors = CORS(app)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'

@app.route("/image", methods=['GET', 'POST'])
def image():
    if(request.method == "POST"):
        bytesOfImage = request.get_data()
        with open('image.jpeg', 'wb') as out:
            out.write(bytesOfImage)

        # load json and create model
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        # load weights into new model
        loaded_model.load_weights("model.h5")

        # evaluate loaded model on test data
        loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

        test_dir = "./"
        img_path = os.path.join(test_dir, '{}'.format("image.jpeg"))
        image_size = (180, 180)
        img = keras.utils.load_img(
           img_path, target_size=image_size
        )
        img_array = keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = loaded_model.predict(img_array, verbose=0)
        score = float(predictions[0])
        return_text = ""
        if 0.2 < score < 0.8:
            return_text = "Bei diesem Bild konnte Tiertyp nicht ermittelt werden! Sind Sie sicher, dass es sich um das Bild eines Hundes oder einer Katze handelt?"
        else :
            return_text = f"Dieses Bild ist {100 * (1 - score):.2f}% Katze und {100 * score:.2f}% Hund."

        print(return_text)
        return return_text

'''
@app.route("/video", methods=['GET', 'POST'])
def video():
    if(request.method == "POST"):
        bytesOfVideo = request.get_data()
        with open('video.mp4', 'wb') as out:
            out.write(bytesOfVideo)
        return "Video read"
'''
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=4000)