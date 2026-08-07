import streamlit as st

st.title("📥 Download Attendance")

with open("exports/attendance.xlsx", "rb") as file:

    st.download_button(
        label="📥 Download Attendance Excel",
        data=file,
        file_name="attendance.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )