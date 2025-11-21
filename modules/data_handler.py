import os
import pandas as pd

# Detect Streamlit Cloud environment
def get_data_file():
    is_cloud = "STREAMLIT_RUNTIME" in os.environ

    if is_cloud:
        data_dir = "/mount/data"
    else:
        data_dir = "data"

    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, "expenses.csv")


DATA_FILE = get_data_file()


def initialize_storage():
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
