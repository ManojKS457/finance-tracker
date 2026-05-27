import streamlit as st
import pandas as pd
import os

# =========================
# ADD EXPENSE FUNCTION
# =========================
def add_expense_page():

    st.markdown("# 💳 Add Expense")

    expense = st.number_input(
        "Enter Expense Amount",
        min_value=0.0,
        step=100.0
    )

    category = st.text_input(
        "Expense Category"
    )

    if st.button("Add Expense"):

        file_path = "dataset/user_finance_data.csv"

        # =========================
        # CREATE FILE IF NOT EXISTS
        # =========================
        if not os.path.exists(file_path):

            empty_df = pd.DataFrame(
                columns=["income", "expense", "category"]
            )

            empty_df.to_csv(
                file_path,
                index=False
            )

        # =========================
        # CREATE NEW ENTRY
        # =========================
        new_data = pd.DataFrame({
            "income": [0],
            "expense": [expense],
            "category": [category]
        })

        # =========================
        # SAVE TO CSV
        # =========================
        new_data.to_csv(
            file_path,
            mode="a",
            header=False,
            index=False
        )

        # =========================
        # UPDATE SESSION
        # =========================
        st.session_state.data_initialized = True

        st.success("Expense Added Successfully ✅")
