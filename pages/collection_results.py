import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')
st.title('Collection Results') 

data = pd.read_excel("Python_app.xlsx", sheet_name='accounts', skiprows=1)
data.drop("Unnamed: 0", axis=1, inplace=True)
data = data[data['LoanNum'].notna()]
data['LoanNum'] = data['LoanNum'].astype(int)
sidebar = st.sidebar
loan = sidebar.selectbox("Loan Number",data['LoanNum'].unique())
if sidebar.button("Submit"):
    row = data[data['LoanNum'] == loan]
    sidebar.metric("DPD", row['Filtered # Days Past Due'].values[0])
    sidebar.metric("Segment", row["Segment"].values[0])
    row.drop(columns = ["LoanNum","RecommendationDate","DPD","Segment"], inplace=True)
    for col in row.columns:
        st.metric(col, row[col].values[0]) 

c = st.columns([9,1]) 
back = c[0].button('Back')
next = c[1].button('Next')
if back:
    switch_page('model_scoring')
if next:
    switch_page('champ_challenger')