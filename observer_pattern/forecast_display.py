from .observer import Observer
from .subject import Subject

class ForecastDisplay(Observer):

    def __init__(self, weather_data: Subject):
        weather_data.register(self)
        self._temperature = None
        self._humidity = None

    def update_temperature(self, temperature):
        self._temperature = temperature

    def update_humidity(self, humidity):
        self._humidity = humidity
