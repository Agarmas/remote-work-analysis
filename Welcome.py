import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from .utils.load import load_data

st.set_page_config(
    page_title='Welcome',
    page_icon=':wave:'
)

data = load_data()

st.title('Remote work productivity data')

st.header('DataFrame')

st.dataframe(data)

st.header('DataFrame info')
st.write(data.info)
st.header('DataFrame describe')
st.write(data.describe)

st.header('Heatmap of Correlation Matrix')

correlation_matrix = data.drop(columns=['Employment_Type']).corr()

plt.figure(figsize=(10, 6))
heatmap = sns.heatmap(correlation_matrix, annot=True,
                      cmap="coolwarm", linewidths=0.5)

st.pyplot(plt)
