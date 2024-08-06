import requests


API_KEY = ""


def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }


def search_locations(query):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()
