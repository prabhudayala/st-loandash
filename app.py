import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time

def main():
    st.markdown("""
        <style>
            .title {
                color: #820263;
                text-align: center;
                font-size: 2.5em;
                margin-bottom: 1em;
            }
            button[kind="primary"] {
                background-color: #f63366;
                color: white;
                padding: 0.5em 1em;
                border-radius: 0.5em;
                border: none;
                cursor: pointer;
                font-size: 1em;
            }
            button[kind="primary"]:hover {
                background-color: #d42c58;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='title'>Login</h1>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        login_btn = st.button("Login", key="login-btn", type="primary", use_container_width=True)
    if login_btn:
        if username  and password :
            st.success("Logged in as: {}".format(username))
            time.sleep(2)
            switch_page('file_upload')

        else:
            st.error("Please input valid username and password")

if __name__ == "__main__":
    main()
