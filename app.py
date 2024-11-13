from urllib import request
from flask import Flask, request, jsonify
from PIL import Image
import io
import cv2
import tensorflow as tf
import numpy as np
from flask_cors import CORS
# from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app, resources={
    r"/classify": {
        "origins": [
            "http://localhost:5173", 
            "https://cifar-10-8rlk80iaj-david-malviyas-projects.vercel.app"
        ]
    }
})

model_path = './CIFAR-10.h5'
model = tf.keras.models.load_model(model_path)

class_labels = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck"
}
def preprocess_image(image):
    print(type(image))
    img = np.array(image)
    img = cv2.resize(img, (32, 32))
    img_array = img / 255.0
    img = img_array.reshape(1, 32, 32, 3)
    return img

@app.route("/classify", methods=['POST'])
def classify():

    if 'file' not in request.files:
        print("---------------------------------------------------------------------")
        return jsonify({'message' : 'File not provided!!'})

    file = request.files['file']
    image = Image.open(io.BytesIO(file.read()))
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    # print(prediction)

    prediction = np.argmax(prediction)
    # print(prediction)
    # print(class_labels[prediction])

    return jsonify({'result' : class_labels[prediction]})

if __name__ == "__main__":
    app.run(debug=True)
