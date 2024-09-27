import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("temperature_scraping/temp_data.db")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temperature")
dates = [item[0] for item in cursor.fetchall()]

cursor.execute("SELECT temperature FROM temperature")
temps = [item[0] for item in cursor.fetchall()]

# cursor.execute("CREATE TABLE temperature('date', 'temperature')")

figure = px.line(x=dates, y=temps, 
                 labels={'x': "Date", 'y': "Temperature (C)"})

st.plotly_chart(figure)