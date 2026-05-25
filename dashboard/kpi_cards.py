import streamlit as st

def show_kpi(title, value):

    st.metric(title, value)