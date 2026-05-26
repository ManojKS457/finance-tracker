import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide"
)

# ==========================================
# SESSION STATE
# ==========================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

if "user_name" not in st.session_state:
    st.session_state.user_name = "Manoj KS"

if "user_email" not in st.session_state:
    st.session_state.user_email = "manojdab10@gmail.com"

# ==========================================
# SIDEBAR CSS
# ==========================================
st.markdown("""
<style>

section[data-testid="stSidebar"] {
    background-color: #1e1e2f;
    width: 320px !important;
}

.sidebar-title {
    color: #00c6ff;
    font-size: 34px;
    font-weight: bold;
    margin-bottom: 25px;
}

.user-card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    border: 1px solid #2d3748;
}

.user-name {
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.user-email {
    color: #cbd5e1;
    font-size: 16px;
    margin-top: 10px;
    word-break: break-word;
}

.nav-title {
    color: #cbd5e1;
    font-size: 20px;
    margin-top: 25px;
    margin-bottom: 10px;
    font-weight: bold;
}

.stRadio > div {
    gap: 12px;
}

.stButton > button {
    width: 100%;
    background-color: #0f172a;
    color: white;
    border: 1px solid #334155;
    padding: 12px;
    border-radius: 10px;
    font-size: 18px;
}

.stButton > button:hover {
    background-color: #0ea5e9;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">💰 Finance Tracker</div>',
        unsafe_allow_html=True
    )

    # USER CARD
    st.markdown(f"""
    <div class="user-card">

        <div class="user-name">
            👤 {st.session_state.user_name}
        </div>

        <div class="user-email">
            📧 {st.session_state.user_email}
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="nav-title">Navigation</div>',
        unsafe_allow_html=True
    )

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

    # LOGOUT BUTTON
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

# ==========================================
# MAIN DASHBOARD
# ==========================================
st.title("📊 Finance Dashboard")

st.success(f"Welcome {st.session_state.user_name}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Income", "₹0")

with col2:
    st.metric("💸 Total Expense", "₹0")

with col3:
    st.metric("🏦 Savings", "₹0")

with col4:
    st.metric("🏠 EMI", "₹0")

st.divider()

if page == "Dashboard":
    st.subheader("Dashboard")
    st.info("No financial data available yet.")

elif page == "Add Income":
    st.subheader("Add Income")

    source = st.text_input("Income Source")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Add Income"):
        st.success("Income Added Successfully")

elif page == "Add Expense":
    st.subheader("Add Expense")

    category = st.selectbox(
        "Category",
        ["Food", "Transport", "Shopping", "Bills"]
    )

    amount = st.number_input("Expense Amount", min_value=0)

    if st.button("Add Expense"):
        st.success("Expense Added Successfully")

elif page == "Budget Planner":
    st.subheader("Budget Planner")
    st.info("Budget Planner Coming Soon")

elif page == "Analytics":
    st.subheader("Analytics")
    st.info("Analytics Coming Soon")

elif page == "Expense History":
    st.subheader("Expense History")
    st.info("No Expense History Available")

elif page == "Profile":
    st.subheader("Profile")

    st.write("### Name")
    st.write(st.session_state.user_name)

    st.write("### Email")
    st.write(st.session_state.user_email)
