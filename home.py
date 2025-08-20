import streamlit as st
import sqlite3
import pandas as pd
import altair as alt

# Function to connect to database
def get_db_connection():
    conn = sqlite3.connect("users.db")   # ✅ same DB as app.py
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database table if not exists
def init_expenses_table():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            username TEXT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            note TEXT,
            date TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Add expense
def add_expense(username, amount, category, note, date):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO expenses (username, amount, category, note, date) VALUES (?, ?, ?, ?, ?)",
        (username, amount, category, note, date),
    )
    conn.commit()
    conn.close()

# Get expenses
def get_expenses(username):
    conn = get_db_connection()
    expenses = pd.read_sql_query(
        "SELECT * FROM expenses WHERE username = ?", conn, params=(username,)
    )
    conn.close()
    return expenses

# Initialize table
init_expenses_table()

def app():
    st.title("💰 AI Personal Finance Tracker")

    if "user" not in st.session_state:
        st.warning("Please login first to access features.")
        return

    user = st.session_state["user"]   # ✅ username (string)

    st.subheader("Add New Expense")

    amount = st.number_input("Enter amount (₹)", min_value=1.0, format="%.2f")

    # ✅ Dropdown for category
    category = st.selectbox(
        "Select Category",
        ["Food", "Stationary", "Gym", "Salon", "Other"]
    )

    note = st.text_input("Add a note (optional)")

    # ✅ Date picker
    date = st.date_input("Date of Expense")

    if st.button("Add Expense"):
        add_expense(user, amount, category, note, str(date))
        st.success("Expense added successfully!")

    st.subheader("📊 Expense Summary")
    expenses = get_expenses(user)

    if not expenses.empty:
        st.write("### All Expenses")
        st.dataframe(expenses)

        # ✅ Group by date for bar chart
        chart_data = expenses.groupby("date")["amount"].sum().reset_index()

        chart = (
            alt.Chart(chart_data)
            .mark_bar()
            .encode(x="date:T", y="amount:Q", tooltip=["date", "amount"])
            .properties(width=700, height=400)
        )

        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("No expenses recorded yet.")
