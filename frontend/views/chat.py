import streamlit as st

from utils.api import (
    send_message,
    get_chat_history
)

from components.sidebar import sidebar


def chat_page():

    # -----------------------------
    # Sidebar
    # -----------------------------
    sidebar()

    st.title("🤖 Customer Support AI")

    st.divider()

    # -----------------------------
    # Load Chat History Only Once
    # -----------------------------
    if "history" not in st.session_state:

        response = get_chat_history(
            st.session_state.user_id
        )

        if response.status_code == 200:

            st.session_state.history = response.json()["history"]

        else:

            st.session_state.history = []

    # -----------------------------
    # Display Chat History
    # -----------------------------
    for chat in st.session_state.history:

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):
            st.write(chat["answer"])

    # -----------------------------
    # Chat Input
    # -----------------------------
    message = st.chat_input("Type your message...")

    if message:

        with st.chat_message("user"):
            st.write(message)

        response = send_message(
            st.session_state.user_id,
            message
        )

        if response.status_code == 200:

            ai = response.json()["ai_response"]

            with st.chat_message("assistant"):
                st.write(ai)

            st.session_state.history.append(
                {
                    "question": message,
                    "answer": ai
                }
            )

            st.rerun()

        else:

            st.error("Unable to get response.")