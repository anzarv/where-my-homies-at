import streamlit as st
import pytz
from datetime import datetime

# Title screen
st.title("Where My Homies At?")
st.write("This application will help you find where your homies are at during their NSU campus schedule.")
st.write("Made by Anzar")

st.write("Enter 'A' for Anzar, 'E' for Elhussy, 'B' for Labubu")

# Finding the current time in GMT+6
target_timezone = pytz.timezone('Asia/Dhaka')
local_time = datetime.now(target_timezone)
st.write("The current time in Dhaka is:")
st.header(local_time.strftime("%A, %I:%M %p"))

# Get the current hour (0 to 23)
current_hour = local_time.hour

# Get the current day of the week (0 is Monday, 4 is Friday, etc.)
current_day = local_time.weekday()


# Finding who you're looking for
running = True

user_input = st.text_input("Type the name of the person you're searching for here: ")
if user_input == "A":
   if current_day == 4:
      st.write("Enjoy your Friday, Anzar!")





