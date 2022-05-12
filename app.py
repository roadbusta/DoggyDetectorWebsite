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




#Google cloud credentials
os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = "doggy-detector-2022-dff1082f34a6.json"
BUCKET_NAME = "doggy-detector-2022-bucket-v2"
BUCKET_DESTINATION = "test_images/test"


# '''
# Define relevant functions
# '''
def breed():
    """
    Access the api and returns the prediction dictionary containing the top two predicted breeds and their associated likelihoods
    """
    url = f"https://doggy-detector-2022-image-q34gthac5q-ts.a.run.app/predict?BUCKET_NAME={BUCKET_NAME}&BLOB_NAME={BUCKET_DESTINATION}"

    response = requests.get(url).json()
    return response['prediction']

def load_image(image_file):
    """
    Takes the image and opens it as an image file.
    It then saves the image as 'test.jpg'
    """
    img = Image.open(image_file)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.save("test.jpg")
    return img

#Allow image to be uploaded
st.markdown("Upload File")
image_file = st.file_uploader("Upload Images", type = ["png","jpg","jpeg"])


if image_file is not None:

    st.image(load_image(image_file))
    st.markdown("I'm thinking...")


    #Upload to google cloud
    client = storage.Client().bucket(BUCKET_NAME)
    blob = client.blob(BUCKET_DESTINATION)
    blob.upload_from_filename("test.jpg")


    #Make prediction
    prediction = breed()
    prediction_1 = prediction[0]
    prediction_2 = prediction[1]

    if prediction_1[0] > 0.85:
        st.markdown(f"This is a {prediction_1[1]}") # Return a single prediction where prediction score is high
    else:
        st.markdown(f"This looks like it might be a {prediction_1[1]} or a {prediction_2[1]}") # Return multiple predictions where prediction score is not high
