# database.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

# -------------------
# DATABASE SETUP
# -------------------
DATABASE_URL = "sqlite:///users.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# -------------------
# TABLES
# -------------------
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    note = Column(String, nullable=True)
    category = Column(String, nullable=False)
    date = Column(String, nullable=False)   # YYYY-MM-DD as string


# Create tables
Base.metadata.create_all(bind=engine)

# -------------------
# FUNCTIONS
# -------------------
def create_user(username, password):
    session = SessionLocal()
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    session.close()


def get_user(username, password):
    session = SessionLocal()
    user = session.query(User).filter_by(username=username, password=password).first()
    session.close()
    return user


def add_expense(username, amount, note, category, expense_date=None):
    session = SessionLocal()
    if not expense_date:
        expense_date = str(date.today())  # default = today
    expense = Expense(
        username=username,
        amount=amount,
        note=note,
        category=category,
        date=str(expense_date)
    )
    session.add(expense)
    session.commit()
    session.close()


def get_expenses(username):
    session = SessionLocal()
    expenses = session.query(Expense).filter_by(username=username).all()
    session.close()
    return expenses
