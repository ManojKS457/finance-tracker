import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0b1120;
    border-right: 1px solid #1e293b;
}

/* App Title */
.app-title {
    font-size: 42px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 25px;
}

/* Profile Card */
.profile-container {
    background: #071739;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #1e3a5f;
    margin-bottom: 30px;
}

/* User Name */
.user-name {
    font-size: 22px;
    font-weight: 700;
    color: white;
    margin-bottom: 15px;
}

/* User Email */
.user-email {
    font-size: 16px;
    color: #cbd5e1;
}

/* Navigation Title */
.nav-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 20px;
    color: #d1d5db;
}

/* Logout Button */
.logout-btn button {
    width: 100%;
    background: #0f172a !important;
    color: white !important;
    border-radius: 12px !important;
    height: 50px;
    border: 1px solid #334155 !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

.logout-btn button:hover {
    background: #1e293b !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    # App Title
    st.markdown(
        '<div class="app-title">Tracker</div>',
        unsafe_allow_html=True
    )

    # Profile Card
    st.markdown(f"""
    <div class="profile-container">

        <div class="user-name">
            👤 Manoj KS
        </div>

        <div class="user-email">
            📧 manojdab10@gmail.com
        </div>

    </div>
    """, unsafe_allow_html=True)

    # Navigation Title
    st.markdown(
        '<div class="nav-title">Navigation</div>',
        unsafe_allow_html=True
    )

    # Navigation Menu
    page = st.radio(
        "",
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

    st.markdown("<br>", unsafe_allow_html=True)

    # Logout Button
    st.markdown('<div class="logout-btn">', unsafe_allow_html=True)
    st.button("🚪 Logout")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MAIN PAGE ----------------
st.title(page)

if page == "Dashboard":
    st.success("Welcome to your Finance Dashboard!")

elif page == "Add Income":
    st.info("Add your income here.")

elif page == "Add Expense":
    st.warning("Add your expenses here.")

elif page == "Budget Planner":
    st.info("Plan your monthly budget.")

elif page == "Analytics":
    st.info("View financial analytics.")

elif page == "Expense History":
    st.info("See all previous expenses.")

elif page == "Profile":
    st.info("User profile section.")
