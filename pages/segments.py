import streamlit as st

st.set_page_config(layout='wide')


score = [">90",'70-90','50-70','50-70','<30']
behaviour = ["Fast Payer- Low Risk", "Forgetful Payer", "Moderate Payer", "In Crisis Payer", "No Payer"]
accuracy = ["92% Pays in next 10 days", "85% Pays in 10-30 days","81% Pays in 30-60 days","75% Pays in 31-90 days","22% Pays 31-129 days"]
treatment = ["Digital/Letter Touchpoint","Low Phone Touch","Medium Phone Touch","Promise To Pay Allocate Hustler Agent","Best Settlement/Repo Best Hustler Agent"]

with st.container():
    for i in range(4):
        with st.expander(f'Seg_{i+1}'):
            cols = st.columns([2,4,4])
            with cols[0]: 
                st.metric('CB2AI™ Score', score[i])
            with cols[1]: 
                st.metric('Predicted Payment Behavior', behaviour[i])
            with cols[2]: 
                st.metric('Prediction Accuracy', accuracy[i])
            st.metric('Treatment for Early Cycle**', treatment[i])