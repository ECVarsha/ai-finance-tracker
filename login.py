import streamlit as st
from database import get_user

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = get_user(username, password)
    if user:
        st.success(f"Welcome {username}!")
        st.session_state["logged_in"] = True
        st.session_state["user"] = username
    else:
        st.error("Invalid username or password")
