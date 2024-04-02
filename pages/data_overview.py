import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(layout='wide')
st.title('Data Collection Overview')

st.image("overview.png", use_column_width=True)
c = st.columns([9,1]) 
back = c[0].button('Back')
next = c[1].button('Next')
if back:
    switch_page('model_framework')
if next:
    switch_page('collection_results')