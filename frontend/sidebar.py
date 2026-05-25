import streamlit as st
from streamlit_option_menu import option_menu

def sidebar_menu():

    with st.sidebar:

        selected = option_menu(
            "Finance Tracker",
            [
                "Dashboard",
                "Add Income",
                "Add Expense",
                "Budget Planner",
                "Analytics",
                "Expense History",
                "Profile"
            ],
            icons=[
                "speedometer2",
                "cash-stack",
                "credit-card",
                "calculator",
                "bar-chart",
                "clock-history",
                "person"
            ],
            menu_icon="list",
            default_index=0
        )

    return selected