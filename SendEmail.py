#SendEmail.py

import smtplib
from datetime import datetime




sender_email = ''
receiver_email = ''
password = ''
subject = ""
message = ""

def send_email():
    # Set up your email details

    # Create the message
    text = f"Subject: {subject}\n\n{message}"


    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)


    # Send the email
    server.sendmail(sender_email, receiver_email, text)


    # Close the server connection
    print("Email has been sent to " + receiver_email)
    server.quit()

