import smtplib
import datetime as dt
import random

my_email = "michalczerwinski123@gmail.com"
password = "jsbrvbwzlcnbdcqo"
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt","r") as file:
        quotes = file.readlines()
        quote = random.choice(list)

    with smtplib.SMTP("smtp.gmail.com", port=465) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=quote)
