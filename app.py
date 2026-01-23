import streamlit as st
import pytz
from datetime import datetime

# Title screen
st.title("Where My Homies At❓")
st.write("This application will help you find where your homies are at during their NSU campus schedule.")
st.write("Made by Anzar")


# Finding the current time in GMT+6
target_timezone = pytz.timezone('Asia/Dhaka')
local_time = datetime.now(target_timezone)
st.write("--------")
st.header(local_time.strftime("%A, %I:%M %p"))

# Get the current minute (0 to 59)
# current_minute = local_time.minute

# Get the current hour (0 to 23)
# current_hour = local_time.hour

# Get the current day of the week (0 is Monday, 4 is Friday, etc.)
# current_day = local_time.weekday()

# Finding who you're looking for

user_input = st.text_input("Enter 'A' for Anzar, 'E' for Elhussy, 'L' for Labubu: ")

current_hour = 13
current_day = 6
current_minute = 20

if user_input == "A":
        if current_day == 6:  # Saturday
            st.subheader("Anzar's Saturday Schedule")

            if (current_hour == 13) or (current_hour == 14 and current_minute <= 30):
                st.write("📍 In Class: ECO101 (NAC 605)")
            elif 10 <= current_hour < 12:
                st.write("📍 In Class: MAT120 (NAC 502)")
            elif 14 == current_hour and 30 <= current_minute <= 45:
                st.write("📍 Free Time: Probably at the Cafeteria")
            else:
                st.write("📍 Off-campus or chilling")





