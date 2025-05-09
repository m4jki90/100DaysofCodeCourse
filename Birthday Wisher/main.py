import datetime
import random
import smtplib
import pandas as pd

my_email = "michalczerwinski123@gmail.com"
password = "jsbrvbwzlcnbdcqo"

today = datetime.now()
today_tuple = (today.month,today.day)

data = pd.read_csv("birthdays.csv")
birthdays = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays:
    person = birthdays[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contens = contents.replace("[NAME]",person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=birthdays["email"],msg=f"Subject:Happy Birthday\n\n{contens}")



