import streamlit as st

from send_email import send_email

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    #raw_message = "Subject: Greetings from PPortfolio App! \n"+message + "\n" + user_email
    message = f"""Subject: New email from {user_email} 

From: {user_email}
{raw_message} 

:D
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfuly")
