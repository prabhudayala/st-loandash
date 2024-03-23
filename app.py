import streamlit as st

def main():
    """Styled Streamlit login page"""
    
    # Set page title with CSS styling
    st.markdown("""
        <style>
            .title {
                color: #f63366;
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
    
    st.markdown("<h1 class='title'>Login Page</h1>", unsafe_allow_html=True)
    
    # Create input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Create a styled login button
    if st.button("Login", key="login-btn", type="primary"):
        # if username == "admin" and password == "password":
        st.success("Logged in as: {}".format(username))
            # Redirect to the dashboard or another page
        # else:
        #     st.error("Invalid username or password")

if __name__ == "__main__":
    main()
