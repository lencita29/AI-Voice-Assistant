#we use newsAPI.org ... provides JSON files to extract latest news for us
# first install 'pip install requests'
import os
from dotenv import load_dotenv
import requests

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

if not NEWS_API_KEY:
    raise ValueError("No API_KEY found in .env file")

api_address=f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWS_API_KEY}"
json_data=requests.get(api_address).json()


#know how to access list and dictionaries
ar=[]

def news():
    for i in range(5):
        ar.append("Number"+ str(i+1) +", "+ json_data["articles"][i]["title"]+".")
    return ar

ar=news()
#print(ar)





