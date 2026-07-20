import streamlit as st


def sidebar():

    with st.sidebar:

        st.title("🤖 TechMart Support AI")

        st.write("---")

        st.write(f"👤 {st.session_state.username}")

        st.write("---")

        if st.button("➕ New Chat", use_container_width=True):

            if "history" in st.session_state:
                st.session_state.history = []

            st.rerun()

        st.write("### 📝 Chat History")

        if "history" in st.session_state:

            for i, chat in enumerate(st.session_state.history, start=1):

                question = chat["question"]

                if len(question) > 25:
                    question = question[:25] + "..."

                st.caption(f"{i}. {question}")

        st.write("---")

        if st.button("🚪 Logout", use_container_width=True):

            st.session_state.page = "login"

            st.session_state.user_id = None

            st.session_state.username = ""

            if "history" in st.session_state:
                del st.session_state.history

            st.rerun()