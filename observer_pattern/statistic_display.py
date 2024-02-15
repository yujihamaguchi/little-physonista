from .observer import Observer
from .subject import Subject

class StatisticDisplay(Observer):

    def __init__(self, weather_data: Subject):
        weather_data.register(self)
        self._temperature = None

    def update_temperature(self, temperature):
        self._temperature = temperature

    def update_humidity(self, humidity):
        pass  # StatisticDisplay does not care about humidity
