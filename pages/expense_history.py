import streamlit as st
import pandas as pd

def expense_history_page():

    st.header("📜 Expense History")

    try:

        df = pd.read_csv(
            "dataset/personal_finance_dataset.csv"
        )

        st.dataframe(df)

    except Exception as e:

        st.error(f"Dataset Error: {e}")