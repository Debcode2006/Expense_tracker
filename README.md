# Expense Tracker

A lightweight Streamlit application for recording, storing, and analysing personal expenses. Transactions are persisted in CSV storage and summarized through tables and interactive charts.

## Features

- Add expenses with date, category, amount, and description
- View stored transactions
- Calculate total spending
- Analyse spending by category
- Analyse spending by month
- Visualize spending with Plotly charts
- Clear stored expense data from the application

## Architecture

```text
Streamlit UI
    ↓
Application Logic
    ↓
Data Handler + Analytics Modules
    ↓
CSV Storage
```

The application separates data handling and analytics from the Streamlit entry point.

## Repository Structure

```text
.
├── app.py
├── data/
│   └── expenses.csv
├── modules/
│   ├── data_handler.py
│   └── analytics.py
├── requirements.txt
└── README.md
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Tech Stack

**Python · Streamlit · Pandas · Plotly**

## Data Storage

Transactions are stored in `data/expenses.csv`. The application reads the CSV for analysis and writes new transactions through the data-handling module.

## Author

Debanjan Sarkar