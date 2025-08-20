import streamlit as st
from database import create_user

st.title("Sign Up")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Sign Up"):
    try:
        create_user(username, password)
        st.success("Account created successfully! Please go to Login page.")
    except:
        st.error("Username already exists! Try another one.")
