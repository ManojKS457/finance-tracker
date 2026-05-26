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
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

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
    color: #00c6ff;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 30px;
}

.menu-container {
    background: #050816;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

.stButton > button {
    width: 100%;
    background-color: transparent;
    color: white;
    border: none;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.stButton > button:hover {
    background-color: #0ea5e9;
    color: white;
}

.active-btn {
    background-color: #0ea5e9 !important;
    color: white !important;
}

.user-card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    margin-top: 25px;
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

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR TITLE
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
# MENU CARD
# =========================
st.sidebar.markdown('<div class="menu-container">', unsafe_allow_html=True)

if st.sidebar.button("📊 Dashboard"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("💵 Add Income"):
    st.session_state.page = "Add Income"

if st.sidebar.button("💳 Add Expense"):
    st.session_state.page = "Add Expense"

if st.sidebar.button("🧮 Budget Planner"):
    st.session_state.page = "Budget Planner"

if st.sidebar.button("📈 Analytics"):
    st.session_state.page = "Analytics"

if st.sidebar.button("🕒 Expense History"):
    st.session_state.page = "Expense History"

if st.sidebar.button("👤 Profile"):
    st.session_state.page = "Profile"

st.sidebar.markdown('</div>', unsafe_allow_html=True)

# =========================
# USER CARD
# =========================
st.sidebar.markdown(
    f"""
    <div class="user-card">

        <div class="user-name">
            👤 {st.session_state.user_name}
        </div>

        <div style="margin-top:10px;" class="user-email">
            📧 {st.session_state.user_email}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# LOGOUT BUTTON
# =========================
if st.sidebar.button("🚪 Logout"):

    st.session_state.clear()

    st.rerun()

# =========================
# PAGE ROUTING
# =========================
page = st.session_state.page

if page == "Dashboard":

    st.success(f"Welcome {st.session_state.user_name}")

    show_dashboard()

elif page == "Add Income":

    show_add_income()

elif page == "Add Expense":

    show_add_expense()

elif page == "Budget Planner":

    st.title("🧮 Budget Planner")

    st.info("Budget Planner Page")

elif page == "Analytics":

    st.title("📈 Analytics")

    st.info("Analytics Page")

elif page == "Expense History":

    st.title("🕒 Expense History")

    st.info("Expense History Page")

elif page == "Profile":

    st.title("👤 Profile")

    st.write("Name:", st.session_state.user_name)

    st.write("Email:", st.session_state.user_email)
