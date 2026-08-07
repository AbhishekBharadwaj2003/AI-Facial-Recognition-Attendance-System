import streamlit as st
import subprocess

st.set_page_config(layout="wide")

st.title("🎥 Live Face Recognition")

st.write("Click below to start recognition.")

if st.button("▶ Start Recognition"):

    subprocess.Popen(
        ["python", "app.py"]
    )

    st.success("Recognition Started!")