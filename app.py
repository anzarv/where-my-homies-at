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
    (980, 1070, "ENG103 (NAC 203)")
]

anzar_thurs_sat = [
    (780, 870, "ACT201 (NAC410)"),
    (880, 970, "BUS112 (NAC207)")
]

labubu_sun_tue = [
    (780, 870, "ENG103 (SAC 309)"),
    (870, 980, "Free Period"),
    (980, 1070, "MAT116 (NAC 513)")
]

labubu_thurs_sat = [
    (780, 870, "BIO103 (NAC301)"),
    (880, 970, "CHE101 (SAC407)")
]

elhussy_sun_tue = [
    (780, 870, "ENG103 (NAC409)"),
    (880, 970, "PSY101 (NAC215)")
]

elhussy_thurs_sat = [
    (780, 870, "ECO101 (NAC412)"),
    (870, 980, "Free Period"),
    (980, 1070, "BUS112 (SAC208)")

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
# current_day = 5
# current_hour = 16
# current_minute = 20

now_mins = (current_hour * 60) + current_minute

# 4. Anzar's Logic
if user_input == "A":
    # Determine which schedule to use
    schedule = []
    day_name = ""

    if current_day == 6 or current_day == 1:
        schedule = anzar_sun_tue
        day_name = "Sunday / Tuesday"
    elif current_day == 3 or current_day == 5:
        schedule = anzar_thurs_sat
        day_name = "Thursday / Saturday"

    if schedule:
        st.subheader(f"Anzar's {day_name} Tracker")
        found_now = False

        # --- PART A: CHECK CURRENT STATUS ---
        for start, end, name in schedule:
            if start <= now_mins <= end:
                # If it's a real class, show the "In Class" UI
                if "Free Period" not in name:
                    st.success(f"📍 Currently in: {name}")
                    found_now = True

                    # Math for Class Countdown
                    mins_left = end - now_mins
                    h_left, m_left = divmod(mins_left, 60)
                    remaining_text = f"{h_left}h {m_left}m" if h_left > 0 else f"{m_left}m"

                    # Pretty print end time
                    end_h, end_m = divmod(end, 60)
                    p = "PM" if end_h >= 12 else "AM"
                    disp_h = end_h - 12 if end_h > 12 else end_h
                    if disp_h == 0: disp_h = 12

                    st.write(f"🕒 This class ends at {disp_h}:{end_m:02d} {p}")
                    st.metric(label="Time remaining in class:", value=remaining_text)
                    break
                else:
                    # It is the Free Period range
                    st.success(f"📍 Currently in: {name}")
                    # We leave found_now = False so the "Next Class" countdown shows below

        # --- PART B: SHOW NEXT CLASS (If not in a real class) ---
        if not found_now:
            if not (880 <= now_mins <= 970):  # If not even in Free Period
                st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in schedule:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time, end_time, class_name = next_class

                # Math for Next Class Countdown
                wait_mins = start_time - now_mins
                h_wait, m_wait = divmod(wait_mins, 60)
                wait_text = f"{h_wait}h {m_wait}m" if h_wait > 0 else f"{m_wait}m"

                # Pretty print start time
                sh, sm = divmod(start_time, 60)
                sp = "PM" if sh >= 12 else "AM"
                sdh = sh - 12 if sh > 12 else sh
                if sdh == 0: sdh = 12

                st.info(f"⏭️ **Next Class:** {class_name} at {sdh}:{sm:02d} {sp}")
                st.metric(label="Time til next class:", value=wait_text)
            else:
                st.success("✅ All classes finished for today!")
    else:
        # This handles Friday (4), Monday (0), Wednesday (2)
        st.success("😎 No classes today brah. Enjoy the vibes.")


# 5. Labubu's Logic
if user_input == "L":
    # Determine which schedule to use
    schedule = []
    day_name = ""

    if current_day == 6 or current_day == 1:
        schedule = labubu_sun_tue
        day_name = "Sunday / Tuesday"
    elif current_day == 3 or current_day == 5:
        schedule = labubu_thurs_sat
        day_name = "Thursday / Saturday"

    if schedule:
        st.subheader(f"Labiba's {day_name} Tracker")
        found_now = False

        # --- PART A: CHECK CURRENT STATUS ---
        for start, end, name in schedule:
            if start <= now_mins <= end:
                # If it's a real class, show the "In Class" UI
                if "Free Period" not in name:
                    st.success(f"📍 Currently in: {name}")
                    found_now = True

                    # Math for Class Countdown
                    mins_left = end - now_mins
                    h_left, m_left = divmod(mins_left, 60)
                    remaining_text = f"{h_left}h {m_left}m" if h_left > 0 else f"{m_left}m"

                    # Pretty print end time
                    end_h, end_m = divmod(end, 60)
                    p = "PM" if end_h >= 12 else "AM"
                    disp_h = end_h - 12 if end_h > 12 else end_h
                    if disp_h == 0: disp_h = 12

                    st.write(f"🕒 This class ends at {disp_h}:{end_m:02d} {p}")
                    st.metric(label="Time remaining in class:", value=remaining_text)
                    break
                else:
                    # It is the Free Period range
                    st.success(f"📍 Currently in: {name}")
                    # We leave found_now = False so the "Next Class" countdown shows below

        # --- PART B: SHOW NEXT CLASS (If not in a real class) ---
        if not found_now:
            if not (880 <= now_mins <= 970):  # If not even in Free Period
                st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in schedule:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time, end_time, class_name = next_class

                # Math for Next Class Countdown
                wait_mins = start_time - now_mins
                h_wait, m_wait = divmod(wait_mins, 60)
                wait_text = f"{h_wait}h {m_wait}m" if h_wait > 0 else f"{m_wait}m"

                # Pretty print start time
                sh, sm = divmod(start_time, 60)
                sp = "PM" if sh >= 12 else "AM"
                sdh = sh - 12 if sh > 12 else sh
                if sdh == 0: sdh = 12

                st.info(f"⏭️ **Next Class:** {class_name} at {sdh}:{sm:02d} {sp}")
                st.metric(label="Time til next class:", value=wait_text)
            else:
                st.success("✅ All classes finished for today!")
    else:
        # This handles Friday (4), Monday (0), Wednesday (2)
        st.success("😎 No classes today brah. Enjoy the vibes.")

# 6. Elhussy's Logic
if user_input == "E":
    # Determine which schedule to use
    schedule = []
    day_name = ""

    if current_day == 6 or current_day == 1:
        schedule = elhussy_sun_tue
        day_name = "Sunday / Tuesday"
    elif current_day == 3 or current_day == 5:
        schedule = elhussy_thurs_sat
        day_name = "Thursday / Saturday"

    if schedule:
        st.subheader(f"Elhan's {day_name} Tracker")
        found_now = False

        # --- PART A: CHECK CURRENT STATUS ---
        for start, end, name in schedule:
            if start <= now_mins <= end:
                # If it's a real class, show the "In Class" UI
                if "Free Period" not in name:
                    st.success(f"📍 Currently in: {name}")
                    found_now = True

                    # Math for Class Countdown
                    mins_left = end - now_mins
                    h_left, m_left = divmod(mins_left, 60)
                    remaining_text = f"{h_left}h {m_left}m" if h_left > 0 else f"{m_left}m"

                    # Pretty print end time
                    end_h, end_m = divmod(end, 60)
                    p = "PM" if end_h >= 12 else "AM"
                    disp_h = end_h - 12 if end_h > 12 else end_h
                    if disp_h == 0: disp_h = 12

                    st.write(f"🕒 This class ends at {disp_h}:{end_m:02d} {p}")
                    st.metric(label="Time remaining in class:", value=remaining_text)
                    break
                else:
                    # It is the Free Period range
                    st.success(f"📍 Currently in: {name}")
                    # We leave found_now = False so the "Next Class" countdown shows below

        # --- PART B: SHOW NEXT CLASS (If not in a real class) ---
        if not found_now:
            if not (880 <= now_mins <= 970):  # If not even in Free Period
                st.error("❌ Not in class right now.")

            next_class = None
            for start, end, name in schedule:
                if start > now_mins:
                    next_class = (start, end, name)
                    break

            if next_class:
                start_time, end_time, class_name = next_class

                # Math for Next Class Countdown
                wait_mins = start_time - now_mins
                h_wait, m_wait = divmod(wait_mins, 60)
                wait_text = f"{h_wait}h {m_wait}m" if h_wait > 0 else f"{m_wait}m"

                # Pretty print start time
                sh, sm = divmod(start_time, 60)
                sp = "PM" if sh >= 12 else "AM"
                sdh = sh - 12 if sh > 12 else sh
                if sdh == 0: sdh = 12

                st.info(f"⏭️ **Next Class:** {class_name} at {sdh}:{sm:02d} {sp}")
                st.metric(label="Time til next class:", value=wait_text)
            else:
                st.success("✅ All classes finished for today!")
    else:
        # This handles Friday (4), Monday (0), Wednesday (2)
        st.success("😎 No classes today brah. Enjoy the vibes.")

# --- LIVE STATUS DASHBOARD ---
st.write("---")
st.header("📍 Homie Dashboard")

# Create a list of all homies and their data for easy looping
homies = [
    {"name": "Anzar", "sun_tue": anzar_sun_tue, "thu_sat": anzar_thurs_sat},
    {"name": "Labubu", "sun_tue": labubu_sun_tue, "thu_sat": labubu_thurs_sat},
    {"name": "Elhan", "sun_tue": elhussy_sun_tue, "thu_sat": elhussy_thurs_sat},
]

cols = st.columns(3)

for i, homie in enumerate(homies):
    with cols[i]:
        # Select correct schedule
        if current_day in [6, 1]:
            current_sched = homie["sun_tue"]
        elif current_day in [3, 5]:
            current_sched = homie["thu_sat"]
        else:
            current_sched = []

        status_found = False
        if not current_sched:
            st.metric(label=homie["name"], value="Vibing", delta="No Classes Today")
        else:
            for start, end, name in current_sched:
                if start <= now_mins <= end:
                    status_found = True
                    if "Free" in name:
                        st.metric(label=homie["name"], value="Free Period", delta="Available")
                    else:
                        st.metric(label=homie["name"], value="In Class", delta=f"{name}")

            if not status_found:
                # Check if classes are over or haven't started
                last_class_end = current_sched[-1][1]
                if now_mins > last_class_end:
                    st.metric(label=homie["name"], value="Done", delta="Left Campus")
                else:
                    st.metric(label=homie["name"], value="Not in yet", delta="Coming soon")