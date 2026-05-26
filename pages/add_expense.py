import streamlit as st
import pandas as pd
import os

# =========================
# ADD EXPENSE FUNCTION
# =========================
def add_expense_page():

    st.markdown("# 💸 Add Expense")

    expense = st.number_input(
        "Enter Expense Amount",
        min_value=0.0,
        step=100.0
    )

    category = st.selectbox(
        "Select Category",
        [
            "Food",
            "Shopping",
            "Bills",
            "Transport",
            "Medical",
            "Entertainment",
            "EMI"
        ]
    )

    if st.button("Add Expense"):

        # =========================
        # CREATE DATAFRAME
        # =========================
        new_data = pd.DataFrame({
            "income": [0],
            "expense": [expense],
            "category": [category]
        })

        file_path = "dataset/personal_finance_dataset.csv"

        # =========================
        # CREATE FILE IF NOT EXISTS
        # =========================
        if not os.path.exists(file_path):

            new_data.to_csv(
                file_path,
                index=False
            )

        else:

            new_data.to_csv(
                file_path,
                mode="a",
                header=False,
                index=False
            )

        # =========================
        # ENABLE DASHBOARD DATA
        # =========================
        st.session_state.data_initialized = True

        st.success("Expense Added Successfully ✅")
