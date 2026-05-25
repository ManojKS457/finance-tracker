import streamlit as st
import database.models

from authentication.login import login_page
from authentication.signup import signup_page
from authentication.session_manager import initialize_session

from frontend.sidebar import sidebar_menu
from frontend.navbar import navbar

from dashboard.dashboard_home import show_dashboard
from dashboard.analytics_dashboard import analytics_dashboard

from pages.add_income import add_income_page
from pages.add_expense import add_expense_page
from pages.budget_planner import budget_page
from pages.expense_history import expense_history_page
from pages.profile import profile_page

st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide"
)

initialize_session()

# ---------------- AUTH SECTION ---------------- #

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

# ---------------- MAIN APP ---------------- #

else:

    navbar()

    selected = sidebar_menu()

    if selected == "Dashboard":
        show_dashboard()

    elif selected == "Add Income":
        add_income_page()

    elif selected == "Add Expense":
        add_expense_page()

    elif selected == "Budget Planner":
        budget_page()

    elif selected == "Analytics":
        analytics_dashboard()

    elif selected == "Expense History":
        expense_history_page()

    elif selected == "Profile":
        profile_page()