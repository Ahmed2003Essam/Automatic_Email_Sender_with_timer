from multiprocessing import context
import ssl
import smtplib
import time
import email 
from email.message import EmailMessage



email_sender = 'Email Sender' 
email_password = 'Email_Sender Password' 

#Steps to get this password: 
# 1. The user have to set "2-Step Verification"
# 2. The user will iniate a one-time password called App password to use it here 


email_receiver = "Email Receiver"


subject =  "Subject in the email will be sent"
body = "The email's body "

em = EmailMessage()

em['From'] =  email_sender
em['To'] =  email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

x =  2
while (x> 0): # The user can replace this by while true, but I thought it will be cool to be written in this way

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        time.sleep(1) # The number of seconds will be between each email
    except Exception as e:
        print(f'An error occurred: {str(e)}')