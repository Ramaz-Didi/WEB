import streamlit as st
from PIL import Image
import pandas

df=pandas.read_csv("data.csv",sep=";")
image1 = Image.open('photo1.jpg')

#setting container size
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
   st.image(image1)

with col2:
    st.title("Ardit Sulce")
    content ="""
    Hi it's me
    """
    st.info(content)
content2 = """
below comment
"""
st.write(content2)

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
       st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
       st.header(row["title"])
