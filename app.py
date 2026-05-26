import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Smart Finance Tracker",
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

if "income_data" not in st.session_state:
    st.session_state.income_data = []

if "expense_data" not in st.session_state:
    st.session_state.expense_data = []

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
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 20px;
}

.menu-container {
    background: #050816;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

.user-card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin-bottom: 20px;
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
    margin-top: 20px;
    margin-bottom: 10px;
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

# =========================================
# SIDEBAR
# =========================================
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">💰 Finance Tracker</div>',
        unsafe_allow_html=True
    )

    # USER CARD
    st.markdown(
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

    # LOGOUT
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

# =========================================
# CALCULATIONS
# =========================================
total_income = sum(item["amount"] for item in st.session_state.income_data)

total_expense = sum(item["amount"] for item in st.session_state.expense_data)

savings = total_income - total_expense

# =========================================
# DASHBOARD
# =========================================
if page == "Dashboard":

    st.title("📊 Finance Dashboard")

    st.success(f"Welcome {st.session_state.user_name}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("💰 Total Income", f"₹{total_income}")

    with col2:
        st.metric("💸 Total Expense", f"₹{total_expense}")

    with col3:
        st.metric("🏦 Savings", f"₹{savings}")

    with col4:
        st.metric("🏠 EMI", "₹0")

    st.divider()

    st.subheader("Expense Distribution")

    if len(st.session_state.expense_data) > 0:

        df = pd.DataFrame(st.session_state.expense_data)

        category_totals = (
            df.groupby("category")["amount"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            category_totals,
            names="category",
            values="amount",
            hole=0.5
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("No expense data available.")

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

        st.session_state.income_data.append({
            "source": source,
            "amount": amount,
            "date": str(date)
        })

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
            "Medical",
            "Entertainment"
        ]
    )

    amount = st.number_input(
        "Expense Amount",
        min_value=0
    )

    date = st.date_input("Expense Date")

    if st.button("Add Expense"):

        st.session_state.expense_data.append({
            "category": category,
            "amount": amount,
            "date": str(date)
        })

        st.success("Expense Added Successfully")

# =========================================
# BUDGET PLANNER
# =========================================
elif page == "Budget Planner":

    st.header("📋 Budget Planner")

    budget = st.number_input(
        "Enter Monthly Budget",
        min_value=0
    )

    if st.button("Save Budget"):

        st.success("Budget Saved Successfully")

# =========================================
# ANALYTICS
# =========================================
elif page == "Analytics":

    st.header("📈 Analytics")

    st.info("Analytics will appear after adding financial data.")

# =========================================
# EXPENSE HISTORY
# =========================================
elif page == "Expense History":

    st.header("🕒 Expense History")

    if len(st.session_state.expense_data) > 0:

        df = pd.DataFrame(st.session_state.expense_data)

        st.dataframe(df)

    else:
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
