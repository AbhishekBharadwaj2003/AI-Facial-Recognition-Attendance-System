import streamlit as st
import os

st.title("👥 Registered Students")

students = sorted(os.listdir("dataset"))

st.metric("Total Students", len(students))

st.divider()

for student in students:
    st.success(student)