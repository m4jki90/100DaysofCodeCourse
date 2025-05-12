import requests
from datetime import datetime

USERNAME ="m4jki90"
TOKEN = "h62j6l35kb43jl5432345j342n9vddsa"
GRAPH_ID = "m4graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
yesterday = datetime(year=2025,month=5,day=11).strftime("%Y%m%d")

pixel_config = {
    "date":today,
    "quantity": input("How many km did you cycle today?"),
}

response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)

putdel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

put_config = {
    "quantity":"17.50"
}

response = requests.delete(url=putdel_endpoint,headers=headers)

