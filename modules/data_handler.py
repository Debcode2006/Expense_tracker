import os
import pandas as pd
import streamlit as st

# Detect if running on Streamlit Cloud
def get_data_file():
    if "mount" in os.getcwd().lower():  # Cloud environment
        data_dir = "/mount/data"
    else:  # Local machine
        data_dir = "data"

    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, "expenses.csv")


DATA_FILE = get_data_file()


def initialize_storage():
    """Creates expenses.csv if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["date", "category", "amount", "description"])
        df.to_csv(DATA_FILE, index=False)


def load_expenses():
    initialize_storage()
    try:
        return pd.read_csv(DATA_FILE)
    except:
        return pd.DataFrame(columns=["date", "category", "amount", "description"])


def add_expense(date, category, amount, description=""):
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
    df = pd.DataFrame(columns=["date", "category", "amount", "description"])
    df.to_csv(DATA_FILE, index=False)
