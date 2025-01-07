import streamlit as st
from streamlit_option_menu import option_menu
from database import fetch_user
import pandas as pd
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()

def user_home_page():
    user = fetch_user(st.session_state["current_user"])
    with st.sidebar:
        st.markdown(f"<h1 style='text-align: center;'>𝐖𝐄𝐋𝐂𝐎𝐌𝐄 👋 {user[1]}</h1>", unsafe_allow_html=True)
        st.image('https://static.vecteezy.com/system/resources/previews/026/773/363/non_2x/eye-with-ai-generated-free-png.png', use_column_width=True)
        select = option_menu(
            "",
            ["Patient Profile",'Predictions', 'Generate Report',"Queries","Logout"],
            icons=['person-square','eye-fill','file-earmark-fill','question-circle-fill' ,'lock-fill'],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
            styles={
                "container": {"padding": "0", "background-color": "#d6d6d6"}, 
                "icon": {"color": "black", "font-size": "20px"},    
                "nav-link": {
                    "font-size": "16px",
                    "margin": "0px",
                    "color": "black",                                          
                },   
                "nav-link-selected": {
                    "background-color": "#10bec4",                            
                },
            },
        )

    if select == 'Patient Profile':
        st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://scitechdaily.com/images/AI-Vision-Eye-Examination-Art-Concept.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
        )

        # Extracting user data from session state after successful login
        if user:
            # Assuming 'user' is a tuple (id, name, email, password, regd_no, year_of_study, branch, student_type, student_image)
            name, age, gender,eye_power,eye_problem = user[1], user[3], user[4],user[5],user[6]
            if gender == 'Male👦🏻':
                image_link = "https://img.freepik.com/photos-premium/elevez-votre-marque-avatar-amical-qui-reflete-professionnalisme-ideal-pour-directeurs-ventes_1283595-18531.jpg?semt=ais_hybrid"
            else:
                image_link = "https://cdn-icons-png.flaticon.com/512/219/219969.png"

            # CSS Styling for vertical container
            profile_css = """
            <style>
                .profile-container {
                    background-color: #10bec4;
                    padding: 50px;
                    border-radius: 50px;
                    box-shadow: 10px 8px 12px rgba(0, 0, 0, 0.15);
                    max-width: 400px;
                    border: 2px solid black;
                    margin-left: 100%;
                    margin: auto;
                    font-family: Arial, sans-serif;
                    text-align: center;
                }
                .profile-header {
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 1px;
                    color: #333;
                }
                .profile-item {
                    font-size: 18px;
                    margin-bottom: 10px;
                    color: #555;
                }
                .profile-image img {
                    border-radius: 50%;
                    max-width: 250px;
                    max-height: 250px;
                    margin-bottom: 0px;
                }
            </style>
            """

            # HTML Structure for vertical alignment
            profile_html = f"""
            <div class="profile-container">
                <div class="profile-image">
                    <img src="{image_link}" alt="User Image">
                </div>
                <div class="profile-details">
                    <div class="profile-header">User Report</div>
                    <div class="profile-item"><strong>Name:</strong> {name}</div>
                    <div class="profile-item"><strong>Age:</strong> {age}</div>
                    <div class="profile-item"><strong>Gender:</strong> {gender}</div>
                    <div class="profile-item"><strong>Eye Power:</strong> {eye_power}</div>
                    <div class="profile-item"><strong>Eye Problem:</strong> {eye_problem}</div>
                </div>
            </div>
            """

            # Display styled content
            st.markdown(profile_css + profile_html, unsafe_allow_html=True)
    elif select == 'Queries':
        st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url("https://t3.ftcdn.net/jpg/02/26/11/28/360_F_226112855_yeHzKpT5GlvblgZlibf9MvJZLVjsqGYf.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
        )
        with st.form('About Us'):
            # Contact Us Form
            st.subheader(f"Enter your Query❓")
            # Create form fields
            name = user[1]
            email = user[2]
            issue = st.text_area('Query❗',height=100)
            # Submit button
            if st.form_submit_button("Submit"):
                if issue:
                    # Process the form data (you can save it or send an email here)
                    st.success("Thank you for reaching out! We'll get back to you soon.")
                else:
                    st.error("Please fill in all fields before submitting.")

    elif select == 'Logout':
        st.session_state["logged_in"] = False
        st.session_state["current_user"] = None
        navigate_to_page("home")
