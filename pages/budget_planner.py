import streamlit as st

def budget_page():

    st.header("📊 Budget Planner")

    income = st.number_input(
        "Monthly Income",
        min_value=0
    )

    emi = st.number_input(
        "Monthly EMI",
        min_value=0
    )

    savings = st.number_input(
        "Savings Goal",
        min_value=0
    )

    limit = income - (emi + savings)

    st.success(
        f"Monthly Expense Limit: ₹ {limit}"
    )

    if limit < 0:

        st.error("Expenses exceed income")