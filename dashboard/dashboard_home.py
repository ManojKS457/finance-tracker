import streamlit as st
import pandas as pd

def show_dashboard():

    st.header("📊 Dashboard")

    try:

        df = pd.read_csv(
            "dataset/personal_finance_dataset.csv"
        )

    except Exception as e:

        st.error(f"Dataset Error: {e}")

        return

    income_df = df[df["type"] == "Income"]

    expense_df = df[df["type"] == "Expense"]

    total_income = income_df["amount"].sum()

    total_expense = expense_df["amount"].sum()

    savings = total_income - total_expense

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "💵 Total Income",
        f"₹ {total_income:,.2f}"
    )

    col2.metric(
        "💸 Total Expense",
        f"₹ {total_expense:,.2f}"
    )

    col3.metric(
        "💰 Savings",
        f"₹ {savings:,.2f}"
    )

    st.subheader("Recent Transactions")

    st.dataframe(df.tail(10))