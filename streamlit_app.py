import streamlit as st
import sqlite3
import pandas as pd
import os

st.set_page_config(
    page_title="AI Facial Recognition Attendance System",
    page_icon=" ",
    layout="wide"
)

st.title("AI Facial Recognition Attendance System")
st.markdown("### Welcome to the AI-Based Facial Recognition Attendance Dashboard")

# ----------------------------
# Database
# ----------------------------

conn = sqlite3.connect("database/attendance.db")
df = pd.read_sql_query("SELECT * FROM attendance", conn)

# ----------------------------
# Metrics
# ----------------------------

registered_students = len(os.listdir("dataset"))

if len(df) > 0:
    unique_students = df["name"].nunique()
    today = df["date"].max()
    today_attendance = len(df[df["date"] == today])
else:
    unique_students = 0
    today_attendance = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👥 Registered Students",
        registered_students
    )

with col2:
    st.metric(
        "✅ Today's Attendance",
        today_attendance
    )

with col3:
    st.metric(
        "📋 Total Records",
        len(df)
    )

st.divider()

# ----------------------------
# Attendance Table
# ----------------------------

st.subheader("📋 Attendance Records")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

conn.close()