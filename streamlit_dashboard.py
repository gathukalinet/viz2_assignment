import pandas as pd
import streamlit as st
import plotly.express as px


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/gathukalinet/viz2_assignment/refs/heads/main/dataset.csv')

emp_df = load_data()

# Simple Streamlit app using Plotly
st.title("Employment Trends Analysis in Kenya ")


col1, col2, col3 = st.columns(3)

with col1(use_container_width=True):
   st.write("Total Inactive Population by Year and Sex.")

   grouped_inactive = emp_df.groupby(['year', 'sex'])['total_inactive_population'].sum().reset_index()
   grouped_inactive['total_inactive_population'] = grouped_inactive['total_inactive_population'] / 1000000

   fig = px.line(grouped_inactive, x='year', y='total_inactive_population', color='sex')
   st.plotly_chart(fig)

   grouped_inactiveTotal = emp_df.groupby(['sex'])['total_inactive_population'].sum().reset_index()
   grouped_inactiveTotal['total_inactive_population'] = grouped_inactiveTotal['total_inactive_population'] / 1000000

   st.write("Total Inactive Population by Sex.")

   fig1 =px.pie(grouped_inactive, values='total_inactive_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_inactive_population': 'total_inactive_population'})
   st.plotly_chart(fig1)

with col2(use_container_width=True):
   st.write("Total Unemployed Population by Year and Sex.")

   grouped_unemployed=emp_df.groupby(['year', 'sex'])['total_unemployed_population'].sum().reset_index()
   grouped_unemployed['total_unemployed_population'] = grouped_unemployed['total_unemployed_population'] / 1000000

   fig2 = px.line(grouped_unemployed, x='year', y='total_unemployed_population', color='sex')
   st.plotly_chart(fig2)

   grouped_unemployedTotal = emp_df.groupby(['sex'])['total_unemployed_population'].sum().reset_index()
   grouped_unemployedTotal['total_unemployed_population'] = grouped_unemployedTotal['total_unemployed_population'] / 1000000
   
   st.write("Total Unemployed Population by Sex.")

   fig3 = px.pie(grouped_unemployed, values='total_unemployed_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_unemployed_population': 'total_unemployed_population'})
   st.plotly_chart(fig3)

with col3(use_container_width=True):
   st.write("Total Employed Population by Year and Sex.")

   grouped_employed=emp_df.groupby(['year', 'sex'])['total_employed_population'].sum().reset_index()
   grouped_employed['total_employed_population'] = grouped_employed['total_employed_population'] / 1000000

   fig4 = px.line(grouped_employed, x='year', y='total_employed_population', color='sex')
   st.plotly_chart(fig4)

   grouped_employedTotal=emp_df.groupby(['sex'])['total_employed_population'].sum().reset_index()
   grouped_employedTotal['total_employed_population'] = grouped_employedTotal['total_employed_population'] / 1000000

   st.write("Total Employed Population by Sex.")

   fig5 = px.pie(grouped_employed, values='total_employed_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_employed_population': 'total_employed_population'})
   st.plotly_chart(fig5)   


