# from urllib import request
# from flask import Flask, request, jsonify
# from PIL import Image
# import io
# import cv2
# import tensorflow as tf
# import numpy as np
# from flask_cors import CORS
# # from tensorflow.keras.models import load_model

# app = Flask(__name__)
# CORS(app, resources={r"/classify": {"origins": "https://cifar-10-ecpwnrbnx-david-malviyas-projects.vercel.app"}})

# model_path = './CIFAR-10.h5'
# model = tf.keras.models.load_model(model_path)

# class_labels = {
#     0: "airplane",
#     1: "automobile",
#     2: "bird",
#     3: "cat",
#     4: "deer",
#     5: "dog",
#     6: "frog",
#     7: "horse",
#     8: "ship",
#     9: "truck"
# }
# def preprocess_image(image):
#     print(type(image))
#     img = np.array(image)
#     img = cv2.resize(img, (32, 32))
#     img_array = img / 255.0
#     img = img_array.reshape(1, 32, 32, 3)
#     return img

# @app.route("/classify", methods=['POST'])
# def classify():

#     if 'file' not in request.files:
#         print("---------------------------------------------------------------------")
#         return jsonify({'message' : 'File not provided!!'})

#     file = request.files['file']
#     image = Image.open(io.BytesIO(file.read()))
#     processed_image = preprocess_image(image)
#     prediction = model.predict(processed_image)
#     # print(prediction)

#     prediction = np.argmax(prediction)
#     # print(prediction)
#     # print(class_labels[prediction])

#     return jsonify({'result' : class_labels[prediction]})

# if __name__ == "__main__":
#     app.run(debug=True)




import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2

# Load model
model = tf.keras.models.load_model("CIFAR-10.h5")

# Class labels
class_labels = {
    0: "airplane", 1: "automobile", 2: "bird", 3: "cat", 4: "deer",
    5: "dog", 6: "frog", 7: "horse", 8: "ship", 9: "truck"
}

def preprocess_image(image):
    img = np.array(image.resize((32, 32)))  # Resize
    img = img / 255.0
    img = img.reshape(1, 32, 32, 3)
    return img

# Streamlit UI
st.title("CIFAR-10 Image Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')

    # Resize for better display (optional: keep aspect ratio)
    display_image = image.resize((256, 256))

    st.image(display_image, caption="Uploaded Image", use_container_width=True)

