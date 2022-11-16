import smtplib
import ssl
from email.mime.text import MIMEText

import pandas as pd

import html_generator


def send_email(html_str):
    email_from = 'python.test.gante@gmail.com'
    password = 'iqmcujhevpphhibq'
    email_to = 'monwlodarczyk@gmail.com'

    email_body = html_str

    # Generate today's date to be included in the email Subject
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    # Configurating user's info
    email_message = MIMEText(email_body, 'html')
    email_message['From'] = 'python.test.gante@gmail.com'
    email_message['To'] = 'monwlodarczyk@gmail.com'
    email_message['Subject'] = f'Meal planner for you! - {date_str}'

    # Connect to the Gmail SMTP server and Send Email
    # Create a secure default settings context
    context = ssl.create_default_context()

    # Connect to Gmail's SMTP Outgoing Mail server with such context
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)  # Provide Gmail's login information
        server.sendmail(email_from, email_to, email_message.as_string())

    print(f"Meal planner has been successfully sent to: {email_to}!")


def main_sending_email():
    html_str = html_generator.main_generator()
    send_email(html_str)


if __name__ == "__main__":
    main_sending_email()
