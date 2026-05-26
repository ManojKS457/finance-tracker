import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💰",
    layout="wide"
)

# =========================================
# SESSION STATE
# =========================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

if "user_name" not in st.session_state:
    st.session_state.user_name = "Manoj KS"

if "user_email" not in st.session_state:
    st.session_state.user_email = "manojdab10@gmail.com"

# =========================================
# CUSTOM CSS
# =========================================
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
    margin-bottom: 20px;
}

.user-card {
    background: #0f172a;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin-bottom: 25px;
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
    font-weight: bold;
    margin-bottom: 10px;
}

.stRadio > div {
    gap: 10px;
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

.metric-card {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">💰 Finance Tracker</div>',
        unsafe_allow_html=True
    )

    # USER CARD
    st.sidebar.markdown(
        f"""
        <div class="user-card">

            <div class="user-name">
                👤 {st.session_state.user_name}
            </div>

            <div class="user-email">
                📧 {st.session_state.user_email}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

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

    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

# =========================================
# MAIN CONTENT
# =========================================
st.title("📊 Finance Dashboard")

st.success(f"Welcome {st.session_state.user_name}")

# =========================================
# DASHBOARD
# =========================================
if page == "Dashboard":

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

    st.subheader("📈 Expense Distribution")

    st.info("No financial data available yet. Add income and expenses to see analytics.")

# =========================================
# ADD INCOME
# =========================================
elif page == "Add Income":

    st.header("💰 Add Income")

    source = st.text_input("Income Source")

    amount = st.number_input(
        "Amount",
        min_value=0
    )

    date = st.date_input("Date")

    if st.button("Add Income"):

        st.success("Income Added Successfully")

# =========================================
# ADD EXPENSE
# =========================================
elif page == "Add Expense":

    st.header("💸 Add Expense")

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Transport",
            "Shopping",
            "Bills",
            "Medical"
        ]
    )

    amount = st.number_input(
        "Expense Amount",
        min_value=0
    )

    date = st.date_input("Expense Date")

    if st.button("Add Expense"):

        st.success("Expense Added Successfully")

# =========================================
# BUDGET PLANNER
# =========================================
elif page == "Budget Planner":

    st.header("📋 Budget Planner")

    monthly_budget = st.number_input(
        "Enter Monthly Budget",
        min_value=0
    )

    if st.button("Save Budget"):

        st.success("Budget Saved Successfully")

# =========================================
# ANALYTICS
# =========================================
elif page == "Analytics":

    st.header("📊 Analytics")

    st.info("Analytics will appear after adding data.")

# =========================================
# EXPENSE HISTORY
# =========================================
elif page == "Expense History":

    st.header("🕒 Expense History")

    st.info("No expense history available.")

# =========================================
# PROFILE
# =========================================
elif page == "Profile":

    st.header("👤 User Profile")

    st.write("### Name")
    st.write(st.session_state.user_name)

    st.write("### Email")
    st.write(st.session_state.user_email)
