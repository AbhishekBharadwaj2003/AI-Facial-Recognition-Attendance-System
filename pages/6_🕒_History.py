import streamlit as st
from utils.attendance_history import RecognitionHistory

st.title("🕒 Recognition History")

history = RecognitionHistory()

df = history.get_recent()

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

history.close()