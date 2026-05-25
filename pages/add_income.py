import streamlit as st
import pandas as pd
from datetime import datetime

def add_income_page():

    st.header("➕ Add Income")

    source = st.selectbox(
        "Income Source",
        [
            "Salary",
            "Freelancing",
            "Bonus",
            "Investments"
        ]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    if st.button("Add Income"):

        new_data = pd.DataFrame({

            "date": [datetime.now().strftime("%Y-%m-%d")],
            "type": ["Income"],
            "category": [source],
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

        st.success("Income Added Successfully")