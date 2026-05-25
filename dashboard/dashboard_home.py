import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard():

    st.title("📊 Finance Dashboard")

    try:

        df = pd.read_csv(
            "dataset/personal_finance_dataset.csv"
        )

        total_income = df["income"].sum()

        total_expense = df["expense"].sum()

        savings = total_income - total_expense

        emi_total = df[df["category"] == "EMI"]["expense"].sum()

        # KPI CARDS
        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "💰 Total Income",
            f"₹{total_income:,.0f}"
        )

        col2.metric(
            "💸 Total Expense",
            f"₹{total_expense:,.0f}"
        )

        col3.metric(
            "🏦 Savings",
            f"₹{savings:,.0f}"
        )

        col4.metric(
            "🏠 EMI",
            f"₹{emi_total:,.0f}"
        )

        st.divider()

        # PIE CHART
        st.subheader("Expense Distribution")

        expense_category = (
            df.groupby("category")["expense"]
            .sum()
            .reset_index()
        )

        pie_fig = px.pie(
            expense_category,
            values="expense",
            names="category",
            hole=0.4
        )

        st.plotly_chart(
            pie_fig,
            use_container_width=True
        )

        # LINE CHART
        st.subheader("Income vs Expense")

        line_fig = px.line(
            df,
            x="date",
            y=["income", "expense"],
            markers=True
        )

        st.plotly_chart(
            line_fig,
            use_container_width=True
        )

        # BAR CHART
        st.subheader("Expenses by Category")

        bar_fig = px.bar(
            expense_category,
            x="category",
            y="expense",
            color="category"
        )

        st.plotly_chart(
            bar_fig,
            use_container_width=True
        )

        # ALERTS
        monthly_limit = 50000

        if total_expense > monthly_limit:

            st.error(
                "⚠️ Monthly Expense Limit Exceeded!"
            )

        else:

            st.success(
                "✅ Expenses are within limit"
            )

    except Exception as e:

        st.error(f"Dashboard Error: {e}")
