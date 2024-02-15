from dataclasses import dataclass, field
from .subject import Subject

@dataclass
class WeatherData(Subject):
    _observers: list = field(default_factory=list)
    _temperature = None
    _humidity = None

    def register(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update_temperature(self._temperature)
            observer.update_humidity(self._humidity)

    def set_measurements(self, temperature, humidity):
        self._temperature = temperature
        self._humidity = humidity
        self.notify_observers()
