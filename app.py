import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Smart Finance Tracker",
    page_icon="💰",
    layout="wide"
)

# =========================
# IMPORT PAGES
# =========================
from dashboard.dashboard_home import show_dashboard

from pages.add_income import show_add_income

from pages.add_expense import show_add_expense

# =========================
# LOGIN CHECK
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

if "user_name" not in st.session_state:
    st.session_state.user_name = "Manoj KS"

# =========================
# SIDEBAR
# =========================
st.sidebar.markdown("# 💰 Finance Tracker")

menu = st.sidebar.radio(
    "Select Option",
    [
        "Dashboard",
        "Add Income",
        "Add Expense"
    ]
)

# =========================
# USER INFO
# =========================
st.sidebar.markdown("---")

st.sidebar.markdown("## 👤 User")

st.sidebar.write(st.session_state.user_name)

# =========================
# LOGOUT BUTTON
# =========================
if st.sidebar.button("🚪 Logout"):

    st.session_state.clear()

    st.rerun()

# =========================
# PAGE ROUTING
# =========================
if menu == "Dashboard":

    st.success(f"Welcome {st.session_state.user_name}")

    show_dashboard()

elif menu == "Add Income":

    show_add_income()

elif menu == "Add Expense":

    show_add_expense()
