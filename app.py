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


# if user_input:
   #  st.write("The Magic Box says:")
   #  st.header(user_input.upper()) # This makes your input BIG and LOUD

st.title("My Local Time App")

# 1. Ask the browser for the time as a number
client_time = st_javascript("Date.now()")

if client_time:
    # 2. We turn that number into a 'timestamp'
    # and tell it to display exactly what the browser sees
    readable_time = datetime.fromtimestamp(client_time / 1000)

    st.write("The time on your device is:")

    # This formats it: %I is hour, %M is minute, %p is AM/PM
    st.header(readable_time.strftime("%I:%M %p"))
else:
    st.write("Checking your watch... ⌚")