import streamlit as st

from authentication.login import login_page
from authentication.signup import signup_page
from authentication.session_manager import initialize_session

from dashboard.dashboard_home import show_dashboard

st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide"
)

initialize_session()

if not st.session_state["logged_in"]:

    st.title("💰 Smart Finance Tracker")

    option = st.sidebar.selectbox(
        "Select Option",
        ["Login", "Signup"]
    )

    if option == "Login":
        login_page()

    else:
        signup_page()

else:

    show_dashboard()
