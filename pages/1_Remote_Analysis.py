import streamlit as st
from utils.load import load_data

st.set_page_config(
    page_title='Remote Analysis',
    page_icon=':computer:'
)

data = load_data()

data = data[data['Employment_Type'] == 'Remote']

st.header('DataFrame describe')
st.dataframe(data.describe())
