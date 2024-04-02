import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(layout='wide')
st.image("results.webp", use_column_width=True)

back = st.button('Back')
if back:
    switch_page("cust_seg")
