from meal_planner_classes import main
import smtplib
import ssl
from email.mime.text import MIMEText
import pandas as pd



def send_email(html_str):
    with open('email.html', 'w') as f:
        print(html_str, file=f)

    email_from = 'python.test.gante@gmail.com'
    password = 'iqmcujhevpphhibq'
    email_to = 'monwlodarczyk@gmail.com'

    email_html = open('email.html')
    email_body = html_str

    # Generate today's date to be included in the email Subject
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    # Configurating user's info
    email_message = MIMEText(email_body, 'html')
    email_message['From'] = 'python.test.gante@gmail.com'
    email_message['To'] = 'monwlodarczyk@gmail.com'
    email_message['Subject'] = f'Meal planner for you! - {date_str}'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)  # Provide Gmail's login information
        server.sendmail(email_from, email_to, email_message.as_string())

    print(f"Meal planner has been successfully sent to:{email_to}!")


if __name__ == "__main__":
    html_str = main()
    send_email(html_str)
