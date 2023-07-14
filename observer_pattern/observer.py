from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update_temperature(self, temperature):
        pass

    @abstractmethod
    def update_humidity(self, humidity):
        pass
