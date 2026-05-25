import streamlit as st

def logout():

    st.session_state["logged_in"] = False

    st.success("Logged Out Successfully")