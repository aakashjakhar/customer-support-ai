import streamlit as st

from views.login import login_page
from views.register import register_page
from views.chat import chat_page

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Customer Support AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "login"

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = ""

# -----------------------------
# Page Routing
# -----------------------------

if st.session_state.page == "login":
    login_page()

elif st.session_state.page == "register":
    register_page()

elif st.session_state.page == "chat":
    chat_page()