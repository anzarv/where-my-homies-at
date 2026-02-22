import streamlit as st
import pytz
from datetime import datetime

# --- CONFIG & DATA ---
st.set_page_config(page_title="NSU Homie Tracker", page_icon="📍")

st.title("Where Are My Homies At❓")
st.write("Find where the homies are during their NSU campus schedule.")
st.caption("Made by Anzar. Message for bugs.")
st.caption("22/02/26 - Updated to Ramadan schedule + optimization")


# Time Setup
target_timezone = pytz.timezone('Asia/Dhaka')
now = datetime.now(target_timezone)
st.write("---")
st.header(now.strftime("%A, %I:%M %p"))

now_mins = (now.hour * 60) + now.minute
current_day = now.weekday()  # 0=Mon, 6=Sun

# Data Structure: { "Key": {"name": "Display Name", "sun_tue": [], "thu_sat": []} }
homie_data = {
    "A": {
        "name": "Anzar", "emoji": "👅",
        "sun_tue": [
            (735, 810, "ECO101 (NAC 605)"),
            (810, 820, "Free Period"),
            (820, 895, "ENG103 (NAC 203)")
        ],
        "thu_sat": [
            (735, 810, "ACT201 (NAC410)"),
            (820, 895, "BUS112 (NAC207)")
        ]
    },
    "E": {
        "name": "Elhan", "emoji": "😿",
        "sun_tue": [
            (735, 810, "ENG103 (NAC409)"),
            (820, 895, "PSY101 (NAC215)")
        ],
        "thu_sat": [
            (735, 810, "ECO101 (NAC412)"),
            (810, 820, "Free Period"),
            (820, 895, "BUS112 (SAC208)")
        ]
    },
    "L": {
        "name": "Labiba", "emoji": "🐥",
        "sun_tue": [
            (735, 810, "ENG103 (SAC 309)"),
            (810, 820, "Free Period"),
            (820, 895, "MAT116 (NAC 513)")
        ],
        "thu_sat": [
            (735, 810, "BIO103 (NAC301)"),
            (820, 895, "CHE101 (SAC407)")
        ]
    }
}


# --- HELPER FUNCTIONS ---

def format_time(total_mins):
    """Converts total minutes to 12-hour string format."""
    h, m = divmod(total_mins, 60)
    p = "PM" if h >= 12 else "AM"
    disp_h = h - 12 if h > 12 else h
    if disp_h == 0: disp_h = 12
    return f"{disp_h}:{m:02d} {p}"


def get_countdown(target_mins, current_mins):
    """Returns a string for time remaining."""
    diff = target_mins - current_mins
    h, m = divmod(diff, 60)
    return f"{h}h {m}m" if h > 0 else f"{m}m"


def show_homie_details(data):
    """The central logic for displaying a specific person's schedule."""
    # Select schedule
    if current_day in [6, 1]:
        schedule, day_name = data["sun_tue"], "Sunday / Tuesday"
    elif current_day in [3, 5]:
        schedule, day_name = data["thu_sat"], "Thursday / Saturday"
    else:
        st.success("😎 No classes today brah. Enjoy the vibes.")
        return

    st.subheader(f"{data['name']}'s {day_name} Tracker")
    found_now = False

    # 1. Current Status
    for start, end, name in schedule:
        if start <= now_mins <= end:
            st.success(f"📍 Currently in: {name}")
            if "Free Period" not in name:
                found_now = True
                st.write(f"🕒 This class ends at {format_time(end)}")
                st.metric("Time remaining:", get_countdown(end, now_mins))
            break

    # 2. Next Class
    if not found_now:
        # Check if they are currently in a designated Free Period (880-970 logic from original)
        if not (880 <= now_mins <= 970):
            st.error("❌ Not in class right now.")

        next_class = next((c for c in schedule if c[0] > now_mins), None)
        if next_class:
            start, end, name = next_class
            st.info(f"⏭️ **Next Class:** {name} at {format_time(start)}")
            st.metric("Time til next class:", get_countdown(start, now_mins))
        else:
            st.success("✅ All classes finished for today!")


# --- MAIN UI ---

st.write("Who you looking for dawg?")
cols = st.columns(len(homie_data))
selected_key = None

for i, (key, info) in enumerate(homie_data.items()):
    if cols[i].button(f"{info['emoji']} {info['name']}"):
        selected_key = key

if selected_key:
    show_homie_details(homie_data[selected_key])

# --- DASHBOARD ---
st.write("---")
st.header("📍 Homie Dashboard")
dash_cols = st.columns(len(homie_data))

for i, (key, info) in enumerate(homie_data.items()):
    # Determine schedule for dashboard
    sched = info["sun_tue"] if current_day in [6, 1] else info["thu_sat"] if current_day in [3, 5] else []

    with dash_cols[i]:
        if not sched:
            st.metric(info["name"], "Vibing", delta="Off Day")
            continue

        status = next((c for c in sched if c[0] <= now_mins <= c[1]), None)
        if status:
            val = "Free Period" if "Free" in status[2] else "In Class"
            st.metric(info["name"], val, delta=status[2])
        elif now_mins > sched[-1][1]:
            st.metric(info["name"], "Done", delta="Left Campus")
        else:
            st.metric(info["name"], "Not in yet", delta="Coming soon")