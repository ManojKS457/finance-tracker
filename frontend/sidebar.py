import streamlit as st
from streamlit_option_menu import option_menu


def sidebar_menu():

    with st.sidebar:

        st.markdown(
            """
            <h2 style='color:#00BFFF;'>
            💰 Finance Tracker
            </h2>
            """,
            unsafe_allow_html=True
        )

        selected = option_menu(
            menu_title=None,

            options=[
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
                "person-circle"
            ],

            default_index=0,

            styles={

                "container": {
                    "padding": "5!important",
                    "background-color": "#0E1117",
                },

                "icon": {
                    "color": "#00BFFF",
                    "font-size": "18px",
                },

                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#262730",
                },

                "nav-link-selected": {
                    "background-color": "#00BFFF",
                    "color": "white",
                },
            }
        )

    return selected
