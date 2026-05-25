import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/auth"

TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"

USER_INFO = "https://www.googleapis.com/oauth2/v1/userinfo"


def google_login():

    oauth = OAuth2Session(
        GOOGLE_CLIENT_ID,
        GOOGLE_CLIENT_SECRET,
        scope="openid email profile",
        redirect_uri=REDIRECT_URI
    )

    query_params = st.query_params

    # ---------------- HANDLE CALLBACK ---------------- #

    if "code" in query_params:

        code = query_params["code"]

        token = oauth.fetch_token(
            TOKEN_ENDPOINT,
            code=code
        )

        response = oauth.get(
            USER_INFO,
            token=token
        )

        user_info = response.json()

        st.session_state["logged_in"] = True

        st.session_state["user_email"] = user_info.get("email")

        st.session_state["user_name"] = user_info.get("name")

        st.success(
            f"Welcome {user_info.get('name')}"
        )

        st.query_params.clear()

        st.rerun()

    # ---------------- SHOW LOGIN BUTTON ---------------- #

    authorization_url, state = oauth.create_authorization_url(
        AUTHORIZATION_ENDPOINT
    )

    st.link_button(
        "🔵 Continue with Google",
        authorization_url,
        use_container_width=True
    )
