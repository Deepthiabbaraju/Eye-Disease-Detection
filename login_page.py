import streamlit as st
from database import authenticate_user,add_otp
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.experimental_rerun()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_alert_email(to_email, subject, message, from_email, from_password):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        pass
def login_page():
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
    with st.form(key="login_form"):
        # Title
        col1,col2=st.columns([10,1])
        col1.title("Login Here !!!")
        if col2.form_submit_button("🏚️"):
            navigate_to_page("home")

        # Email and Password inputs
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        #add forgot password link

        # Submit button inside the form
        col1,col2,col3=st.columns([1,2,1])
        with col1:
            if st.form_submit_button("Verify 🔐"):
                if authenticate_user(email, password):
                    import random
                    otp=random.randint(1000,9999)
                    to_email=email
                    subject = "OTP for login for Eye Care"
                    body = f"Hello,\n\nYour OTP for login is {otp}.\n\nThanks,\nEye Care Team"
                    from_email = 'deepthiabbaraju02@gmail.com'
                    from_password = 'kphfxyllpxxwbcst'  
                    send_alert_email(to_email, subject, body, from_email, from_password)
                    add_otp(email,otp)
                    st.success(f"Login successful.")
                    st.session_state["logged_in"] = True
                    st.session_state["current_user"] = email
                    navigate_to_page("verify")
                else:
                    st.error("Invalid email or password.")
        with col3:
            if st.form_submit_button("Forgot Password?"):
                navigate_to_page("forgot_password")