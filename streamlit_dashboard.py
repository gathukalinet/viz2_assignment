# Importing the required libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Setting the layout to evenly spread my containers
st.set_page_config(layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/gathukalinet/viz2_assignment/refs/heads/main/dataset.csv')

emp_df = load_data()

# Simple Streamlit app using Plotly


# etting the title for the first half of visualizations
st.title("Employment Trends Analysis in Kenya ")

# Establishing the number of rows and columns of the above title
row1 = st.columns(3)
row2 = st.columns(3)


with row1[0]:
# Grouping the dataset by year and sex and summing the total inactive population
   grouped_inactive = emp_df.groupby(['year', 'sex'])['total_inactive_population'].sum().reset_index()
  
# Creating individual containers for each visualization
   container = st.container(border=True)
   container.write("Total Inactive Population by Year and Sex.")
   fig = px.line(grouped_inactive, x='year', y='total_inactive_population', color='sex')
   container.plotly_chart(fig, use_container_width=True)

with row2[0]:
# Grouping the dataset by sex and summing the total inactivepopulation
   grouped_inactiveTotal = emp_df.groupby(['sex'])['total_inactive_population'].sum().reset_index()
   
# Creating an individual container for the pie chart
   container = st.container(border=True)
   container.write("Total Inactive Population by Sex.")
   fig1 =px.pie(grouped_inactive, values='total_inactive_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_inactive_population': 'total_inactive_population'})
   container.plotly_chart(fig1,use_container_width=True)

with row1[1]:
# Grouping the dataset by year and sex and summing the total unemployed population
   grouped_unemployed=emp_df.groupby(['year', 'sex'])['total_unemployed_population'].sum().reset_index()
   
# Creating an individual container for the line chart   
   container = st.container(border=True)
   container.write("Total Unemployed Population by Year and Sex.")
   fig2 = px.line(grouped_unemployed, x='year', y='total_unemployed_population', color='sex')
   container.plotly_chart(fig2, use_container_width=True)

with row2[1]:
# Grouping the dataset by sex and summing the total unemployed population
   grouped_unemployedTotal = emp_df.groupby(['sex'])['total_unemployed_population'].sum().reset_index()
  
# Creating an individual container for the pie chart
   container = st.container(border=True)
   container.write("Total Unemployed Population by Sex.")
   fig3 = px.pie(grouped_unemployed, values='total_unemployed_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_unemployed_population': 'total_unemployed_population'})
   container.plotly_chart(fig3, use_container_width=True)

with row1[2]:
# Grouping the dataset by year and sex and summing the total employed population
   grouped_employed=emp_df.groupby(['year', 'sex'])['total_employed_population'].sum().reset_index()
   
# Creating an individual container for the line chart
   container = st.container(border=True)
   container.write("Total Employed Population by Year and Sex.")
   fig4 = px.line(grouped_employed, x='year', y='total_employed_population', color='sex')
   container.plotly_chart(fig4, use_container_width=True)

with row2[2]:
# Grouping the dataset by sex and summing the total employed  population
   grouped_employedTotal=emp_df.groupby(['sex'])['total_employed_population'].sum().reset_index()
   
# Creating an individual container for the pie chart
   container = st.container(border=True)
   container.write("Total Employed Population by Sex.")
   fig5 = px.pie(grouped_employed, values='total_employed_population', names='sex', color='sex', 
       labels={'sex': 'sex', 'total_employed_population': 'total_employed_population'})
   container.plotly_chart(fig5, use_container_width=True)   

# Setting the title for the second half of visualizations
st.title("Education Level by Year and Age Groups Kenya")
# Establishing the number of rows and columns of the above title
row1 = st.columns(3)
row2 = st.columns(3)

with row1[0]:
# Grouping the dataset by year and sex to determine the sum of people with basic education
   df_grouped1 = emp_df.groupby(['year', 'sex'])[['total_inactive_population', 'total_unemployed_population', 'total_employed_population',
                                              'Basic_unemployment','Intermediate_unemployment',
                                              'Advanced_unemployment','age_group']].sum().reset_index()
# Creating an individual container for the bar chart
   container = st.container(border=True)
   container.write("Total Basic Education by Sex.")
   fig6 = px.bar(df_grouped1, x='year', y='Basic_unemployment', color='sex')
   container.plotly_chart(fig6, use_container_width=True)

with row1[1]:
# Grouping the dataset by year and sex to determine the sum of people with intermediate education
    df_grouped1 = emp_df.groupby(['year', 'sex'])[['total_inactive_population', 'total_unemployed_population', 'total_employed_population',
                                              'Basic_unemployment','Intermediate_unemployment',
                                              'Advanced_unemployment','age_group']].sum().reset_index()
# Creating an individual container for the bar chart
    container = st.container(border=True)
    container.write("Total Intermediate Education by Sex.")
    fig7 = px.bar(df_grouped1, x='year', y='Intermediate_unemployment', color='sex')
    container.plotly_chart(fig7, use_container_width=True)

with row1[2]:
# Grouping the dataset by year and sex to determine the sum of people with advanced education
    df_grouped1 = emp_df.groupby(['year', 'sex'])[['total_inactive_population', 'total_unemployed_population', 'total_employed_population',
                                              'Basic_unemployment','Intermediate_unemployment',
                                              'Advanced_unemployment','age_group']].sum().reset_index()
# Creating an individual container for the bar chart
    container = st.container(border=True)
    container.write("Total Advanced Education by Sex.")
    fig8 = px.bar(df_grouped1, x='year', y='Advanced_unemployment', color='sex')
    container.plotly_chart(fig8, use_container_width=True)

with row2[0]:
# Creating a container for the pie chart plot of basic education by age_group
    container = st.container(border=True)
    container.write("Total Basic Education by Age Group.")
    fig9 = px.pie(emp_df, values='Basic_unemployment',names='age_group', color='age_group', hole=0.5)
    container.plotly_chart(fig9, use_container_width=True)

with row2[1]:
# Creating a container for the pie chart plot of intermediate education by age_group
    container = st.container(border=True)
    container.write("Total Intermediate Education by Age Group.")
    fig10 = px.pie(emp_df, values='Intermediate_unemployment',names='age_group', color='age_group', hole=0.5)
    container.plotly_chart(fig10, use_container_width=True)

with row2[2]:
# Creating a container for the pie chart plot of advanced education by age_group
    container = st.container(border=True)
    container.write("Total Advanced Education by Age Group.")
    fig11 = px.pie(emp_df, values='Advanced_unemployment',names='age_group', color='age_group', hole=0.5)
    container.plotly_chart(fig11, use_container_width=True)
   