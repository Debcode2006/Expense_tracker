import os
import pandas as pd

DATA_FILE = "/mount/data/expenses.csv"


def initialize_storage():
    """
    Ensures the data directory and expenses.csv exist.
    Creates an empty CSV with proper headers if not existing.
    """
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["date", "category", "amount", "description"])
        df.to_csv(DATA_FILE, index=False)


def load_expenses():
    """Loads the expenses CSV as a pandas DataFrame."""
    initialize_storage()
    try:
        return pd.read_csv(DATA_FILE)
    except Exception:
        return pd.DataFrame(columns=["date", "category", "amount", "description"])


def add_expense(date, category, amount, description=""):
    """
    Adds a new expense entry to the CSV file.
    Args:
        date (str): YYYY-MM-DD
        category (str): Expense category
        amount (float): Amount spent
        description (str): Optional description
    """
    df = load_expenses()
    new_entry = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    }

    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)


def clear_all_expenses():
    """Deletes all expense records (used for resetting)."""
    initialize_storage()
    df = pd.DataFrame(columns=["date", "category", "amount", "description"])
    df.to_csv(DATA_FILE, index=False)
