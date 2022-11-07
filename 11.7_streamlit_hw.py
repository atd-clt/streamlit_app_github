import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

#import the data set
unemployment = pd.read_csv('unemployment_2012-2014.csv')

st.title ("Abey T. Dessie - DSBA 5122")
st.header('World Unemployment Data: 2012 - 2014')


st.write(unemployment)

st.sidebar.header("Pick two variables for your scatterplot")
x_val = st.sidebar.selectbox("Pick your x-axis",unemployment.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",unemployment.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(unemployment, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val, title=f"{x_val}"),
    alt.Y(y_val, title=f"{y_val}"),
    tooltip=[x_val,y_val])
st.altair_chart(scatter, use_container_width=True)

#calculate the correlation 
corr = round(unemployment[x_val].corr(unemployment[y_val]),3)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")