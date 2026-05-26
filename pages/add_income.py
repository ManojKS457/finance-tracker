import streamlit as st
import pandas as pd
from datetime import date
import os


def add_income_page():

    st.title("💰 Add Income")

    income = st.number_input(
        "Enter Income",
        min_value=0
    )

    category = st.selectbox(
        "Income Source",
        [
            "Salary",
            "Freelancing",
            "Business",
            "Other"
        ]
    )

    if st.button("Add Income"):

        new_data = pd.DataFrame({
            "date": [date.today()],
            "income": [income],
            "expense": [0],
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

        st.success("Income Added Successfully ✅")
