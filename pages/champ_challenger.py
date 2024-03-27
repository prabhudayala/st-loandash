import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(layout='wide')
st.title('Champion/Challenger Setup')

st.image("ab_test.png", use_column_width=True)

if st.button("Back"):
    switch_page("collection_results")