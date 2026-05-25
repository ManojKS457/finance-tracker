import streamlit as st
from streamlit_option_menu import option_menu


def sidebar_menu():

    with st.sidebar:

        st.markdown(
            """
            <h1 style='color:#18c1ff;'>
            💰 Finance Tracker
            </h1>
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
                "house-fill",
                "cash-stack",
                "credit-card",
                "wallet2",
                "bar-chart-fill",
                "clock-history",
                "person-circle"
            ],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {
                    "padding": "10px",
                    "background-color": "#050816",
                    "border-radius": "15px"
                },

                "icon": {
                    "color": "#00c3ff",
                    "font-size": "22px"
                },

                "nav-link": {
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "8px",
                    "--hover-color": "#111827",
                    "color": "white",
                    "border-radius": "10px"
                },

                "nav-link-selected": {
                    "background-color": "#18c1ff",
                    "color": "white",
                    "font-weight": "bold"
                }
            }
        )

        st.divider()

        st.markdown(
            f"""
            ### 👤 User
            **{st.session_state.get('user_name', 'User')}**
            """
        )

        st.markdown(
            f"""
            📧 {st.session_state.get('user_email', '')}
            """
        )

        st.divider()

        # LOGOUT BUTTON
        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.clear()

            st.rerun()

    return selected
