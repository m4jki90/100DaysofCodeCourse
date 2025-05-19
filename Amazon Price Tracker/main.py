import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
HOST = "smtp.gmail.com"
EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASS")

header = {
    "Accept-Language": "pl-PL,pl;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}

response = requests.get(URL, headers=header)
product = response.text

soup = BeautifulSoup(product, "html.parser")
price = soup.find(name="span", class_="a-offscreen").getText().strip()
price_float = float(price.split("$")[1])
print(price_float)
title = soup.find(id="productTitle").getText().strip()
print(title)

if price_float < 100:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP(HOST, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL,PASS)
        connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))


