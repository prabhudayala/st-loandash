import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import plotly.express as px
import datetime as dt

st.set_page_config(layout='wide')

st.title('Dashboard - Chargeoff')

data = st.session_state['data']
data = data[data['Acct Status Desc'] == 'Charged Off'] 
data['Month'] = pd.to_datetime(data['Primary Loan Contract Date']).dt.month_name()

filtered_data = data[(data['Year'] == "2022") & (data['Month'] != 'December')]

st.write('### Charge Off Total Balance')
metric_cols = st.columns(2)
metric_cols[0].metric('**2022**', f"$ {filtered_data['Charge Off Orig Total Balance'].sum():,.2f}" )
metric_cols[1].metric('**2023**', f"$ {data[data['Year'] == '2023']['Charge Off Orig Total Balance'].sum():,.2f}" )
data = data[data['Charge Off Date'].notnull()]
acct_status_by_dealer = data.groupby(['Dealer', 'Acct Status Desc'])['Primary Loan Orig Amount Financed'].sum().reset_index()
fig1 = px.bar(acct_status_by_dealer, x='Dealer', y='Primary Loan Orig Amount Financed', title='Charged off amount by Dealer', barmode='group')

data['Charge Off Month'] = pd.to_datetime(data['Charge Off Date']).dt.month_name()
data['Charge Off Year'] = pd.to_datetime(data['Charge Off Date']).dt.year.astype(str)

data['Charge Off Month Year'] = data['Charge Off Month'] + ' ' + data['Charge Off Year']

charge_offs_by_date = data.groupby('Charge Off Month Year')['Charge Off Orig Total Balance'].sum().reset_index()
charge_offs_by_date.columns = ['Charge Off Month Year', 'Charge Off Amount']
fig2 = px.bar(charge_offs_by_date, x='Charge Off Month Year', y='Charge Off Amount', title='Charge-offs by Date')


fig3 = px.bar(data, x='Charge Off Month', y='Cur Balance', title='Charge-offs by Date', barmode='group', color='Dealer')



col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
c = st.columns([9,1]) 
back = c[0].button('Back')
next = c[1].button('Next')
if back:
    switch_page('sales_dash')
if next:
    switch_page('model_scoring')