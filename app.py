import streamlit as st
import pytz
from datetime import datetime

# Title screen
st.title("Where Are My Homies At❓")
st.write("This application will help you find where your homies are at during their NSU campus schedule.")
st.write("Made by Anzar. If you find any bugs, please message me and let me know.")


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

anzar_thurs_sat = [
    (780, 870, "ACT201 (NAC410)"),
    (880, 970, "BUS112 (NAC207")
]

labubu_sun_tue = [
    (780, 870, "ENG103 (SAC 309)"),
    (870, 980, "Free Period"),
    (990, 1070, "MAT116 (NAC 513)")
]

labubu_thurs_sat = [
    (780, 870, "BIO103 (NAC310)"),
    (880, 970, "CHE101 (SAC407)")
]

elhussy_sun_tue = [
    (780, 870, "ENG103 (NAC409)"),
    (880, 970, "PSY101 (NAC215")
]

elhussy_thurs_sat = [
    (780, 870, "ECO101 (NAC412)"),
    (870, 980, "Free Period"),
    (990, 1070, "BUS112 (SAC208)")

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

# Test variables
current_day = 6
current_hour = 13
current_minute = 0

now_mins = (current_hour * 60) + current_minute

if user_input == "A":
    # Sunday (6) or Tuesday (1)
    if current_day == 6 or current_day == 1:
        st.subheader("Anzar's Sunday / Tuesday Tracker")

        # 1. Check if CURRENTLY in class
        found_now = False
        for start, end, name in anzar_sun_tue:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                if not 870 <= now_mins <= 980:
                    found_now = True
                    break

                # 2. If NOT in class, find the NEXT one
        if not found_now:
            st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in anzar_sun_tue:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time = next_class[0]
                class_name = next_class[2]

                # Countdown math
                mins_to_go = start_time - now_mins
                hours_left = mins_to_go // 60
                rem_mins = mins_to_go % 60

                countdown_text = f"{hours_left}h {rem_mins}m" if hours_left > 0 else f"{rem_mins}m"

                # Start time formatting
                start_h = start_time // 60
                start_m = start_time % 60
                period = "PM" if start_h >= 12 else "AM"
                display_h = start_h - 12 if start_h > 12 else start_h
                if display_h == 0: display_h = 12  # Handle 12:00

                st.info(f"⏭️ **Next Class:** {class_name} at {display_h}:{start_m:02d} {period}")
                st.metric(label="Time til next class:", value=countdown_text)
            else:
                # This happens if it's after 5:50 PM
                st.success("✅ All classes finished for today!")
    # Thursday (3) or Saturday (5)
    elif current_day == 3 or current_day == 5:
        st.subheader("Anzar's Thursday / Saturday Tracker")

        # 1. Check if CURRENTLY in class
        found_now = False
        for start, end, name in anzar_thurs_sat:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                if not 870 <= now_mins <= 980:
                    found_now = True
                    break

                # 2. If NOT in class, find the NEXT one
        if not found_now:
            st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in anzar_thurs_sat:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time = next_class[0]
                class_name = next_class[2]

                # Countdown math
                mins_to_go = start_time - now_mins
                hours_left = mins_to_go // 60
                rem_mins = mins_to_go % 60

                countdown_text = f"{hours_left}h {rem_mins}m" if hours_left > 0 else f"{rem_mins}m"

                # Start time formatting
                start_h = start_time // 60
                start_m = start_time % 60
                period = "PM" if start_h >= 12 else "AM"
                display_h = start_h - 12 if start_h > 12 else start_h
                if display_h == 0: display_h = 12  # Handle 12:00

                st.info(f"⏭️ **Next Class:** {class_name} at {display_h}:{start_m:02d} {period}")
                st.metric(label="Time til next class:", value=countdown_text)
            else:
                # This happens if it's after 5:50 PM
                st.success("✅ All classes finished for today!")
    else:
        st.success("😎 No classes today brah.")

if user_input == "L":
    # Sunday (6) or Tuesday (1)
    if current_day == 6 or current_day == 1:
        st.subheader("Labiba's Sunday / Tuesday Tracker")

        # 1. Check if CURRENTLY in class
        found_now = False
        for start, end, name in labubu_sun_tue:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                if not 870 <= now_mins <= 980:
                    found_now = True
                    break

                # 2. If NOT in class, find the NEXT one
        if not found_now:
            st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in labubu_sun_tue:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time = next_class[0]
                class_name = next_class[2]

                # Countdown math
                mins_to_go = start_time - now_mins
                hours_left = mins_to_go // 60
                rem_mins = mins_to_go % 60

                countdown_text = f"{hours_left}h {rem_mins}m" if hours_left > 0 else f"{rem_mins}m"

                # Start time formatting
                start_h = start_time // 60
                start_m = start_time % 60
                period = "PM" if start_h >= 12 else "AM"
                display_h = start_h - 12 if start_h > 12 else start_h
                if display_h == 0: display_h = 12  # Handle 12:00

                st.info(f"⏭️ **Next Class:** {class_name} at {display_h}:{start_m:02d} {period}")
                st.metric(label="Time til next class:", value=countdown_text)
            else:
                # This happens if it's after 5:50 PM
                st.success("✅ All classes finished for today!")

    # Thursday (3) or Saturday (5)
    elif current_day == 3 or current_day == 5:
        st.subheader("Labiba's Thursday / Saturday Tracker")

        # 1. Check if CURRENTLY in class
        found_now = False
        for start, end, name in labubu_thurs_sat:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                if not 870 <= now_mins <= 980:
                    found_now = True
                    break

                # 2. If NOT in class, find the NEXT one
        if not found_now:
            st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in labubu_thurs_sat:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time = next_class[0]
                class_name = next_class[2]

                # Countdown math
                mins_to_go = start_time - now_mins
                hours_left = mins_to_go // 60
                rem_mins = mins_to_go % 60

                countdown_text = f"{hours_left}h {rem_mins}m" if hours_left > 0 else f"{rem_mins}m"

                # Start time formatting
                start_h = start_time // 60
                start_m = start_time % 60
                period = "PM" if start_h >= 12 else "AM"
                display_h = start_h - 12 if start_h > 12 else start_h
                if display_h == 0: display_h = 12  # Handle 12:00

                st.info(f"⏭️ **Next Class:** {class_name} at {display_h}:{start_m:02d} {period}")
                st.metric(label="Time til next class:", value=countdown_text)
            else:
                # This happens if it's after 5:50 PM
                st.success("✅ All classes finished for today!")
    else:
        st.success("😎 No classes today brah.")

if user_input == "E":
    # Sunday (6) or Tuesday (1)
    if current_day == 6 or current_day == 1:
        st.subheader("Elhan's Sunday / Tuesday Tracker")

        # 1. Check if CURRENTLY in class
        found_now = False
        for start, end, name in elhussy_sun_tue:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                if not 870 <= now_mins <= 980:
                    found_now = True
                    break

                # 2. If NOT in class, find the NEXT one
        if not found_now:
            st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in elhussy_sun_tue:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time = next_class[0]
                class_name = next_class[2]

                # Countdown math
                mins_to_go = start_time - now_mins
                hours_left = mins_to_go // 60
                rem_mins = mins_to_go % 60

                countdown_text = f"{hours_left}h {rem_mins}m" if hours_left > 0 else f"{rem_mins}m"

                # Start time formatting
                start_h = start_time // 60
                start_m = start_time % 60
                period = "PM" if start_h >= 12 else "AM"
                display_h = start_h - 12 if start_h > 12 else start_h
                if display_h == 0: display_h = 12  # Handle 12:00

                st.info(f"⏭️ **Next Class:** {class_name} at {display_h}:{start_m:02d} {period}")
                st.metric(label="Time til next class:", value=countdown_text)
            else:
                # This happens if it's after 5:50 PM
                st.success("✅ All classes finished for today!")

    # Thursday (3) or Saturday (5)
    elif current_day == 3 or current_day == 5:
        st.subheader("Elhan's Thursday / Saturday Tracker")

        # 1. Check if CURRENTLY in class
        found_now = False
        for start, end, name in elhussy_thurs_sat:
            if start <= now_mins <= end:
                st.success(f"📍 Currently in: {name}")
                if not 870 <= now_mins <= 980:
                    found_now = True
                    break

                # 2. If NOT in class, find the NEXT one
        if not found_now:
            st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in elhussy_thurs_sat:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time = next_class[0]
                class_name = next_class[2]

                # Countdown math
                mins_to_go = start_time - now_mins
                hours_left = mins_to_go // 60
                rem_mins = mins_to_go % 60

                countdown_text = f"{hours_left}h {rem_mins}m" if hours_left > 0 else f"{rem_mins}m"

                # Start time formatting
                start_h = start_time // 60
                start_m = start_time % 60
                period = "PM" if start_h >= 12 else "AM"
                display_h = start_h - 12 if start_h > 12 else start_h
                if display_h == 0: display_h = 12  # Handle 12:00

                st.info(f"⏭️ **Next Class:** {class_name} at {display_h}:{start_m:02d} {period}")
                st.metric(label="Time til next class:", value=countdown_text)
            else:
                # This happens if it's after 5:50 PM
                st.success("✅ All classes finished for today!")

    else:
        st.success("😎 No classes today brah.")
