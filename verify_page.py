import streamlit as st
from database import fetch_user,add_otp,fetch_otp

def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()

def verify_page():
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
    with st.form(key="verify_form"):
        st.title("Verify OTP !!!")
        ver_otp=fetch_otp(st.session_state["current_user"])
        otp = st.text_input("Enter OTP")
        col1,col2=st.columns([1,1])
        with col1:
            if st.form_submit_button("Verify",type='primary'):
                if otp:
                    st.success("Verified")
                    navigate_to_page("user_home")
                else:
                    st.error("Invalid OTP")
    
