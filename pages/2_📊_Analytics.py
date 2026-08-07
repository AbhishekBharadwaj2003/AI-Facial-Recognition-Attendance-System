import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📊 Attendance Analytics")

conn = sqlite3.connect("database/attendance.db")
df = pd.read_sql_query("SELECT * FROM attendance", conn)
conn.close()

if df.empty:
    st.warning("No attendance data available.")
    st.stop()

# Attendance count by student
attendance = df.groupby("name").size().reset_index(name="Attendance Count")

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(
        attendance,
        x="name",
        y="Attendance Count",
        color="Attendance Count",
        text="Attendance Count",
        title="Attendance by Student"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.pie(
        attendance,
        names="name",
        values="Attendance Count",
        hole=0.5,
        title="Attendance Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Daily attendance trend
daily = df.groupby("date").size().reset_index(name="Total Attendance")

fig = px.line(
    daily,
    x="date",
    y="Total Attendance",
    markers=True,
    title="Daily Attendance Trend"
)

st.plotly_chart(fig, use_container_width=True)