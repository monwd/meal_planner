import meal_planner_classes
import pandas as pd
from IPython.display import display, HTML
from pandas import read_html as rh
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

meal_planner_classes
email_string = 'This is a test email sent by Python.'


email_from = 'python.test.gante@gmail.com'
password = 'iqmcujhevpphhibq'
email_to = 'monwlodarczyk@gmail.com'

# Generate today's date to be included in the email Subject
date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

email_message = MIMEMultipart()
email_message['From'] = 'python.test.gante@gmail.com'
email_message['To'] = 'monwlodarczyk@gmail.com'
email_message['Subject'] = f'Sending emails! - {date_str}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(meal_planner_classes, "html"))
# Convert it as a string
email_string = email_message.as_string()

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login('python.test.gante@gmail.com', 'iqmcujhevpphhibq')  # Provide Gmail's login information
    server.sendmail(email_from, email_to, email_string)
