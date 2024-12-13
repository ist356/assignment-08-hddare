'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")
st.title('Top Locations for Parking Tickets')
st.caption('This dashboard shows the top locations for parking tickets.')
data = pd.read_csv('cache/final_cuse_parking_violations.csv')
locations = data['location'].unique()
location = st.selectbox('Select a location:', locations)
if location:
    location_data = data[data['location'] == location]
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Total tickets issued', location_data.shape[0])
        fig1, ax1 = plt.subplots()
        ax1.set_title('Tickets Issued by Hour of Day')
        sns.barplot(data=location_data, x='hourofday', y='count', estimator='sum', hue='hourofday', ax=ax1)
        st.pyplot(fig1)
    with col2:
        st.metric('Total amount', f"$ {location_data['amount'].sum()}")
        fig2, ax2 = plt.subplots()
        ax2.set_title('Tickets Issued by Day of Week')
        sns.barplot(data=location_data, x='dayofweek', y='count', estimator='sum', hue='dayofweek', ax=ax2)
        st.pyplot(fig2)

    st.map(location_data[['lat', 'lon']])