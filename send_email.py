import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user_name = os.getenv("USER_NAME")
    receiver = user_name
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)


#send_email()


