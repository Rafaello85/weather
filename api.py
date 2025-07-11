from config import Settings
import requests
import datetime
from tools import wind_speed, konwersja

def fetch_weather ():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Settings.city}&appid={Settings.api_key}"

    try:
        response = requests.get(URL)
        weather = response.json()

        data = {
            "Odczuwalna": konwersja(weather["main"]["feels_like"]),
            "Ciśnienie": weather["main"]["pressure"],
            "Wilgotność": weather["main"]["humidity"],
            "Zwykla temperatura": konwersja(weather["main"]["temp"]),
            "Opis pogody": weather["weather"][0]["description"],
            "Miejsce": weather["name"],
            "Prędkosc wiatru": wind_speed(weather["wind"]["speed"]),
            "Data pomiaru": datetime.datetime.now()
        }
        return data

    except Exception as e:
        print (e)


fetch_weather()