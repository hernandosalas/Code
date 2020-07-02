'''
Web app using Streamlit


You can install Streamlit with pip:
$pip install streamlit

run streamlit on a python script:
$streamlit run app.py

# $ pip install virtualenv
# $ pip install -r requirements.txt
# $ virtualenv --system-site-packages -p python ./venv ; .\venv\Scripts\activate
# $ pip freeze -l > requirements.txt 
'''

import streamlit as st
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import plotly_express as px


st.title('Football DB')

'''
# Club and Nationality App
This very simple webapp allows you to select and visualize players from certain clubs and certain nationalities.
'''
df = st.cache(pd.read_csv)("football_data.csv")
clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())
new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(new_df)
# Create distplot with custom bin_size
fig = px.scatter(new_df, x ='Overall',y='Age',color='Name')
'''
### Here is a simple chart between player age and overall
'''
st.plotly_chart(fig)


# # Text Input
# url = st.text_input('Enter URL')

# # Write
# st.write('The Entered URL is', url)


# # Checkbox
# df = pd.read_csv("football_data.csv")
# if st.checkbox('Show dataframe'):
#     st.write(df)

# # SelectBox
# age = streamlit.selectbox("Choose your age: ", np.arange(18, 66, 1))

# # Slide
# age = streamlit.slider("Choose your age: ", min_value=16, max_value=66, value=35, step=1)

# # MultiSelect
# artists = st.multiselect("Who are your favorite artists?", ["Michael Jackson", "Elvis Presley", "Eminem", "Billy Joel", "Madonna"])


# # Caching
# df = st.cache(pd.read_csv)("football_data.csv")
# 
# @st.cache
# def load_data():
#     df = pd.read_csv("your_data.csv")
#     return df
# df = load_data()

# # Sidebar
# clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())

# # Markdown
# st.markdown("### 🎲 The Application")
# st.markdown("This application is a Streamlit dashboard hosted on Heroku that can be used"
#             "to explore the results from board game matches that I tracked over the last year.")
# st.markdown("**♟ General Statistics ♟**")
# st.markdown("* This gives a general overview of the data including"
#             "frequency of games over time, most games played in a day, and longest break"
#             "between games.")



