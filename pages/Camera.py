import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Start Camera"):
    #started camera
    camera_image =st.camera_input("Camera")
#print(camera_image)


if camera_image:
    #create a pillow image instance
    img = Image.open(camera_image)

    #Convert the pillow image to grayscale
    gray_img = img.convert("L")

    #render the grayscale image on the web
    st.image(gray_img)

uploaded_image = st.file_uploader("Upload Image") 

if uploaded_image:
    #create a pillow image instance
    img = Image.open(uploaded_image)

    #Convert the pillow image to grayscale
    gray_uploaded_img = img.convert("L")

    #render the grayscale image on the web
    st.image(gray_uploaded_img)
