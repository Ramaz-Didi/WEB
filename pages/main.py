import streamlit as st
from PIL import Image

#image1 = Image.open('photo1.jpg')

#setting container size
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

#with col1:
#   st.image(image1)

with col2:
    st.title("Ardit Sulce")
    content ="""
    Hi it's me
    """
    st.info(content)
    