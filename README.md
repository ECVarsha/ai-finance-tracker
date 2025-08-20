# ai-finance-tracker
An AI-powered personal finance dashboard to help you track expenses, analyze spending patterns, and gain smart insights.
# 💸 AI-powered Personal Finance Tracker  

An **AI-powered personal finance tracking system** built with **Streamlit, SQLite/SQLAlchemy, and Python**.  
Track expenses, visualize spending patterns, and get AI-powered insights into your financial habits.  

---

## 🚀 Features  

- 🔑 **User Authentication** (Sign up & Login with secure password hashing)  
- 📝 **Expense Tracking** (amount, category, note, date)  
- 📊 **Interactive Dashboards** (charts & summaries with Altair/Matplotlib)  
- 🤖 **AI-powered Insights** :  
  - Predictive analytics – forecast future spending  
  - Smart categorization – auto-detect expense categories using NLP  
  - Anomaly detection – flag unusual or overspending behavior  
- 🗄 **SQLite + SQLAlchemy** for reliable database handling  

---

## 📂 Project Structure  

finance-tracker/
│── app.py              # Main entry Streamlit app (handles navigation)
│
├── pages/              # Streamlit multipage support
│   │── home.py         # Dashboard page
│   │── login.py        # Login page
│   │── signup.py       # (Optional) Signup page
│
├── db/                 # Database logic
│   │── database.py     # SQLAlchemy ORM models & functions
│   │── init_db.py      # Initialize database (tables setup)
│   │── check_schema.py # Debug: check DB schema
│   │── finance.db      # Main database (unify here, ignore other .db files)
│
├── data/               # (Optional) Store exported CSVs, backups, etc.
│   │── expenses.db     # old db - remove after migration
│   │── users.db        # old db - remove after migration
│   │── user.db         # old db - remove after migration
│
├── utils/              # Helper functions
│   │── security.py     # password hashing / session utils
│   │── ai.py           # AI-powered insights (prediction, NLP categorization)
│
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignore .db, __pycache__, venv, etc.

## ## How to Run It

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```







