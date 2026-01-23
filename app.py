import streamlit as st
from streamlit_javascript import st_javascript

# Title screen
st.title("Where My Homies At?")
st.header("This application will help you find where your homies are at during their NSU campus schedule.")
st.subheader("Made by Anzar")

st.write("Enter 'A' for Anzar, 'E' for Elhussy, 'B' for Labubu")

# This creates a box for you to type in
user_input = st.text_input("Type something here:")

# This shows the output only after you type something


if user_input:
    st.write("The Magic Box says:")
    st.header(user_input.upper()) # This makes your input BIG and LOUD

st.title("Local Time App")

# This tiny bit of 'JavaScript' asks the phone for its own clock
# it returns the time in "milliseconds" (a very long number)
client_time = st_javascript("Date.now()")

if client_time:
    # We turn that long number into a readable time
    from datetime import datetime

    readable_time = datetime.fromtimestamp(client_time / 1000)

    st.write("On your device, the time is:")
    st.header(readable_time.strftime("%I:%M %p"))  # Shows as 02:30 PM
