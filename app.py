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
    (870, 980, "Free Period (Gym/Library/Cafeteria)"),
    (990, 1070, "ENG103 (NAC 203)")
]

labubu_sun_tue = [
    (780, 870, "ENG103 (SAC 309)"),
    (870, 980, "Free Period"),
    (990, 1070, "MAT116 (NAC 513)")
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

current_hour = 14
current_day = 6
current_minute = 40

now_mins = (current_hour * 60) + current_minute

if user_input == "A":
    if current_day == 6 or 1:  # Sunday or Tuesday
        st.subheader("Anzar's Sunday / Tuesday Tracker")

        # 1. Check current status
        found_now = False
        for start, end, name in anzar_sun_tue:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                found_now = True

        # If Anzar is in his free period, he's at the gym or library (unique to him)
        if 870 <= now_mins <= 980:
            found_now = False

            # 2. Only show "Next Class" if he is NOT in one right now
            if not found_now:
                st.write("❌ Not in class right now.")

                next_class = None
                for start, end, name in anzar_sun_tue:
                    if start > now_mins:
                        next_class = (start, end, name)  # Added end for completeness
                        break

                if next_class:
                    start_time = next_class[0]
                    class_name = next_class[2]

                    # --- NEW CALCULATION ---
                    mins_to_go = start_time - now_mins
                    hours_left = mins_to_go // 60
                    rem_mins = mins_to_go % 60

                    # Make the countdown look nice
                    if hours_left > 0:
                        countdown_text = f"{hours_left}h {rem_mins}m"
                    else:
                        countdown_text = f"{rem_mins} minutes"
                    # -----------------------

                    # Math to make the start time look pretty (e.g., 4:30 PM)
                    start_h = start_time // 60
                    start_m = start_time % 60
                    period = "PM" if start_h >= 12 else "AM"
                    display_h = start_h - 12 if start_h > 12 else start_h

                    st.info(f"⏭️ **Next Class:** {class_name} at {display_h}:{start_m:02d} {period}")
                    st.metric(label="Time til next class:", value=countdown_text)
                else:
                    st.write("✅ All done for today!")


if user_input == "L":
    if current_day == 6 or 1:  # Sunday or Tuesday
        st.subheader("Labiba's Sunday / Tuesday Tracker")

        # 1. Check current status
        found_now = False
        for start, end, name in labubu_sun_tue:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                found_now = True

        if 870 <= now_mins <= 980:
            found_now = False

        if not found_now:
            st.write("❌ Not in class right now.")

        # 2. Find and show next class
        next_class = None
        for start, end, name in labubu_sun_tue:
            if start > now_mins:
                next_class = (start, name)
                break  # Stop at the very next one

        if next_class:
            # Math to make time look pretty (e.g., 4:30 PM)
            start_h = next_class[0] // 60
            start_m = next_class[0] % 60
            period = "PM" if start_h >= 12 else "AM"
            display_h = start_h - 12 if start_h > 12 else start_h

            st.info(f"⏭️ **Next Class:** {next_class[1]} at {display_h}:{start_m:02d} {period}")
        else:
            st.success("✅ All done for today!")







