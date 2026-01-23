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

st.write("Who you looking for dawg?")
user_input = None

# Create three columns so the buttons are side-by-side
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👅 Anzar"):
        user_input = "A"
with col2:
    if st.button("😿 Elhussy"):
        user_input = "E"
with col3:
    if st.button("🐥 Labubu"):
        user_input = "L"

current_hour = 14
current_day = 1
current_minute = 30

if user_input == "A":
        if current_day == 6 or 1:  # Sunday or Tuesday
            st.subheader("Anzar's Sunday / Tuesday Schedule")

            if (current_hour == 13) or (current_hour == 14 and current_minute <= 29):
                st.write("📍 In Class: ECO101 (NAC 605)")
                st.write("Floor number 6 of NAC.")
            elif (current_hour == 14 and current_minute >= 30) or (current_hour == 15) or (current_hour == 16 and current_minute <= 20):
                st.write("😎 Free Period.")
                st.write("I'm probably at the NSU gym or central library at this time.")
            elif (current_hour == 16) or (current_hour == 17 and current_minute <= 50):
                st.write("📍 In Class: ENG103 (NAC 203)")
            else:
                st.write("🤠 Not in class yet.")

        elif current_day == 3 or 5:  # Thursday or Saturday
            st.subheader("Anzar's Thursday / Saturday Schedule")






