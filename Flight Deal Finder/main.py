from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.getData()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.getdestination(row["city"])
    print(f"{sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.updateData()
