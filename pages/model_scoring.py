import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Collection Model Scoring')
data = pd.read_excel('CollectionAI_SampleData_v1.xlsx')
data = data.drop('Proposed Strategy', axis=1)

def make_clickable(url, text):
    st.session_state['selected_seg'] = text
    return f'<a href="{url}" target="_blank">{text}</a>'

data['Link'] = data['Segment'].apply(lambda x: make_clickable(f'/segments', x))


st.markdown(data.to_html(escape=False, render_links=True), unsafe_allow_html=True)
# st.dataframe(data, use_container_width=True)