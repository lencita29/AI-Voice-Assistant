import os
from dotenv import load_dotenv
import requests

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

if not WEATHER_API_KEY:
    raise ValueError("No API_KEY found in .env file")
api_address="https://api.openweathermap.org/data/2.5/weather?q=mangaluru&appid="+WEATHER_API_KEY
json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data["main"]["temp"]-273,1) #convertig from kelvin to degree and rounded it to one decimal
    return temperature

def des():
    description=json_data["weather"][0]["description"]
    return description

#print(temp())
#print(des())
#using api we can access weather
#copy and paste the api address in chrome to know where this info is accessed from
