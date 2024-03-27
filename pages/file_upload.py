from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import pandas as pd


st.markdown("<h1 class='title'>Upload Data</h1>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload excel File", type="xlsx")
next = st.button('Next')
if next:
    if uploaded_file:
        df = pd.read_excel(uploaded_file, sheet_name='data summary')
        st.session_state['data'] = df
        switch_page('sales_dash')
    else:
        st.error("Please Upload the Data")