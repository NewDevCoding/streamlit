import streamlit as st
import info
import pandas as pd

#About Me

def about_me():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write("---")

about_me()

def sidebar():
    st.sidebar.header("Links")

    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    
    st.sidebar.text("Checkout My Work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="GitHub" width="75" height="75"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    
    st.sidebar.text("Or email me!")
    email_html = f'<a href="{info.my_email_address}"><img src="{info.email_image_url}" alt="Instagram" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True) 

sidebar()


def education(education_data, course_data):
    st.header("Education")
    
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")

    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config = {
        "code": 'Course Code',
        "names": 'Course Names',
        "semester_taken": 'Semester Taken',
        "slills": 'What I Learned'},
        hide_index = True,
        )
    
    st.write("---")

education(info.education_data, info.course_data)


def experience(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width = 250)

        for bullet_point in job_description:
            expander.write(bullet_point)

        st.write("---")

experience(info.experience_data)

def projects(projects_data):
    st.header("Projects")
    
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)

    st.write("---")
        
projects(info.projects_data)

def skills(programming_data, spoken_data):
    st.header("Skills")
    
    st.subheader("Programming Languages")

    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill, '')}")
        st.progress(percentage)

    st.subheader("Spoken Languages")
    for spoken, profiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken, "")}: {profiency}")

    st.write("---")

skills(info.programming_data, info.spoken_data)


def activities(leadership_data, activity_data):
    st.header("Activities")

    tab1, tab2 = st.tabs(["Leadership", "Community Service"])

    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width = 250)

            for bullet_point in details:
                expander.write(bullet_point)

    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet_point in details:
                expander.write(bullet_point)

    st.write("---")

activities(info.leadership_data, info.activity_data)







