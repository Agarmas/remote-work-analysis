import streamlit as st
import pandas as pd
from utils.load import load_data

st.set_page_config(
    page_title='Conclusion',
    page_icon=':scroll:'
)

data = load_data()

st.header('Average Productivity and Well-Being by Employment Type')

remote_data = data[data['Employment_Type'] == 'Remote']
office_data = data[data['Employment_Type'] == 'In-Office']

avg_remote = remote_data[['Productivity_Score', 'Well_Being_Score']].mean()
avg_office = office_data[['Productivity_Score', 'Well_Being_Score']].mean()

avg_data = pd.DataFrame({
    'Remote': avg_remote,
    'In-Office': avg_office
}).T

st.subheader('Average Productivity Score by Employment Type')
st.bar_chart(avg_data['Productivity_Score'])

st.subheader('Average Well-Being Score by Employment Type')
st.bar_chart(avg_data['Well_Being_Score'])
