import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

base_url = "https://api.openweathermap.org/data/2.5/weather?"

print("Welcome to weather app. ")
print("Enter name of a city. ")
city_name = input(">>> ").capitalize()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)
x = response.json()

if x["cod"] == 200:
    main = x["main"]
    more_info = x["weather"]
    
    temperature = f"Temperature: {main["temp"]}C"
    humidity = f"Humidity: {main["humidity"]}%"
    detail = f"Description: {more_info[0]["description"]}"
    
    print(
        f"Weather in {city_name}" +
        "\n" +
        temperature +
        "\n" +
        humidity +
        "\n" +
        detail)
    
else:
    print("City not found. ")