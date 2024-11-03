import streamlit as st

st.write("hello")

st.slider("Amount", min_value=10, max_value=30)

user_choice = st.radio("Amount",options=[10,20,30])
if user_choice ==30:
    st.info("Good")