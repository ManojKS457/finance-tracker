import streamlit as st
import pandas as pd
import os

# =========================
# ADD INCOME FUNCTION
# =========================
def show_add_income():

    st.markdown("# 💰 Add Income")

    income = st.number_input(
        "Enter Income Amount",
        min_value=0.0,
        step=100.0
    )

    source = st.text_input(
        "Income Source"
    )

    if st.button("Add Income"):

        # =========================
        # CREATE DATAFRAME
        # =========================
        new_data = pd.DataFrame({
            "income": [income],
            "expense": [0],
            "category": [source]
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

        st.success("Income Added Successfully ✅")
