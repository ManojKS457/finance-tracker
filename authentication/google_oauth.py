import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
from dotenv import load_dotenv
import requests
import os

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
USER_INFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"


def google_login():

    oauth = OAuth2Session(
        GOOGLE_CLIENT_ID,
        GOOGLE_CLIENT_SECRET,
        scope="openid email profile",
        redirect_uri=REDIRECT_URI
    )

    query_params = st.query_params

    # GOOGLE CALLBACK
    if "code" in query_params:

        try:

            code = query_params["code"]

            token = oauth.fetch_token(
                TOKEN_ENDPOINT,
                code=code
            )

            access_token = token["access_token"]

            headers = {
                "Authorization": f"Bearer {access_token}"
            }

            response = requests.get(
                USER_INFO_URL,
                headers=headers
            )

            user_info = response.json()

            st.session_state["logged_in"] = True

            st.session_state["user_name"] = user_info.get(
                "name",
                "Google User"
            )

            st.session_state["user_email"] = user_info.get(
                "email",
                ""
            )

            st.query_params.clear()

            st.rerun()

        except Exception as e:

            st.error(f"Google Login Failed: {e}")

    authorization_url, state = oauth.create_authorization_url(
        AUTHORIZATION_ENDPOINT
    )

    st.link_button(
        "🔵 Continue with Google",
        authorization_url,
        use_container_width=True
    )
