import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

base_url = "https://api.openweathermap.org/data/2.5/weather?"

print("Welcome to the weather app.")
print("Enter the name of a city.")
city_name = input(">>> ").capitalize()

# Create the request URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

# Get the response from the API
response = requests.get(url)
x = response.json()

# Check if the response status is 200 (OK)
if x["cod"] == 200:
    main = x["main"]
    more_info = x["weather"]
    
    # Format temperature, humidity, and description correctly using f-strings
    temperature = f"Temperature: {main['temp']}°C"
    humidity = f"Humidity: {main['humidity']}%"
    detail = f"Description: {more_info[0]['description']}"
    
    # Print the weather details
    print(
        f"Weather in {city_name}:\n"
        f"{temperature}\n"
        f"{humidity}\n"
        f"{detail}"
    )
    
else:
    print("City not found.")
