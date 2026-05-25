import streamlit as st
from authentication.google_oauth import google_login

def login_page():

    st.subheader("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if email == "admin@gmail.com" and password == "admin":

            st.session_state["logged_in"] = True

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Credentials")

    st.markdown("---")

    st.subheader("OR")

    google_login()
