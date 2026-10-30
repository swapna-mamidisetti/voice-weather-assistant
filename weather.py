import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geo = requests.get(geo_url).json()
    if not geo:
        return None

    lat, lon = geo[0]["lat"], geo[0]["lon"]
    weather_url = (f"https://api.openweathermap.org/data/2.5/weather"
                   f"?lat={lat}&lon={lon}&units=metric&appid={API_KEY}")
    w = requests.get(weather_url).json()

    temp = w["main"]["temp"]
    humidity = w["main"]["humidity"]
    desc = w["weather"][0]["description"]
    return (f"The temperature in {city} is {temp} degrees Celsius. "
            f"Humidity is {humidity} percent. The weather is {desc}.")

if __name__ == "__main__":
    print(get_weather("Hyderabad"))