import streamlit as st
import pandas as pd

data = pd.read_csv('./remote_work_productivity.csv', index_col='Employee_ID')

st.title('Remote work productivity dataframe')
st.dataframe(data)
