import streamlit as st

def check_expense_limit(total_expense, limit):

    if total_expense > limit:

        st.error("⚠️ Expense Limit Exceeded")

    elif total_expense > limit * 0.8:

        st.warning("⚠️ Approaching Expense Limit")

    else:

        st.success("✅ Expenses Under Control")