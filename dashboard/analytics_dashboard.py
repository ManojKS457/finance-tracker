import streamlit as st
import pandas as pd
import plotly.express as px

def analytics_dashboard():

    st.header("📈 Expense Analytics")

    try:

        df = pd.read_csv(
            "dataset/personal_finance_dataset.csv"
        )

    except Exception as e:

        st.error(f"Dataset Error: {e}")

        return

    expense_df = df[df["type"] == "Expense"]

    # ---------------- PIE CHART ---------------- #

    st.subheader("🥧 Expense Distribution")

    pie_fig = px.pie(
        expense_df,
        names="category",
        values="amount",
        title="Expense Distribution"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

    # ---------------- BAR CHART ---------------- #

    st.subheader("📊 Expenses By Category")

    category_expense = expense_df.groupby(
        "category",
        as_index=False
    )["amount"].sum()

    bar_fig = px.bar(
        category_expense,
        x="category",
        y="amount",
        color="category",
        title="Expenses By Category"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

    # ---------------- LINE CHART ---------------- #

    st.subheader("📉 Expense Trend Over Time")

    expense_df["date"] = pd.to_datetime(
        expense_df["date"]
    )

    daily_expense = expense_df.groupby(
        "date",
        as_index=False
    )["amount"].sum()

    line_fig = px.line(
        daily_expense,
        x="date",
        y="amount",
        markers=True,
        title="Daily Expense Trend"
    )

    st.plotly_chart(
        line_fig,
        use_container_width=True
    )

    # ---------------- MONTHLY TREND ---------------- #

    st.subheader("📅 Monthly Expense Analysis")

    expense_df["month"] = expense_df["date"].dt.strftime("%B")

    monthly_expense = expense_df.groupby(
        "month",
        as_index=False
    )["amount"].sum()

    monthly_fig = px.line(
        monthly_expense,
        x="month",
        y="amount",
        markers=True,
        title="Monthly Expense Trend"
    )

    st.plotly_chart(
        monthly_fig,
        use_container_width=True
    )