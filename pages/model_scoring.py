import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Collection Model Scoring')
data = pd.read_excel('CollectionAI_SampleData_v1.xlsx')
st.session_state['result_data'] = data
data = data.drop('Proposed Strategy', axis=1)

def make_clickable(url, text):
    st.session_state['selected_seg'] = text
    return f'<a href="{url}" target="_blank">{text}</a>'

data['Link'] = data['Segment'].apply(lambda x: make_clickable(f'/segments', x))

c = st.columns([9,1]) 
st.markdown(data.to_html(escape=False, render_links=True), unsafe_allow_html=True)
back = c[0].button('Back')
next = c[1].button('Next')
if back:
    switch_page('chargeoff_dash')
if next:
    switch_page('model_framework')