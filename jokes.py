#we use api that is common for all
import requests

url="https://official-joke-api.appspot.com/random_joke"
#enter the url in chrome to know wha's inside
json_data=requests.get(url).json()

arr=["",""]
arr[0]=json_data["setup"]
arr[1]=json_data["punchline"]

def joke():
    return arr