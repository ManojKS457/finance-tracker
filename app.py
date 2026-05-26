import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Smart Finance Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
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

if "user_email" not in st.session_state:
    st.session_state.user_email = "manojdab10@gmail.com"

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

section[data-testid="stSidebar"] {
    background-color: #1e1e2f;
    width: 320px !important;
}

.sidebar-title {
    font-size: 34px;
    font-weight: bold;
    color: #00c6ff;
    margin-bottom: 20px;
}

.user-card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 25px;
    border: 1px solid #2d3748;
}

.user-name {
    color: white;
    font-size: 22px;
    font-weight: bold;
}

.user-email {
    color: #9ca3af;
    font-size: 15px;
}

.main-title {
    font-size: 50px;
    font-weight: bold;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR HEADER
# =========================
st.sidebar.markdown(
    """
    <div class="sidebar-title">
    💰 Finance Tracker
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# USER CARD AT TOP
# =========================
st.sidebar.markdown(
    f"""
    <div class="user-card">
        <div class="user-name">
            👤 {st.session_state.user_name}
        </div>

        <br>

        <div class="user-email">
            📧 {st.session_state.user_email}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# MENU
# =========================
menu = st.sidebar.radio(
    "Navigation",
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
# LOGOUT
# =========================
st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout"):

    st.session_state.clear()

    st.rerun()

# =========================
# ROUTING
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

    st.write("Email:", st.session_state.user_email)
