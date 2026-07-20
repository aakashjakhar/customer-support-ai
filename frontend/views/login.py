import streamlit as st
from utils.api import login_user


def login_page():

    st.title("🤖 Customer Support AI")
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        if not email or not password:
            st.warning("Please enter email and password.")
            return

        status_code, data = login_user(email, password)

        if status_code == 200:

            st.session_state.user_id = data["user_id"]
            st.session_state.username = data["username"]
            st.session_state.page = "chat"

            st.rerun()

        else:
            error_message = data.get(
                "detail",
                "Invalid email or password"
            )
            st.error(error_message)

    st.write("---")

    if st.button(
        "Create New Account",
        use_container_width=True
    ):
        st.session_state.page = "register"
        st.rerun()