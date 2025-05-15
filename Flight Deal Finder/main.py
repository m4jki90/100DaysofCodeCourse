from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime, timedelta
import time
from flight_data import find_cheapest_flight

data_manager = DataManager()
sheet_data = data_manager.getData()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LON"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.getdestination(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.updateData()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    time.sleep(2)