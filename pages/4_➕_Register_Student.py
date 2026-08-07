import streamlit as st
import subprocess

st.title("➕ Register New Student")

name = st.text_input("Enter Student Name")

if st.button("Start Registration"):

    if name.strip() == "":
        st.warning("Please enter a student name.")

    else:

        st.info("Opening camera...")

        subprocess.run(
            ["python", "register_student.py", name]
        )

        st.success("Student Registered Successfully!")