import streamlit as st
from database import fetch_user,add_otp,fetch_otp
import time
import random
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()

def forgot_page():
    # Center the login form using Streamlit form layout
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url("https://blindspot.ai/assets/img/intro-background.svg?3");  
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title("Reset Your Password 🔑")
    
    with st.form(key="forgot_password_form"):
        email = st.text_input("Enter your registered email")
        if st.form_submit_button("Send OTP"):
            user = fetch_user(email)
            otp = random.randint(1000,9999)
            if fetch_otp(email)[0]==0:
                add_otp(email,otp)
                st.success("OTP sent successfully. Please check your email.")
            st.write(fetch_otp(email))
            st.write(otp)
            