import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/auth"

def google_login():

    if not GOOGLE_CLIENT_ID:
        st.warning("Google OAuth not configured")
        return

    oauth = OAuth2Session(
        GOOGLE_CLIENT_ID,
        GOOGLE_CLIENT_SECRET,
        scope="openid email profile",
        redirect_uri=REDIRECT_URI
    )

    authorization_url, state = oauth.create_authorization_url(
        AUTHORIZATION_ENDPOINT
    )

    st.link_button(
        "🔵 Continue with Google",
        authorization_url,
        use_container_width=True
    )
