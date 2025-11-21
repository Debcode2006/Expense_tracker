import pandas as pd


def get_total_spending(df: pd.DataFrame):
    """Returns total amount spent."""
    if df.empty:
        return 0
    return df["amount"].sum()


def category_wise_summary(df: pd.DataFrame):
    """Returns total spending grouped by category as a DataFrame."""
    if df.empty:
        return pd.DataFrame(columns=["category", "total"])

    summary = df.groupby("category")["amount"].sum().reset_index()
    summary = summary.rename(columns={"amount": "total"})
    return summary


def monthly_summary(df: pd.DataFrame):
    """Returns spending grouped by month (YYYY-MM) as a DataFrame."""
    if df.empty:
        return pd.DataFrame(columns=["month", "total"])

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["month"] = df["date"].dt.to_period("M").astype(str)

    summary = df.groupby("month")["amount"].sum().reset_index()
    summary = summary.rename(columns={"amount": "total"})
    return summary


def get_recent_expenses(df: pd.DataFrame, limit=5):
    """Returns the most recent 'limit' number of expenses."""
    if df.empty:
        return df

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df.sort_values(by="date", ascending=False).tail(limit)
