from io import BufferedReader
import streamlit as st
import requests
'''
# Doggy Detector
'''


# '''
# Predicted dog Breed
# '''


# url = "https://doggy-detector-2022-image-q34gthac5q-ts.a.run.app/predict?BUCKET_NAME=doggy-detector-2022-bucket-v2&BLOB_NAME=test_images/test"

# response = requests.get(url).json()

# breed = response['prediction']


# st.markdown(f'''
# {breed}
# ''')

image_file = st.file_uploader("Upload Images", type = ["png","jpg","jpeg"])
if image_file is not None:
    st.write(type(image_file))
