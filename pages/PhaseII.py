import streamlit as st
import pandas as pd
import json
import info

# Load data from JSON file
with open("travel_data.json", "r") as f:
    data = json.load(f)
df = pd.DataFrame(data)

# Session State for dynamic graph selection #NEW
if "selected_dest" not in st.session_state:
    st.session_state.selected_dest = df["destination"][0]

st.title("My Favorite Travel Destinations")
st.write("Explore data about my favorite places I've visited, including ratings, activities, and visit history.")

# User input: Select destination (affects dynamic graphs) #NEW
selected_dest = st.selectbox("Choose a destination:", df["destination"])
st.session_state.selected_dest = selected_dest

# User input: Minimum rating filter (affects dynamic graphs) #NEW
min_rating = st.slider("Minimum rating to display:", min_value=1, max_value=10, value=5)

# Static Visualization: Bar chart of visits
st.subheader("Number of Visits to Each Destination")
st.bar_chart(df.set_index("destination")["visits"])

# Dynamic Visualization 1: Ratings filtered by user input
st.subheader("Destinations by Rating (Filtered)")
filtered_df = df[df["rating"] >= min_rating]
st.line_chart(filtered_df.set_index("destination")["rating"])

# Dynamic Visualization 2: Favorite activity for selected destination
st.subheader(f"Favorite Activity in {st.session_state.selected_dest}")
activity = df[df["destination"] == st.session_state.selected_dest]["favorite_activity"].values[0]
st.info(f"My favorite activity in {st.session_state.selected_dest} is: **{activity}**")  #NEW

# Display last visited year for selected destination #NEW
last_year = df[df["destination"] == st.session_state.selected_dest]["year_last_visited"].values[0]
st.write(f"Last visited in: {last_year}")

# requirements.txt (add any extra modules you use, e.g., matplotlib, plotly, etc.)
# For this example, only Streamlit and Pandas are needed (already included).

with open("personal_data.json", "r") as f:
    data = json.load(f)
df = pd.DataFrame(data["weeks"])

st.title("My Progress & Hobbies Dashboard")
st.write("Track and compare your weekly habits: running, working out, reading, coding, airsoft, tabletop games, and diorama building.")

# User input: Select activity #NEW
activity_options = {
    "Running": "running_days",
    "Working Out": "workout_days",
    "Reading": "books_read",
    "Coding": "coding_hours",
    "Airsoft": "airsoft_sessions",
    "Tabletop Games": "tabletop_sessions",
    "Diorama Building": "diorama_hours"
}
selected_activity = st.selectbox("Choose an activity to view progress:", list(activity_options.keys()))
activity_col = activity_options[selected_activity]
st.session_state["selected_activity"] = selected_activity  #NEW

# User input: Select number of weeks to display #NEW
num_weeks = st.slider("Number of recent weeks to display:", min_value=1, max_value=len(df), value=4)
st.session_state["num_weeks"] = num_weeks  #NEW

recent_df = df.tail(num_weeks)

# Static Visualization: Average weekly frequency for each activity
st.subheader("Average Weekly Activity Frequency")
avg_data = {k: df[v].mean() for k, v in activity_options.items()}
st.bar_chart(pd.Series(avg_data))

# Dynamic Visualization 1: Progress over time for selected activity
st.subheader(f"{selected_activity} Progress Over Time")
st.line_chart(recent_df.set_index("week")[activity_col])

# Dynamic Visualization 2: Proportion of time/effort spent (last N weeks)
st.subheader(f"Activity Proportion (Last {num_weeks} Weeks)")
pie_data = recent_df[[v for v in activity_options.values()]].sum()

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
pie_data.plot.pie(autopct='%1.1f%%', ylabel='', ax=ax)
st.pyplot(fig)


def like_project_widget(project_id: str, project_name: str):
   
    like_key = f"liked_{project_id}"

  
    if like_key not in st.session_state:
        st.session_state[like_key] = False

   
    st.subheader(project_name)

    st.image(info.app, width = 600)

    if st.session_state[like_key]:
        st.success("❤️ You liked this project!")
        if st.button("Undo Like", key=f"undo_{project_id}"):
            st.session_state[like_key] = False
    else:
        if st.button("👍 Like", key=f"like_{project_id}"):
            st.session_state[like_key] = True

like_project_widget('12345678910', 'AI learning app')