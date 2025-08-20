import streamlit as st
import sqlite3
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# -------------------
# DATABASE SETUP
# -------------------
conn = sqlite3.connect("expenses.db", check_same_thread=False)
c = conn.cursor()

# Create user table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT)''')

# Create expenses table (added date column)
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (username TEXT, amount REAL, category TEXT, note TEXT, date TEXT)''')
conn.commit()

# -------------------
# HELPER FUNCTIONS
# -------------------
def make_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password):
    c.execute("INSERT INTO users VALUES (?,?)", (username, make_hash(password)))
    conn.commit()

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", 
              (username, make_hash(password)))
    return c.fetchall()

def add_expense(username, amount, category, note, exp_date):
    c.execute("INSERT INTO expenses VALUES (?,?,?,?,?)", 
              (username, amount, category, note, exp_date))
    conn.commit()

def get_expenses(username):
    df = pd.read_sql_query("SELECT amount, category, note, date FROM expenses WHERE username=?", 
                           conn, params=(username,))
    return df

# -------------------
# STREAMLIT UI
# -------------------
st.set_page_config(page_title="AI Personal Finance Tracker", layout="centered")

st.title("💸 AI-powered Personal Finance Tracker")

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

menu = ["Home", "Login", "SignUp"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to AI Personal Finance Tracker")
    st.write("Track your expenses, analyze spending patterns, and get AI-powered insights.")

elif choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type='password')
    if st.button("Sign Up"):
        if new_user and new_pass:
            add_user(new_user, new_pass)
            st.success("Account created successfully! Go to Login.")
        else:
            st.warning("Please enter username and password")

elif choice == "Login":
    if not st.session_state.logged_in:
        st.subheader("Login Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            result = login_user(username, password)
            if result:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success(f"Welcome {username}")
            else:
                st.warning("Incorrect Username/Password")
    else:
        # ---- Dashboard ----
        st.subheader("📊 Dashboard")
        st.write(f"Logged in as **{st.session_state.user}**")

        amount = st.number_input("Expense Amount", min_value=1.0)
        category = st.selectbox("Category", ["Food", "Travel", "Bills","Shopping","Gym","Groceries","Online Subscriptions","Gadgets & Accessories","Other"])
        note = st.text_input("Note")
        exp_date = st.date_input("Date", date.today())

        if st.button("Add Expense"):
            add_expense(st.session_state.user, amount, category, note, str(exp_date))
            st.success(f"Added {amount} under {category} ✅")

        df = get_expenses(st.session_state.user)
        if not df.empty:
            st.write("### Expense History")
            st.dataframe(df)

            # Chart - Spending by Category
            st.write("### Spending by Category")
            fig1, ax1 = plt.subplots()
            df.groupby("category")["amount"].sum().plot(kind="bar", ax=ax1)
            st.pyplot(fig1)

            # Chart - Spending Over Time
            st.write("### Spending Over Time")
            df["date"] = pd.to_datetime(df["date"])
            fig2, ax2 = plt.subplots()
            df.groupby("date")["amount"].sum().plot(kind="line", marker="o", ax=ax2)
            st.pyplot(fig2)

        # Logout
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.success("Logged out successfully!")
