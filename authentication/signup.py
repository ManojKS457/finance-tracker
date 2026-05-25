import streamlit as st

def signup_page():

    st.subheader("📝 Signup")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Create Account"):

        if password != confirm_password:

            st.error("Passwords do not match")

        else:

            st.success("Account Created Successfully")