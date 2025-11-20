# Expense Tracker (Python + Streamlit)

A simple **Expense Tracker** built using **Python**, **Streamlit**, **Pandas**, and **Plotly**. Tracks daily expenses, displays summaries, and shows charts.

---

## Features

* Add expenses (date, category, amount, description)
* View all expenses in a table
* Total spending summary
* Category-wise pie chart
* Month-wise spending bar chart
* CSV-based storage

---

## Folder Structure

```
expense_tracker/
│── app.py
│── data/
│   └── expenses.csv
│── modules/
│   ├── data_handler.py
│   └── analytics.py
│── requirements.txt
└── README.md
```

---

## Installation

```
pip install -r requirements.txt
```

Or:

```
python -m pip install -r requirements.txt
```

---

## Run the App

```
streamlit run app.py
```

Or:

```
python -m streamlit run app.py
```

---

## Requirements

```
streamlit
pandas
plotly
```

---

## Description

All expenses are stored in **data/expenses.csv**. You can add, view, and analyze your spending visually through the Streamlit UI.

---

## Reset Data

Use the **Clear All Expenses** button in the UI to wipe the CSV.

---

## Author

Debanjan Sarkar, Madhurima Das