import streamlit as st

# Display your full name and course name
st.title("Isaac Aaron Sheridan")
st.header("CS 1301")

# Brief description of your app
st.write("Welcome to my multi-page Streamlit web application! Use the sidebar to navigate between pages.")

# Descriptions for each page
st.subheader("Pages in this App")

st.markdown("""
- **Portfolio**: My personal and academic portfolio, including projects, skills, and interests.
- **Phase II**: An interactive page where you can explore and visualize data about me and my hobbies using dynamic graphs and user input.
 

""")

st.subheader("What to explore!!")

st.markdown("""
- **Destination log**: Explore my personal favorite destinations, view my visiting frequency. and see the graphed data .
- **Hobbies tracker**: Here you can view my favorite hobbies, as well how often I do them on a weekly basis.
- **Activity pie chart**: Ever want to know where your time is going each week? This pie chart lets you visualize the hours I spend each week on each of them.
 - **Project approval section**: I am in the middle of building an AI learning app, and it this section you can give my project a heart for encouragement. This function utilizes session states

""")


