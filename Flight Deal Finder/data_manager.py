from pprint import pprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/0b5e2a0fc3fa6835fa228c56d48b3210/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.user = os.getenv("_USERNAME")
        self.password = os.getenv("PASSWORD")
        self.destination_data = {}
        
    def getData (self):
        response = requests.get(url=SHEETY_ENDPOINT,auth=(self.user,self.password))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def updateData (self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",json=new_data,auth=(self.user,self.password))
            print(response.text)
        


