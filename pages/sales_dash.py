import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(layout='wide')

st.title('Dashboard - Sales')

data = st.session_state['data']
data['Primary Loan Orig Amount Financed'] = data['Primary Loan Orig Amount Financed'].astype(float)

data['Year'] = pd.to_datetime(data['Primary Loan Contract Date']).dt.year
data['Month'] = pd.to_datetime(data['Primary Loan Contract Date']).dt.month_name()

sales_by_year_month = data.groupby(['Year', 'Month'])['Primary Loan Orig Amount Financed'].sum().reset_index()
fig1 = px.bar(sales_by_year_month, x='Month', y='Primary Loan Orig Amount Financed', color='Year', title='Sales by Year and Month')


sales_by_dealer = data.groupby('Dealer')['Primary Loan Orig Amount Financed'].sum().reset_index()
fig2 = px.bar(sales_by_dealer, x='Dealer', y='Primary Loan Orig Amount Financed', title='Sales by Dealer')

col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)
back = col1.button('Back')
c = col2.columns([9,1]) 
next = c[1].button('Next')
if back:
    switch_page('file_upload')
if next:
    switch_page('chargeoff_dash')