import streamlit as st
import pytz
from datetime import datetime

# Title screen
st.title("Where My Homies At?")
st.write("This application will help you find where your homies are at during their NSU campus schedule.")
st.write("Made by Anzar")

st.write("Enter 'A' for Anzar, 'E' for Elhussy, 'B' for Labubu")

# This creates a box for you to type in
user_input = st.text_input("Type something here:")

# This shows the output only after you type something

if user_input:
   st.write("The Magic Box says:")
   st.header(user_input.upper()) # This makes your input BIG and LOUD

# 1. Define the GMT+6 timezone
# In the coding world, GMT+6 is often represented by 'Asia/Dhaka' or 'Etc/GMT-6'
# (Note: GMT offsets in 'Etc/' are often inverted, so we use a fixed offset)
target_timezone = pytz.timezone('Asia/Dhaka')

# 2. Get the current time in that timezone
local_time = datetime.now(target_timezone)

# 3. Show it on the screen
st.write("The current time in GMT+6 is:")
st.header(local_time.strftime("%I:%M %p"))

