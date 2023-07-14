from .subject import Subject

class WeatherData(Subject):

    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None

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
