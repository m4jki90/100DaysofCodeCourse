import requests

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
data = response.json()
print(data)