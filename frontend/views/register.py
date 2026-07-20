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

        if not username or not email or not password:
            st.warning("Please fill in all fields.")
            return

        status_code, data = register_user(
            username,
            email,
            password
        )

        if status_code in [200, 201]:

            st.success("Registration successful!")

            st.session_state.page = "login"
            st.rerun()

        else:
            error_message = data.get(
                "detail",
                "Registration failed"
            )
            st.error(error_message)

    st.write("---")

    if st.button(
        "Already have an account? Login",
        use_container_width=True
    ):
        st.session_state.page = "login"
        st.rerun()