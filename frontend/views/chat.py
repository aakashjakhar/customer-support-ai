import streamlit as st

from utils.api import send_message, get_chat_history
from components.sidebar import sidebar


def chat_page():

    sidebar()

    st.title("🤖 Customer Support AI")
    st.divider()

    if "user_id" not in st.session_state:
        st.error("Please login first.")
        st.session_state.page = "login"
        st.rerun()

    if (
        "history" not in st.session_state
        or not isinstance(st.session_state.history, list)
    ):
        status_code, data = get_chat_history(
            st.session_state.user_id
        )

        if status_code == 200:
            history = data.get("history", [])

            if isinstance(history, list):
                st.session_state.history = history
            else:
                st.session_state.history = []
        else:
            st.session_state.history = []

    for chat in st.session_state.history:

        if not isinstance(chat, dict):
            continue

        with st.chat_message("user"):
            st.write(chat.get("question", ""))

        with st.chat_message("assistant"):
            st.write(chat.get("answer", ""))

    message = st.chat_input("Type your message...")

    if message:

        with st.chat_message("user"):
            st.write(message)

        with st.spinner("AI is thinking..."):

            status_code, data = send_message(
                st.session_state.user_id,
                message
            )

        if status_code == 200:

            ai_response = data.get(
                "ai_response",
                "No response received."
            )

            with st.chat_message("assistant"):
                st.write(ai_response)

            st.session_state.history.append(
                {
                    "question": message,
                    "answer": ai_response
                }
            )

            st.rerun()

        else:
            detail = data.get(
                "detail",
                "Unable to get response."
            )

            if isinstance(detail, list):
                st.error(str(detail))
            else:
                st.error(detail)