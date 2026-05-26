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
# SESSION STATE
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

if "user_name" not in st.session_state:
    st.session_state.user_name = "Manoj KS"

# =========================
# SIDEBAR
# =========================
st.sidebar.markdown(
    """
    # 💰 Finance Tracker
    """
)

# =========================
# MENU
# =========================
menu = st.sidebar.radio(
    "Select Option",
    [
        "Dashboard",
        "Add Income",
        "Add Expense",
        "Budget Planner",
        "Analytics",
        "Expense History",
        "Profile"
    ]
)

# =========================
# USER SECTION
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

elif menu == "Budget Planner":

    st.title("📋 Budget Planner")

    st.info("Budget Planner Page")

elif menu == "Analytics":

    st.title("📊 Analytics")

    st.info("Analytics Page")

elif menu == "Expense History":

    st.title("📜 Expense History")

    st.info("Expense History Page")

elif menu == "Profile":

    st.title("👤 Profile")

    st.write("Name:", st.session_state.user_name)
