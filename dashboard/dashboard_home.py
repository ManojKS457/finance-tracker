import streamlit as st
import pandas as pd
import plotly.express as px
import os


def dashboard_page():

    st.title("📊 Finance Dashboard")

    file_path = "dataset/personal_finance_dataset.csv"

    # CHECK IF FILE EXISTS
    if not os.path.exists(file_path):

        st.warning("No financial data available yet.")

        return

    # READ DATA
    df = pd.read_csv(file_path)

    # HANDLE EMPTY DATASET
    if df.empty:

        st.warning("No financial data available yet.")

        return

    # FIX MISSING COLUMNS
    if "income" not in df.columns:
        df["income"] = 0

    if "expense" not in df.columns:
        df["expense"] = 0

    if "category" not in df.columns:
        df["category"] = "Other"

    # CONVERT TO NUMERIC
    df["income"] = pd.to_numeric(
        df["income"],
        errors="coerce"
    ).fillna(0)

    df["expense"] = pd.to_numeric(
        df["expense"],
        errors="coerce"
    ).fillna(0)

    # CALCULATIONS
    total_income = df["income"].sum()

    total_expense = df["expense"].sum()

    savings = total_income - total_expense

    emi_total = df[
        df["category"] == "EMI"
    ]["expense"].sum()

    # METRICS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💰 Total Income",
            f"₹{total_income:,.0f}"
        )

    with col2:
        st.metric(
            "💸 Total Expense",
            f"₹{total_expense:,.0f}"
        )

    with col3:
        st.metric(
            "🏦 Savings",
            f"₹{savings:,.0f}"
        )

    with col4:
        st.metric(
            "🏠 EMI",
            f"₹{emi_total:,.0f}"
        )

    st.divider()

    # EXPENSE DISTRIBUTION
    expense_df = df[df["expense"] > 0]

    if not expense_df.empty:

        st.subheader("Expense Distribution")

        category_expense = (
            expense_df.groupby("category")["expense"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            category_expense,
            names="category",
            values="expense",
            hole=0.5
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # RECENT TRANSACTIONS
    st.subheader("Recent Transactions")

    st.dataframe(
        df.tail(10),
        use_container_width=True
    )
