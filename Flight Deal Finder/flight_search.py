import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):
        self.key = os.getenv("FLIGHTAPIKEY")
        self.secret = os.getenv("FLIGHTAPISECRET")
        self._token = self._get_new_token()

    def getdestination(self,city_name):
        headers = {"Authorization":f"Bearer {self._token}"}
        query = {
            "keyword":city_name,
            "max":"2",
            "include":"AIRPORTS",
        }
        try:
            response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
            response.raise_for_status()  
            data = response.json()
            
            if not data.get("data"):
                print(f"No data found for {city_name}")
                return "N/A"
                
            first_result = data["data"][0]
            return first_result.get("iataCode", "N/A")
            
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {city_name}: {e}")
            return "N/A"
        except (IndexError, KeyError) as e:
            print(f"Data parsing error for {city_name}: {e}")
            return "N/A"


    def _get_new_token(self):
        header ={
             "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type":"client_credentials",
            "client_id":self.key,
            "client_secret":self.secret
        }
        response = requests.post(url=TOKEN_ENDPOINT,headers=header,data=body)
        return response.json()['access_token']
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()

