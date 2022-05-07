from io import BufferedReader, StringIO
import streamlit as st
import requests
from google.cloud import storage
import os
from PIL import Image
'''
# Doggy Breed Detector
'''
##

# '''
# Predicted dog Breed
# '''

def breed():
    url = "https://doggy-detector-2022-image-q34gthac5q-ts.a.run.app/predict?BUCKET_NAME=doggy-detector-2022-bucket-v2&BLOB_NAME=test_images/test"

    response = requests.get(url).json()

    return response['prediction']




# Take a photo
# st.camera_input(label, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)

#Google cloud credentials
os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = "doggy-detector-2022-dff1082f34a6.json"
BUCKET_NAME = "doggy-detector-2022-bucket-v2"
BUCKET_DESTINATION = "test_images/test"

def load_image(image_file):
    img = Image.open(image_file)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.save("test.jpg")
    return img


image_file = st.file_uploader("Upload Images", type = ["png","jpg","jpeg"])
st.markdown("I'm thinking...")
if image_file is not None:
    st.image(load_image(image_file))


    #Upload to google cloud
    client = storage.Client().bucket(BUCKET_NAME)
    blob = client.blob(BUCKET_DESTINATION)
    blob.upload_from_filename("test.jpg")


    #Make prediction
    prediction = breed()[0]
    prediction_1 = prediction[0]
    prediction_2 = prediction[1]

    if prediction_1[0] > 0.85:
        st.markdown(f"This is a {prediction_1[1]}")
    else:
        st.markdown(f"This looks like it might be a {prediction_1[1]} or a {prediction_2[1]}")
