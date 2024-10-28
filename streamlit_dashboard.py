import pandas as pd
import streamlit as st
import plotly.express as px


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/gathukalinet/viz2_assignment/refs/heads/main/dataset.csv')

emp_df = load_data()

# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")

grouped_inactive = emp_df.groupby(['year', 'sex'])['total_inactive_population'].sum().reset_index()
grouped_inactive['total_inactive_population'] = grouped_inactive['total_inactive_population'] / 1000000

fig = px.line(grouped_inactive, x='year', y='total_inactive_population', color='sex')
st.plotly_chart(fig)
git 