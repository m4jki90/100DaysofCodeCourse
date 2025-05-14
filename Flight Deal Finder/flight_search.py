import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.key = os.getenv("FLIGHTAPIKEY")
        self.secret - os.getenv("FLIGHTAPISECRET")
        self._token = self._get_new_token()

    def getdestination(self,city_name):
        pass

    def _get_new_token(self):
        pass