import streamlit as st
import pandas as pd
from datetime import datetime

def add_expense_page():

    st.header("➖ Add Expense")

    category = st.selectbox(
        "Expense Category",
        [
            "Food",
            "Shopping",
            "Transport",
            "Bills",
            "EMI",
            "Medical",
            "Entertainment"
        ]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    if st.button("Add Expense"):

        new_data = pd.DataFrame({

            "date": [datetime.now().strftime("%Y-%m-%d")],
            "type": ["Expense"],
            "category": [category],
            "amount": [amount]

        })

        df = pd.read_csv(
            "dataset/personal_finance_dataset.csv"
        )

        df = pd.concat(
            [df, new_data],
            ignore_index=True
        )

        df.to_csv(
            "dataset/personal_finance_dataset.csv",
            index=False
        )

        st.success("Expense Added Successfully")