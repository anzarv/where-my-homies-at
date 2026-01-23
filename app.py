import datetime
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
import streamlit as st
from streamlit_javascript import st_javascript
from datetime import datetime

st.title("My Local Time App")

# Ask the phone for the time
client_time = st_javascript("Date.now()")

# Check if we have the time yet
if client_time is not None and client_time > 0:
    # Convert milliseconds to a datetime object
    # We add a "timedelta" if the server is stubbornly showing UTC
    # Since you were 6 hours off, we subtract 6 hours (or add, depending on your zone)
    raw_time = datetime.fromtimestamp(client_time / 1000)

    st.write("Your local time is:")
    st.header(raw_time.strftime("%I:%M %p"))

elif client_time == 0:
    st.warning("Still waiting for your device to respond...")
else:
    st.info("Loading your clock... ⌚")