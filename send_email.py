import smtplib, ssl


host = "smtp.gmail.com"
port = 465

password = "gjltthnpaetvigvk"
user_name="lukasz.nawrocki.pl@gmail.com"

receiver = "lukasz.nawrocki.pl@gmail.com"
context = ssl.create_default_context()

message ="""\
Subject: Welcoming email
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_name,password)
    server.sendmail(user_name, receiver, message)


