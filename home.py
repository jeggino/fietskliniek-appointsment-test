import streamlit as st
import smtplib
from email.mime.text import MIMEText


# Taking inputs
email_sender = st.secrets["EMAIL"]
password = st.secrets["PASSWORD"]

def send_email(subject, body, sender, recipients, password):
    try:
        # Create a MIMEText object with the body of the email
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients
        # Connect to Gmail's SMTP server using SSL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        st.markdown("You have booked your appointment! Please check your email")
    except:
        st.markdown("Please check your email")



name = st.text_input("Name")
email_receiver = st.text_input("E-Mail")
date = st.date_input("Date")
time_shift = st.time_input("Time")
link = "https://payment-links.mollie.com/payment/QRHiqREMEec7PXeByiszR"

#---

subject = "Fietsklieniek appointment"
body = f"""
Dear {name},

you have booked an appont on {date} at {time_shift}.
Please, pay your fee at this link {link}.

If you need to change or cancel your appointment, please use the dedicated form. 
If you have any questions, you can also contact us by phone or email.

Regards, Fietsklienik people
"""

if st.button("Send Email"):
    send_email(subject, body, email_sender, email_receiver, password)

