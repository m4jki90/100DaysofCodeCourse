import requests
from twilio.rest import Client
from twilio import *

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API="NGQPCZISQ72V3TON"
NEWS_API="7e4a939daa8c4d0d87dc34edd37b555d"



stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API,
}


response = requests.get(STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday = data_list[0]
day_before = data_list[1]
yesterday_close = float(yesterday["4. close"])
day_before_close = float(day_before["4. close"])
difference = round(abs(yesterday_close-day_before_close),2)
difference_percentage = round(100 * difference/yesterday_close,2) 

if yesterday_close - day_before_close > 0:
    sign = "🔺"
else:
    sign="🔺"

if difference_percentage > 1:
    news_params = {
    "qInTitle":COMPANY_NAME,
    "apiKey":NEWS_API,
}
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {sign}{difference_percentage}\nHeadline: {article["title"]}.\nBrief description: {article["description"]}" for article in three_articles]
    client = Client(TWILIO_SID,TWILIO_TOKEN)
    for article in formatted_articles:
        message = client.messages \
                        .create( body= article,
                                from_=TWILIO_NUM,
                                to=MY_NUM
                        )



