import streamlit as st
import pandas as pd
from datetime import date
import os


def add_expense_page():

    st.title("💸 Add Expense")

    expense = st.number_input(
        "Enter Expense",
        min_value=0
    )

    category = st.selectbox(
        "Expense Category",
        [
            "Food",
            "Shopping",
            "Bills",
            "EMI",
            "Medical",
            "Transport",
            "Entertainment"
        ]
    )

    if st.button("Add Expense"):

        new_data = pd.DataFrame({
            "date": [date.today()],
            "income": [0],
            "expense": [expense],
            "category": [category]
        })

        file_path = "dataset/personal_finance_dataset.csv"

        if os.path.exists(file_path):

            old_df = pd.read_csv(file_path)

            updated_df = pd.concat(
                [old_df, new_data],
                ignore_index=True
            )

        else:

            updated_df = new_data

        updated_df.to_csv(
            file_path,
            index=False
        )

        st.success("Expense Added Successfully ✅")
