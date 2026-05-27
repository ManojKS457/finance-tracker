import streamlit as st

from authentication.login import login_page
from authentication.signup import signup_page
from authentication.session_manager import initialize_session

from frontend.sidebar import sidebar_menu

from dashboard.dashboard_home import show_dashboard
from dashboard.analytics_dashboard import analytics_dashboard

from pages.add_income import add_income_page
from pages.add_expense import add_expense_page
from pages.budget_planner import budget_page
from pages.expense_history import expense_history_page
from pages.profile import profile_page


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide"
)

# =========================================
# SESSION INITIALIZATION
# =========================================

initialize_session()

# =========================================
# INITIALIZE USER DATA
# =========================================

if "income_data" not in st.session_state:
    st.session_state["income_data"] = []

if "expense_data" not in st.session_state:
    st.session_state["expense_data"] = []

if "dashboard_income" not in st.session_state:
    st.session_state["dashboard_income"] = 0

if "dashboard_expense" not in st.session_state:
    st.session_state["dashboard_expense"] = 0

if "dashboard_savings" not in st.session_state:
    st.session_state["dashboard_savings"] = 0


# =========================================
# LOGIN / SIGNUP
# =========================================

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


# =========================================
# MAIN APPLICATION
# =========================================

else:

    try:

        selected = sidebar_menu()

        st.success(
            f"Welcome {st.session_state.get('user_name', 'User')}"
        )

        # =========================================
        # CALCULATE LIVE VALUES FROM USER INPUTS
        # =========================================

        total_income = sum(
            item["amount"]
            for item in st.session_state["income_data"]
        )

        total_expense = sum(
            item["amount"]
            for item in st.session_state["expense_data"]
        )

        savings = total_income - total_expense

        # =========================================
        # STORE VALUES FOR DASHBOARD
        # =========================================

        st.session_state["dashboard_income"] = total_income
        st.session_state["dashboard_expense"] = total_expense
        st.session_state["dashboard_savings"] = savings

        # =========================================
        # NAVIGATION
        # =========================================

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

    except Exception as e:

        st.error(f"Dashboard Error: {e}")
