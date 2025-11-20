import streamlit as st
import pandas as pd
from modules.data_handler import load_expenses, add_expense, clear_all_expenses
from modules.analytics import (
    get_total_spending,
    category_wise_summary,
    monthly_summary,
    get_recent_expenses,
)
import plotly.express as px

# ---------------------------
# Streamlit App
# ---------------------------
st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("💰 Expense Tracker")

# Load existing data
df = load_expenses()

# ---------------------------
# Add New Expense
# ---------------------------
st.header("➕ Add New Expense")
with st.form("add_expense_form"):
    col1, col2, col3, col4 = st.columns(4)

    date = col1.date_input("Date")
    category = col2.selectbox(
        "Category", ["Food", "Travel", "Shopping", "Bills", "Other"]
    )
    amount = col3.number_input("Amount", min_value=0.0, step=0.5)
    description = col4.text_input("Description (optional)")

    submitted = st.form_submit_button("Add Expense")
    if submitted:
        add_expense(str(date), category, amount, description)
        st.success("Expense added successfully!")
        st.experimental_rerun()

# ---------------------------
# Dashboard Overview
# ---------------------------
st.header("📊 Dashboard Overview")

colA, colB, colC = st.columns(3)

with colA:
    st.subheader("Total Spending")
    st.metric("₹", get_total_spending(df))

with colB:
    st.subheader("Most Recent Expenses")
    st.dataframe(get_recent_expenses(df))

with colC:
    st.subheader("Category Breakdown")
    cat_summary = category_wise_summary(df)
    if not cat_summary.empty:
        fig = px.pie(cat_summary, names="category", values="total")
        st.plotly_chart(fig)

# ---------------------------
# Monthly Summary Chart
# ---------------------------
st.subheader("📅 Monthly Spending Trend")
month_summary = monthly_summary(df)

if not month_summary.empty:
    fig2 = px.bar(month_summary, x="month", y="total", title="Monthly Expenses")
    st.plotly_chart(fig2)

# ---------------------------
# View All Expenses
# ---------------------------
st.header("📄 All Expenses")
st.dataframe(df)

# ---------------------------
# Reset Option
# ---------------------------
st.warning("Be careful: This will delete all stored expenses.")
if st.button("Clear All Expenses"):
    clear_all_expenses()
    st.success("All expenses cleared!")
    st.experimental_rerun()