import streamlit as st
import smtplib
from email.mime.text import MIMEText


# Taking inputs
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
    try:
        msg = MIMEText(body)
        msg['From'] = st.secrets["EMAIL"]
        msg['To'] = email_receiver
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(st.secrets["EMAIL"], st.secrets["PASSWORD"])
        resp = smtp_server.rcpt(recipients)
        st.write(resp)
        server.sendmail(st.secrets["EMAIL"], email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")

