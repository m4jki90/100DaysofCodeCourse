import requests
from datetime import datetime


APP_ID = "d5d21239"
API_KEY = "dfa58693b5438864260486cbaf9633ee"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = "84"
HEIGHT = "183"
AGE = "19"
SHEET_ENDPOINT = "https://api.sheety.co/0b5e2a0fc3fa6835fa228c56d48b3210/workoutTracking/workouts"
USERNAME = "m4jki90"
PASSWORD = "Jazdaman6990"


today_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

parameters = {
    "query":input("Tell me which exercises you did: "),
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE,
}



response = requests.post(url=ENDPOINT,headers=headers,json=parameters)
result = response.json()
for exercise in result["exercises"]:
    sheet_parameters = {
        "workout": {
            "date":today_date,
            "time":time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response2 = requests.post(url=SHEET_ENDPOINT, json=sheet_parameters,auth=(USERNAME,PASSWORD))
    print(response2.text)





