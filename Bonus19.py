import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    #start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
    #create pillow image intance
    img = Image.open(camera_image)

    #Convert the pillow image to grayscale
    gray_image = img.convert("L")

    # Render the gratscale image on the webpage
    st.image(gray_image)