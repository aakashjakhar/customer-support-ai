import streamlit as st
from utils.api import register_user


def register_page():

    st.title("📝 Create Account")

    username = st.text_input("Username")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register", use_container_width=True):

        response = register_user(
            username,
            email,
            password
        )

        if response.status_code == 200:

            st.success("Registration Successful!")

            st.session_state.page = "login"

            st.rerun()

        else:
            st.error("Registration Failed")

    st.write("---")

    if st.button("Already have an account? Login", use_container_width=True):

        st.session_state.page = "login"

        st.rerun()