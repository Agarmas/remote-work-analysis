import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Welcome',
    page_icon=':wave:'
)

dtype_dict = {
    'Employee_ID': 'int64',
    'Employment_Type': 'category',
    'Hours_Worked_Per_Week': 'int64',
    'Productivity_Score': 'int64',
    'Well_Being_Score': 'int64'
}

data = pd.read_csv('./remote_work_productivity.csv',
                   index_col='Employee_ID', dtype=dtype_dict)

st.title('Remote work productivity data')

st.header('DataFrame')

st.dataframe(data)

st.header('Heatmap of Correlation Matrix')

correlation_matrix = data.drop(columns=['Employment_Type']).corr()

plt.figure(figsize=(10, 6))
heatmap = sns.heatmap(correlation_matrix, annot=True,
                      cmap="coolwarm", linewidths=0.5)

st.pyplot(plt)
