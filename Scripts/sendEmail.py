import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

# Read configuration file
config = configparser.ConfigParser()
config.read('config.cfg')

# Get email credentials from config file
sender_email = config.get('email', 'sender_email')
receiver_email = config.get('email', 'receiver_email')
password = config.get('email', 'password')

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Vivo vivo'

# Email body
body = 'Io sono vivooooo!'
msg.attach(MIMEText(body, 'plain'))

# Connect to Gmail's SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
finally:
    server.quit()
