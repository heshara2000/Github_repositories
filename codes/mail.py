import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'your_email@gmail.com'
receiver_email = 'receiver_email@gmail.com'
password = 'your_app_password'  # Use the generated App Password here

# Create a message object
message = MIMEMultipart()
message['from'] = sender_email
message['to'] = receiver_email
message['subject'] = 'Testing1'

body = 'Hello, I am Hesharadananjanee, and I am from Kadawatha.'
message.attach(MIMEText(body, 'plain'))

# Connect to SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Login
    server.login(sender_email, password)
    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully")

except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
