from __future__ import annotations
import asyncio
from datetime import datetime
import pprint
import threading
import time
import requests
from controller.AbstractController import AbstractController


class WeatherDataController(AbstractController):
    API_KEY_OPEN_WEATHER = "56a81dcf3778961c19b1ce122dc8e450"
    API_KEY_WEATHER_BIT = "f8cf8bde822d4e1fb79d5b0d5af103b2"
    lat = "50.85580690844865"
    lon = "7.340034524137979"
    exclude = "minutely"
    url_open_weather = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY_OPEN_WEATHER}"
    url_weatherBit = f"https://api.weatherbit.io/v2.0/forecast/minutely?,NC&key={API_KEY_WEATHER_BIT}&units=I&lat={lat}&lon={lon}"

    def __init__(self):
        self.__three_hour_forecast = []
        self.__minute_precip_forecast = []
        self.__minutely_weather_update_listener = []
        self.__hourely_weather_update_listener = []
        self.__sunrise = None
        self.__sunset = None


    @property
    def three_hour_forecast(self) -> []:
        return self.__three_hour_forecast

    @property
    def minute_precip_forecast(self) -> []:
        return self.__minute_precip_forecast

    async def load_weather_data(self):
        print("Load new Weather Data", datetime.now())
        await asyncio.gather(self.load_minute_forecast(), self.load_three_hour_forecast())

    async def load_three_hour_forecast(self):
        data_three_hour_forecast = requests.get(self.url_open_weather)
        self.__extract_data_open_weather(data_three_hour_forecast)
        for listener in self.__hourely_weather_update_listener:
            listener(self.three_hour_forecast)

    async def load_minute_forecast(self):
        data_minute_forecast = requests.get(self.url_weatherBit)
        self.__extract_data_weather_bit(data_minute_forecast)
        for listener in self.__minutely_weather_update_listener:
            listener(self.minute_precip_forecast)

    # minutely api-request
    def __extract_data_weather_bit(self, response):
        if response.status_code != 200:
            return
        self.__minute_precip_forecast.clear()
        data = response.json()
        for entry in data["data"]:
            precip = entry["precip"]
            if precip >= 0.05:
                minute = int(entry["timestamp_local"][14:16])
                self.__minute_precip_forecast.append((minute, precip))
                print(f"Minute: {minute}, Regenwahrscheinlichkeit: {precip * 100}%")

    # three hour weather-forecast
    def __extract_data_open_weather(self, response):
        if response.status_code != 200:
            return
        self.__three_hour_forecast.clear()
        data = response.json()
        weather_entries = data["list"]
        self.__sunrise = datetime.fromtimestamp(data["city"]["sunrise"])
        self.__sunset = datetime.fromtimestamp(data["city"]["sunset"])
        print(self.__sunrise)
        for entry in weather_entries[0:8]:
            time = int(entry["dt_txt"][11:13])
            temperature = int(round(float(entry["main"]["temp_max"]) - 273.15, 0))  # Kelvin to Celcius.
            self.__three_hour_forecast.append((time, temperature))

    def register_minutely_listener(self, listener):
        self.__minutely_weather_update_listener.append(listener)
        listener(self.minute_precip_forecast)

    def register_three_hourely_listener(self, listener):
        self.__hourely_weather_update_listener.append(listener)
        listener(self.three_hour_forecast)

    def log_off_minutely_listener(self, listener):
        self.__minutely_weather_update_listener.remove(listener)

    def log_off_three_hourely_listener(self, listener):
        self.__hourely_weather_update_listener.remove(listener)

    def start(self):
        while True:
            asyncio.run(self.load_weather_data())
            time.sleep(180)

    @classmethod
    def init(cls) -> WeatherDataController:
        controller = WeatherDataController()
        thread = threading.Thread(target=controller.start, args=())
        thread.daemon = True
        thread.start()
        return controller

