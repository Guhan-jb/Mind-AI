import streamlit as st
from video import video1
from Audio import record_and_save_audio
from Assitant import assist
# Page 1: Video Recording
st.title("Video Recording")

def record_video(duration):
   
    #  video1(duration)
    #  st.write(record_and_save_audio())
    assist()

if st.button("Start Recording"):
    record_video(5)  # Record for 5 seconds

st.sidebar.markdown(
    """
    ### Instructions

    1. Click the "Start Recording" button to start recording. Recording will last for 5 seconds.
    """
)
