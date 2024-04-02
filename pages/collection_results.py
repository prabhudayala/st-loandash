import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px
import numpy as np

st.set_page_config(layout='wide')
st.title('Collection Results') 

data = pd.read_excel("Python_app.xlsx", sheet_name='accounts', skiprows=1)
data.drop("Unnamed: 0", axis=1, inplace=True)
data = data[data['LoanNum'].notna()]
data['LoanNum'] = data['LoanNum'].astype(int)
data[data.columns[6]] = data[data.columns[6]].astype(int)
data.fillna("NA", inplace=True)
sidebar = st.sidebar
loan = sidebar.selectbox("Loan Number",data['LoanNum'].unique())


def change_curr(x):
    return f"${x:,.2f}"


st.markdown(
        """
    <style>
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
    }

    [data-testid="stMetricLabel"] {
        color: green;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

if sidebar.button("Submit"):
    row = data[data['LoanNum'] == loan]
    sidebar.metric("DPD", row['Filtered # Days Past Due'].values[0])
    sidebar.metric("Segment", row["Segment"].values[0])
    row.drop(columns = ["LoanNum","RecommendationDate","DPD","Segment"], inplace=True)

    for i in [7,8,10,17,19,22,23,25]:
        row[row.columns[i]] = row[row.columns[i]].apply(change_curr)

    st.metric(row.columns[0], row[row.columns[0]].values[0])
    c1,c2 = st.columns(2)
    for i in range(1,len(row.columns),2):
        with c1:
            st.metric(row.columns[i], row[row.columns[i]].values[0])
        try:
            with c2:
                st.metric(row.columns[i+1], row[row.columns[i+1]].values[0])
        except IndexError:
            pass

c = st.columns([9,1]) 
back = c[0].button('Back')
next = c[1].button('Next')
if back:
    switch_page('data_overview')
if next:
    switch_page('champ_challenger')