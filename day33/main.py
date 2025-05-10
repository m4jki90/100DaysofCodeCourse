import requests
from datetime import datetime
import smtplib
import time

MY_LAT=50.971378
MY_LNG=16.928711
my_email = "michalczerwinski123@gmail.com"
password = "jsbrvbwzlcnbdcqo"

def iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= latitude <=MY_LAT+5 and MY_LNG-5<= longitude <= MY_LNG+5:
        return True
    
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted":0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data ["results"]["sunset"].split("T")[1].split(":")[0]
    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True
    
while True:
    time.sleep(60)    
    if iss() and is_night():
        with smtplib.SMTP("smtp.gmail@com") as connection:
            connection.starttls()
            connection.login()
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="Look up")
