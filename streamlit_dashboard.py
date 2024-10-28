import pandas as pd
import streamlit as st
import plotly.express as px


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/gathukalinet/viz2_assignment/refs/heads/main/dataset.csv')

data = load_data()

# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")
   
fig = px.line(data, x="year", y="population", color="sex", title="Population Over Time")
st.plotly_chart(fig)
