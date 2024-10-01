import streamlit as st
from utils.load import load_data

st.set_page_config(
    page_title='In-Ofice Analysis',
    page_icon=':briefcase:'
)

data = load_data()

data = data[data['Employment_Type'] == 'In-Office']

st.header('DataFrame describe')
st.dataframe(data.describe())
