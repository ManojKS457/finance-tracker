import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =========================
# DASHBOARD FUNCTION
# =========================
def show_dashboard():

    st.markdown("# 📊 Finance Dashboard")

    csv_file = "dataset/personal_finance_dataset.csv"

    # =========================
    # CREATE FILE IF NOT EXISTS
    # =========================
    if not os.path.exists(csv_file):

        empty_df = pd.DataFrame(
            columns=["income", "expense", "category"]
        )

        empty_df.to_csv(csv_file, index=False)

    # =========================
    # READ CSV
    # =========================
    df = pd.read_csv(csv_file)

    # =========================
    # CONVERT TO NUMERIC
    # =========================
    df["income"] = pd.to_numeric(
        df["income"],
        errors="coerce"
    ).fillna(0)

    df["expense"] = pd.to_numeric(
        df["expense"],
        errors="coerce"
    ).fillna(0)


    # =========================
    # HANDLE REAL DATA
    # =========================
    if df.empty:

        total_income = 0
        total_expense = 0
        savings = 0
        emi = 0

    else:

        total_income = df["income"].sum()

        total_expense = df["expense"].sum()

        savings = total_income - total_expense

        emi = df[df["category"] == "EMI"]["expense"].sum()

    # =========================
    # METRICS
    # =========================
    st.markdown("## 💰 Financial Overview")

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
            f"₹{emi:,.0f}"
        )

    st.divider()

    # =========================
    # EXPENSE DISTRIBUTION
    # =========================
    expense_df = (
        df.groupby("category")["expense"]
        .sum()
        .reset_index()
    )

    st.subheader("Expense Distribution")

    pie_chart = px.pie(
        expense_df,
        values="expense",
        names="category",
        hole=0.5
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    # =========================
    # BAR CHART
    # =========================
    st.subheader("Expenses By Category")

    bar_chart = px.bar(
        expense_df,
        x="category",
        y="expense",
        color="category"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )
