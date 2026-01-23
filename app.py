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
current_minute = local_time.minute

# Get the current hour (0 to 23)
current_hour = local_time.hour

# Get the current day of the week (0 is Monday, 4 is Friday, etc.)
current_day = local_time.weekday()

# Everyone's schedules

anzar_sun_tue = [
    (780, 870, "ECO101 (NAC 605)"),
    (990, 1070, "ENG103 (NAC 203)"),
    ()
]

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

current_hour = 16
current_day = 6
current_minute = 30

now_mins = (current_hour * 60) + current_minute

if user_input == "A":
    if current_day == 6:  # Sunday
        st.subheader("Anzar's Sunday Tracker")

        # 1. Check current status
        found_now = False
        for start, end, name in anzar_sun_tue:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                found_now = True

        if not found_now:
            st.write("🏠 Not in class right now.")

        # 2. Find and show next class
        next_class = None
        for start, end, name in anzar_sun_tue:
            if start > now_mins:
                next_class = (start, name)
                break

        if next_class:
            st.warning(f"⏳ Next up: {next_class[1]} at {next_class[0] // 60}:{next_class[0] % 60:02d}")








