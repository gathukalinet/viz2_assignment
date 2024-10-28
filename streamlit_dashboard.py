import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/gathukalinet/viz2_assignment/refs/heads/main/dataset.csv')

emp_df = load_data()

# Simple Streamlit app using Plotly



st.title("Employment Trends Analysis in Kenya ")


row1 = st.columns(3)
row2 = st.columns(3)


with row1[0]:
   grouped_inactive = emp_df.groupby(['year', 'sex'])['total_inactive_population'].sum().reset_index()
   grouped_inactive['total_inactive_population'] = grouped_inactive['total_inactive_population'] / 1000000

   container = st.container(border=True)
   container.write("Total Inactive Population by Year and Sex.")
   fig = px.line(grouped_inactive, x='year', y='total_inactive_population', color='sex')
   container.plotly_chart(fig, use_container_width=True)

with row2[0]:
   grouped_inactiveTotal = emp_df.groupby(['sex'])['total_inactive_population'].sum().reset_index()
   grouped_inactiveTotal['total_inactive_population'] = grouped_inactiveTotal['total_inactive_population'] / 100000

   container = st.container(border=True)
   container.write("Total Inactive Population by Sex.")
   fig1 =px.pie(grouped_inactive, values='total_inactive_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_inactive_population': 'total_inactive_population'})
   container.plotly_chart(fig1,use_container_width=True)

with row1[1]:
   
   grouped_unemployed=emp_df.groupby(['year', 'sex'])['total_unemployed_population'].sum().reset_index()
   grouped_unemployed['total_unemployed_population'] = grouped_unemployed['total_unemployed_population'] / 1000000
   
   container = st.container(border=True)
   container.write("Total Unemployed Population by Year and Sex.")
   fig2 = px.line(grouped_unemployed, x='year', y='total_unemployed_population', color='sex')
   container.plotly_chart(fig2, use_container_width=True)

with row2[1]:
   grouped_unemployedTotal = emp_df.groupby(['sex'])['total_unemployed_population'].sum().reset_index()
   grouped_unemployedTotal['total_unemployed_population'] = grouped_unemployedTotal['total_unemployed_population'] / 1000000
   
   container = st.container(border=True)
   container.write("Total Unemployed Population by Sex.")
   fig3 = px.pie(grouped_unemployed, values='total_unemployed_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_unemployed_population': 'total_unemployed_population'})
   container.plotly_chart(fig3, use_container_width=True)

with row1[2]:
   
   grouped_employed=emp_df.groupby(['year', 'sex'])['total_employed_population'].sum().reset_index()
   grouped_employed['total_employed_population'] = grouped_employed['total_employed_population'] / 1000000

   container = st.container(border=True)
   container.write("Total Employed Population by Year and Sex.")
   fig4 = px.line(grouped_employed, x='year', y='total_employed_population', color='sex')
   container.plotly_chart(fig4, use_container_width=True)

with row2[2]:
   grouped_employedTotal=emp_df.groupby(['sex'])['total_employed_population'].sum().reset_index()
   grouped_employedTotal['total_employed_population'] = grouped_employedTotal['total_employed_population'] / 1000000

   container = st.container(border=True)
   container.write("Total Employed Population by Sex.")
   fig5 = px.pie(grouped_employed, values='total_employed_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_employed_population': 'total_employed_population'})
   container.plotly_chart(fig5, use_container_width=True)   


st.title("Employment Status by Education Level in Kenya")

row1 = st.columns(3)
row2 = st.columns(3)

with row1[0]:
   df_grouped1 = emp_df.groupby(['year', 'sex'])[['total_inactive_population', 'total_unemployed_population', 'total_employed_population',
                                              'Basic_unemployment','Intermediate_unemployment',
                                              'Advanced_unemployment','age_group']].sum().reset_index()
   container = st.container(border=True)
   container.write("Total Basic Education by Sex.")
   fig6 = px.bar(df_grouped1, x='year', y='Basic_unemployment', color='sex')
   container.plotly_chart(fig6, use_container_width=True)

with row1[1]:
    df_grouped1 = emp_df.groupby(['year', 'sex'])[['total_inactive_population', 'total_unemployed_population', 'total_employed_population',
                                              'Basic_unemployment','Intermediate_unemployment',
                                              'Advanced_unemployment','age_group']].sum().reset_index()
    container = st.container(border=True)
    container.write("Total Intermediate Education by Sex.")
    fig7 = px.bar(df_grouped1, x='year', y='Intermediate_unemployement', color='sex')
    container.plotly_chart(fig7, use_container_width=True)

with row1[2]:
    df_grouped1 = emp_df.groupby(['year', 'sex'])[['total_inactive_population', 'total_unemployed_population', 'total_employed_population',
                                              'Basic_unemployment','Intermediate_unemployment',
                                              'Advanced_unemployment','age_group']].sum().reset_index()
    container = st.container(border=True)
    container.write("Total Advanced Education by Sex.")
    fig8 = px.bar(df_grouped1, x='year', y='Advanced_unemployment', color='sex')
    container.plotly_chart(fig8, use_container_width=True)